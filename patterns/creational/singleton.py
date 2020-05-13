class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


a = Singleton()
b = Singleton()
print(a)  # <__main__.Singleton object at 0x00000220866EF400>
print(b)  # <__main__.Singleton object at 0x00000220866EF400>
