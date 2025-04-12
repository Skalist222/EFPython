import sqlite3 

# 12.04.2025
class DataBase:
    connection=None
    baseName:str
    def __init__(self,baseName):
        self.baseName = baseName
        self.create_connection(baseName)

    @classmethod
    def create_connection(self,baseName):pass
    @classmethod
    def close_connection(self,baseName):pass
    @classmethod
    def valid_connection(self)->bool:
        try:
            if self.connection is None: return False
            if self.baseName == "": return False
            return True
        except: return False
    @classmethod
    def select(self,sql:str)->list[dict]:pass
    @classmethod
    def execute(self,sql:str)->bool:pass


class SQLite(DataBase):

    connection:sqlite3.Connection
    def create_connection(self,baseName):
        self.connection = sqlite3.connect(baseName)
    def close_connection(self):
        self.connection.close()

    def valid_connection(self)->bool:
        if not super().valid_connection(): return False
        try:
            if self.connection.in_transaction: return False
            self.connection.cursor()
            return True
        except: return False
    
            

    def select(self,sql:str)->list[dict]:
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if result is None: return []
        else: return result
        
   
    def execute(self,sql:str)->bool:
        cursor = self.connection.cursor()
        cursor.execute(sql)
        if cursor.fetchone() is None: return False
        else: return True
    
    # connection:Connection = sqlite3.connect()