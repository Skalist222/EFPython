from Entity_Framework.v_types import *
from Entity_Framework.v_DB import *
class SQLite_Table:
    sql_create_table:str
    db:DataBase
    def __init__(self,db:DataBase):
        table_name = self.__class__.__name__
        self.db = db
        fields_list=[]
        for k,v in self.__class__.__dict__.items():
            if(not k.startswith("__")):
                v:SQLite_Type = v 
                fields_list.append(" ".join(['"'+k+'"',v.to_string()]))
        fields:str=", ".join(fields_list)
        sql_create_table = f"CREATE TABLE {table_name} IF NOT EXISTS({fields})"
        self.db.execute(sql_create_table)



class TemplateTable(SQLite_Table):
    id=ID()
    name=TEXT()
    age=TEXT()
    admin=BOOl()

class TemplateTable2(SQLite_Table):
    id=ID()
    name=TEXT()
    description=TEXT()
    nomenclative_id=TEXT()
