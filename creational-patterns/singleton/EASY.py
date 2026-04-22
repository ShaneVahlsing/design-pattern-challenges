# Implement 'CashRegister' using the __new__ method.
# If 'reg1' and 'reg2' are created, they must both point to the same object.

class CashRegister:
    singleInstance = None

    def __new__(cls, *args, **kwargs):
        if cls.singleInstance is None:
            cls.singleInstance = super(CashRegister,cls).__new__(cls)

        return cls.singleInstance
    
reg1 = CashRegister()
reg2 = CashRegister()

print(reg1 is reg2)