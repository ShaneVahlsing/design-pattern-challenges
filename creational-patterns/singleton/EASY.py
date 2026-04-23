# Implement 'CashRegister' using the __new__ method.
# If 'reg1' and 'reg2' are created, they must both point to the same object.
# i.e 'reg1 is reg2' must return True

class CashRegister:
    register = None

    def __new__(cls, *args, **kwargs):
        if cls.register is None:
            cls.register = super(CashRegister,cls).__new__(cls)

        return cls.register
    
reg1 = CashRegister()
reg2 = CashRegister()

print(reg1 is reg2)