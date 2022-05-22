import dbAccessorBase


class ProductsDbAccessor(dbAccessorBase.DBAccessorBase):
    def __init__(self):
        super().__init__('products')
