import abc
import sqlite3 


class DataBase:
    connection=None
    @classmethod
    def select(self,sql:str)->list[dict]:pass
    @classmethod
    def execute(self,sql:str)->bool:pass

class SQLite(DataBase):
    def __init__(self,baseName):
        self.connection = sqlite3.connect(baseName)
    
        
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