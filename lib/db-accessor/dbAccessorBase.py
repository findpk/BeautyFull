import pymongo

host = 'localhost'
port = 27017


class DBAccessorBase:
    def __init__(self, tableName):
        self.tableName = tableName
        self.database = 'beautyfull'
        if(not hasattr(self, 'my_client')):
            self.my_client = pymongo.MongoClient(host, port)
