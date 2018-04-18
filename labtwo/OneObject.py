class OneObject:
    instance = None

    class OneObjectTester:
        def __call__(self, *args, **kw):
            if OneObject.instance is None:
                obj = OneObject()
                OneObject.instance = obj
            return OneObject.instance

    getInstance = OneObjectTester()

    def __init__(self):
        if OneObject.instance is not None:
            raise RuntimeError('Only one instance of is allowed in this class!')


for i in range(7):
    print(OneObject.getInstance())

# Check if single instance of One Object already exists if not throw error
OneObject()
