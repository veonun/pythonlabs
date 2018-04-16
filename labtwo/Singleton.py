class Singleton(type):
    instance = None

    def __call__(clas, *args, **kw):
        if not clas.instance:
            clas.instance = super(Singleton, clas).__call__(*args, **kw)
        return clas.instance


class SingletonObject(object):
    __metaclass__ = Singleton


a = SingletonObject()
b = SingletonObject()

print("singleton object a: " + a.__class__.__name__)
print("singleton object b: " + b.__class__.__name__)
