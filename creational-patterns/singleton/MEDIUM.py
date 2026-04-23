# Create 'ShopConfig'. It must store 'shop_name' and 'is_open'. 
# Ensure that updating the name via one variable updates it for all references in the app.

class ShopConfig:
    shop = None

    def __new__(cls, *args, **kwargs):
        ...