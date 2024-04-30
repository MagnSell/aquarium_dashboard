import os
import uuid
import psycopg2
import psycopg2.extras
import pandas as pd
from dotenv import load_dotenv
import pandas as pd


def initialize_conn():
    # Load environment variables from .env file
    load_dotenv()

    db_url = os.getenv("DATABASE_URL")
    # Get database connection details from environment variables
    print("Trying to connect to the database")
    conn = psycopg2.connect(
        db_url,
        application_name="$ docs_simplecrud_psycopg2",
        cursor_factory=psycopg2.extras.RealDictCursor,
    )
    print("Connected to the database")

    psycopg2.extras.register_uuid()
    return conn


def close_conn(conn):
    # Close communication with the database
    conn.close()
    print("Closed the connection to the database")


def select_node_measurements_as_df(conn):
    # Create a cursor object to execute SQL queries
    print("Selecting all the Node_Measurement rows")
    cursor = conn.cursor()

    # Select all the Node_Measurement rows
    cursor.execute("SELECT * FROM Node_Measurement")

    # Fetch all the rows from the result
    rows = cursor.fetchall()
    df = pd.DataFrame(rows).sort_values(by="timestamp")
    # Commit the changes to the database
    conn.commit()

    return df

def get_newest_node_measurements_as_df(conn, n):
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Select the newest N Node_Measurement rows
    cursor.execute(f"SELECT * FROM Node_Measurement ORDER BY timestamp DESC LIMIT {n}")

    # Fetch all the rows from the result
    rows = cursor.fetchall()
    df = pd.DataFrame(rows).sort_values(by="timestamp")
    # Commit the changes to the database
    conn.commit()

    return df


def get_newest_fish(conn):
    # Create a cursor object to execute SQL queries
    n=4
    cursor = conn.cursor()

    # Select the newest N Node_Measurement rows
    cursor.execute(f"SELECT * FROM Fish ORDER BY timestamp DESC LIMIT {n}")

    # Fetch all the rows from the result
    rows = cursor.fetchall()
    df = pd.DataFrame(rows).sort_values(by="timestamp")
    # Commit the changes to the database
    conn.commit()

    # Convert UUID values to string
    df['uuid'] = df['uuid'].apply(lambda x: str(x))
    # Convert timestamp column to string
    df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))

    # Round 'x_position','y_position','z_position','x_velocity','y_velocity','z_velocity' columns to 3 decimals
    df[['x_position','y_position','z_position','x_velocity','y_velocity','z_velocity']] = df[['x_position','y_position','z_position','x_velocity','y_velocity','z_velocity']].round(3)

    return df