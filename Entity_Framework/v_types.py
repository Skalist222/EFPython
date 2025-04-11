class SQLite_Type:
    field_name:str
    unique:bool
    nullable:bool
    default:str|int
    autoincrement:bool

    def __init__(self,field_name:str,unique:bool=False,nullable:bool=True,default:str|int=None,autoincrement:bool=False):
        self.field_name = field_name
        self.unique = unique
        self.nullable = nullable
        self.default = default
        self.autoincrement = autoincrement

class TEXT(SQLite_Type):
    field_name = "TEXT"
    def __init__(self, unique = False, nullable = True, default = None, autoincrement = False):
        super().__init__(self.field_name, unique, nullable, default, autoincrement)
class STR(TEXT):pass
class STRING(TEXT):pass

class INTEGER(SQLite_Type):
    field_name = "INTEGER"
    def __init__(self, unique = False, nullable = True, default = None, autoincrement = False):
        super().__init__(self.field_name, unique, nullable, default, autoincrement)
class INT(INTEGER):pass

class REAL(SQLite_Type):
    field_name = "REAL"
    def __init__(self, unique = False, nullable = True, default = None, autoincrement = False):
        super().__init__(self.field_name, unique, nullable, default, autoincrement)
class FLOAT(REAL):pass

class BLOB(SQLite_Type):
    field_name = "BLOB"
    def __init__(self, unique = False, nullable = True, default = None, autoincrement = False):
        super().__init__(self.field_name, unique, nullable, default, autoincrement)
class BOOl(BLOB):pass
class BOOLEAN(BLOB):pass

class IDINT(INTEGER):
    unique=True
    nullable=False
    default=None
    def __init__(self, autoincrement=True):
        super().__init__(self.unique, self.nullable, self.default, autoincrement)
class INTID(IDINT):pass
class ID(IDINT):pass
class TEXT_ID(TEXT):
    unique=True
    nullable=False
    autoincrement=False
    default=None
    def __init__(self):
        super().__init__(self.unique, self.nullable, self.default, self.autoincrement)