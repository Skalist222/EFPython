from Entity_Framework.model_v import Model
from Entity_Framework.types_v import *
class Table(Model):
  name = TEXT()
  width = INTEGER()
  height = INTEGER()
class Users():
  id= INTEGER(null=False,unique=True)