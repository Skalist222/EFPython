from abc import ABC
from EnFr.v_tables import *
from EnFr.v_DB import *
from EnFr.v_types import *
from collections import namedtuple




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
            if(not k.startswith("__")):
                self.fields.append(k)
                v:SQLite_Type = v 
                fields_list.append(" ".join(['"'+k+'"',v.to_string()]))
        fields:str=", ".join(fields_list)
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {'"'+self.table_name+'"'}({fields})"
        self.db.execute(sql_create_table)
    
    def get(self,**kwargs):
        # if "limit" in kwargs:
        WHERE_LIST = []
        for k,v in kwargs.items():
            if k in self.fields:
                if type(v) is int or type(v) is float:
                    WHERE_LIST.append(f"{k} = {v}")
                else: 
                    WHERE_LIST.append(f"{k} = '{v}'" )
        WHERE =""
        if(len(WHERE_LIST)>0):WHERE = " WHERE "+" AND ".join(WHERE_LIST)
        sql = f"SELECT * FROM {self.table_name}{WHERE}"
        result = self.db.select(sql)
        if(result is []):return None
        Table = namedtuple(self.table_name," ".join(self.fields))
        tabrows = []
        for row in result:
            vals = {}
            for field,val in zip(self.fields,row):
                vals[field] = val
            tabrows.append(Table(**vals))
        return tabrows

        # print(sql)
    def get_all(self):
        return self.get()
    
    def create(self,**kwargs):
        params ={}
        for field,v in self.__class__.__dict__.items():
            if(not field.startswith("__")):
                field_type:SQLite_Type = v
                if (not field_type.nullable) and field not in kwargs and not field_type.autoincrement:
                    raise Exception(f"Отсутствует обязательный параметр {field}")
                
                if field_type.autoincrement and field in kwargs: 
                    raise Exception(f"Нельзя отправить {field} так как это автоматически инкрементируемое поле")
                    
                if field in kwargs:
                    params["'"+field+"'"] = "'"+str(kwargs[field])+"'"

        sql = f"INSERT INTO {self.table_name} ({", ".join(params.keys())}) VALUES ({", ".join(params.values())})"
        self.db.execute(sql)
    def update(self,key,**kwargs):
        params = []
        for field,v in self.__class__.__dict__.items():
            if(not field.startswith("__")):
                field_type:SQLite_Type = v
                if field_type.primary:
                    WHERE = f"WHERE {field} = '{key}'"
                else:
                    params.append(f"{field} = '{kwargs[field]}'") 
        sql = f"UPDATE {self.table_name} SET {', '.join(params)} {WHERE}"  
        return self.db.execute(sql)
                    
                    

        
                    

                    
                    
                




class Users(SQLite_Table):
    id = ID()
    last_name =TEXT()
    first_name = TEXT()
    patr_name = TEXT()
    login =TEXT()
    password = TEXT()
    role = TEXT()