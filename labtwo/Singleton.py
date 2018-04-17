class Singleton(type):
    instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class SingletonObject(object):
    __metaclass__ = Singleton


a = SingletonObject()
b = SingletonObject()

print("singleton object a: " + a.__class__.__name__)
print("singleton object b: " + b.__class__.__name__)
