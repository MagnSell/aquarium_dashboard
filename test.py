import database_communication as db

conn = db.initialize_conn()
for i in range(10):
    print(db.get_newest_fish(conn).loc[:,['timestamp','fish_id']])
db.close_conn(conn)