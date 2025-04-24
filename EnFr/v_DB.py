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
        try:
            if self.connection.in_transaction: return False
            cursor = self.connection.cursor()
            cursor.close()
            return True
        except: return False
    
            

    def select(self,sql:str)->list[dict]:
        print("select:",sql)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        columns = list(map(lambda x: x[0], cursor.description))
        result = cursor.fetchall()

        if(result):
            retResult = []
            for row in result:
                retResult.append(dict(zip(columns, row)))
            cursor.close()
            return retResult
        else:
            cursor.close()
            return []
                
   
    def execute(self,sql:str)->bool:
        print("execute:",sql)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        
        if cursor.lastrowid == -1:
            cursor.close()
            return False
        else:
            cursor.close() 
            return True
    
    # connection:Connection = sqlite3.connect()