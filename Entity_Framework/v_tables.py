from Entity_Framework.v_types import *
from Entity_Framework.v_DB import *

# 12.04.2025
class SQLite_Table:
    table_name:str
    fields:list
    db:DataBase
    def __init__(self,db:DataBase):
        self.fields=[]
        sql_create_table:str
        self.table_name = self.__class__.__name__
        self.db = db
        fields_list=[]
        for k,v in self.__class__.__dict__.items():
            self.fields.append(k)
            if(not k.startswith("__")):
                v:SQLite_Type = v 
                fields_list.append(" ".join(['"'+k+'"',v.to_string()]))
        fields:str=", ".join(fields_list)
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {'"'+self.table_name+'"'}({fields})"
        self.db.execute(sql_create_table)
    
    def __get__(self,**kwargs):
        for k,v in kwargs:
            print(k)
            print(v)
            print("")



class Users(SQLite_Table):
    id = ID()
    last_name =TEXT()
    first_name = TEXT()
    patr_name = TEXT()
    login =TEXT()
    password = TEXT()
    role = TEXT()