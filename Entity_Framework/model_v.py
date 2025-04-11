class Model:
    def __init__(self, *args, **kwargs):
        fields = [el for el in vars(self.__class__) if not el.startswith("__")] #поля, которые мы создали в модели (в данном случае name, width, height)
        for i, value in enumerate(args):
            setattr(self, fields[i], value)#задаем переменные переданные с помощью args

        for field, value in kwargs.items():#задаем переменные переданные с помощью kwargs
            setattr(self, field, value)
    def json(self):
        attributes = {}
        for key, value in vars(self).items():
            if not key.startswith("__") and not callable(value):#проверка на системные методы и поля
                attributes[key] = value
        
        return attributes