# 12.04.2025
class SQLite_Type:

    field_name:str
    primary:bool
    unique:bool
    nullable:bool
    default:str|int
    autoincrement:bool

    def __init__(self,field_name:str,unique:bool=False,primary:bool=False,nullable:bool=True,default:str|int=None,autoincrement:bool=False):
        self.field_name = field_name
        self.unique = unique
        self.nullable = nullable
        self.default = default
        self.autoincrement = autoincrement
        self.primary = primary
        if self.autoincrement: self.primary = True

    def to_string(self):
        items = []
        items.append(self.field_name)
        if(self.primary):items.append("PRIMARY KEY")
        if(self.autoincrement):items.append("AUTOINCREMENT")
        if(self.nullable):items.append("NULL")
        else: items.append("NOT NULL")
        if(self.unique):items.append("UNIQUE")
        return " ".join(items)
    # CREATE TABLE название_таблицы (название_столбца1 тип_данных атрибуты_столбца1, название_столбца2 тип_данных атрибуты_столбца2 ). 


class TEXT(SQLite_Type):
    field_name = "TEXT"
    def __init__(self, unique = False,primary=False, nullable = True, default = None, autoincrement = False):
        super().__init__(self.field_name, unique, primary, nullable, default, autoincrement)
class STR(TEXT):pass
class STRING(TEXT):pass

class INTEGER(SQLite_Type):
    field_name = "INTEGER"
    def __init__(self, unique = False,primary=False, nullable = True, default = None, autoincrement = False):
        super().__init__(self.field_name, unique, primary, nullable, default, autoincrement)
class INT(INTEGER):pass

class REAL(SQLite_Type):
    field_name = "REAL"
    def __init__(self, unique = False,primary=False, nullable = True, default = None, autoincrement = False):
        super().__init__(self.field_name, unique, primary, nullable, default, autoincrement)
class FLOAT(REAL):pass

class BLOB(SQLite_Type):
    field_name = "BLOB"
    
    def __init__(self, unique = False,primary=False, nullable = True, default = 1, autoincrement = False): 
        super().__init__(self.field_name, unique, primary, nullable, default, autoincrement)
class BOOl(BLOB):pass
class BOOLEAN(BLOB):pass

class IDINT(INTEGER):
    unique=False
    nullable=False
    default=None
    def __init__(self, autoincrement=True):
        super().__init__(self.unique,True, self.nullable, self.default, autoincrement)
class INTID(IDINT):pass
class ID(IDINT):pass
class TEXT_ID(TEXT):
    unique=True
    nullable=False
    autoincrement=False
    default=None
    def __init__(self):
        super().__init__(self.unique,True, self.nullable, self.default, self.autoincrement)

class SQLITE_VARIANTS:
    NUMBER_TYPES=[INT,INTEGER,ID,INTID,IDINT,FLOAT,REAL]
    BOOLEAN_TYPES=[BOOLEAN,BOOl,BLOB]
    TEXT_TYPES=[TEXT,TEXT_ID,STR,STRING]
    