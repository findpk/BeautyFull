import dbAccessorBase


class CartsDbAccessor(dbAccessorBase.DBAccessorBase):
    def __init__(self):
        super().__init__('carts')
        self.collection_name = self.my_client[self.database][self.tableName]

    def createCart(self, payload):
        self.collection_name.insert_one(payload)
        del(payload['_id'])
        return payload
