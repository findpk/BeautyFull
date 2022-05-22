import sys
sys.path.insert(0, '/Users/praveenkumarb/Documents/pk-workspace/BeautyFull/lib/db-accessor')
import cartsDbAccessor
import productsDbAccessor
sys.path.insert(0, '/Users/praveenkumarb/Documents/pk-workspace/BeautyFull/lib/helpers')
import commonHelper


class Manager:
    def __init__(self):
        self.productsDbAccessor = productsDbAccessor.ProductsDbAccessor()
        self.cartsDbAccessor = cartsDbAccessor.CartsDbAccessor()
        self.commonHelper = commonHelper

    def createCart(self, id):
        payload = {
            "cart_id": id,
            "bo_id": "B0"+commonHelper.generateRandomString(10),
            "products": [],
            "tags": [],
            "status": "Initiated",
        }
        return self.cartsDbAccessor.createCart(payload)