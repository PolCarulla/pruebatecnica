import psycopg2
import os
import urllib.parse as up


class dbManager:
    def __init__(self):
        up.uses_netloc.append("postgres")
        self.url = up.urlparse(os.environ["covid19_database"])
    def connect(self):
        try:
            self.conn = psycopg2.connect(database=self.url.path[1:],
                user=self.url.username,
                password=self.url.password,
                host=self.url.hostname,
                port=self.url.port
                )
            print("Connected to Database")
        except Exception as e:
            print("Error connecting to Database")
            print(e)
    
    def makeQuery(self,query):
        try:
            cmd = "INSERT INTO covid19(day,comarca,fv_doses) VALUES(%s,%s,%s)"
            cursor = self.conn.cursor()
            cursor.executemany(cmd,query)
            self.conn.commit()
            cursor.close()

        except Exception as e:
            print(e)
    
    def disconnect(self):
        try:
            self.conn.close()
            print("Disconnected from Database")
        except Exception as e:
            print("Error disconnecting")
            print(e)