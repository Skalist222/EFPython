class BASETYPE:
    field_type: str #название типа данных поля, например, "INTEGER"
    unique:bool
    null:bool
    default:bool

    def __init__(self, unique: bool = False, null: bool = True, default: int = None):
        self.unique = unique
        self.null = null
        self.default = default


class INTEGER(BASETYPE):
    autoincrement:bool
    field_type ="INTEGER"
    def __init__(self, unique:bool = False, null:bool = True, default:int = None,autoincrement =True):
        self.autoincrement = autoincrement
        super().__init__(unique, null, default)

class TEXT(BASETYPE):
    field_type ="TEXT"
    
class BLOB(BASETYPE):
    field_type ="BLOB"

class REAL(BASETYPE):
    field_type ="REAL"

class NUMERIC(BASETYPE):
    field_type ="NUMERIC"