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
    def __init__(self,db:DataBase,delete_not_use_columns:bool=False):
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

        # Проверка на отсутствие нужных полей в таблице
        columns_in_table = self.db.select(f"PRAGMA table_info({self.table_name})")
        columns_names = [item['name'] for item in columns_in_table]

        if(len(columns_names) < len(self.fields)):
            l = list(set(self.fields)- set(columns_names))
            for f in l:
                fieldConfig = self.__class__.__dict__[f].to_string()
                print(f"В таблице '{self.table_name}' отсутствует поле '{f} {fieldConfig}'!  Добавляем поле...  " )
                self.db.execute(f"ALTER TABLE {self.table_name} ADD COLUMN {f} {fieldConfig};")  
        elif(len(columns_names) > len(self.fields)):    
            if(not delete_not_use_columns):
                raise Exception(f"В таблице '{self.table_name}' присутствуют лишние поля!!!!\r\nПожалуйста, удалите лишние поля вручную или установите параметр 'delete_not_use_columns' в конструкторе на True.\r\nПример: {self.table_name}(database, delete_not_use_columns=True)")
            else:
                l = list(set(columns_names) - set(self.fields))
                for f in l:
                    self.db.execute(f"ALTER TABLE {self.table_name} DROP COLUMN {f};")


        
    
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
        for row in result: tabrows.append(Table(**row))
        if(len(tabrows)==1):return tabrows[0]
        else: return tabrows

        # print(sql)
    def get_all(self):
        return self.get()
    def get_last(self):
        sql = f"SELECT * FROM {self.table_name} ORDER BY id DESC LIMIT 1"
        result = self.db.select(sql)
        if(result is []):return None
        Table = namedtuple(self.table_name," ".join(self.fields))
        vals = {}
        for field,val in zip(self.fields,result[0]):
            vals[field] = val
        return Table(**vals)
    
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
        return self.get_last()
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