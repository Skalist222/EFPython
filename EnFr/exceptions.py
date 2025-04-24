# 24.04.2025
class ImportantParametrNotSet(Exception):
    def __init__(self, parametrname):
        super().__init__(f"Важный параметр не установлен: {parametrname}")
class SettedAutoincrementParametr(Exception):
    def __init__(self, parametrname):
        super().__init__(f"Нельзя отправить {parametrname} так как это автоматически инкрементируемое поле")
class FieldDeleteNotSetted(Exception):
    def __init__(self, table_name):
        super().__init__(f"В таблице '{table_name}' присутствуют лишние поля!!!!\r\nПожалуйста, удалите лишние поля вручную или установите параметр 'delete_not_use_columns' в конструкторе на True.\r\nПример: {table_name}(database, delete_not_use_columns=True)")