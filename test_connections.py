from models import KvsDb, FirstCollection
from store_classes.doc_based.schema import Schema
# print(KvsDb.insert_key("key1", 10, True))
print(KvsDb.insert_key_value_pair("key2", "value2"))
# print(KvsDb.get_value("key1"))
# print(KvsDb.get_keys())
# print(KvsDb.delete_key("key1"))
# print(KvsDb.update_value("key2", "value3"))
# print(KvsDb.delete_bulk({"key3": "value3", "key4": "value4"}))

# class User(Schema):
#     name: str
#     age: int
#     profession: str
#     collegues: list

# user = User(name='John', age=25, profession='developer', collegues=['Jane', 'Jack'])
# user1 = User(name='John')

# print(FirstCollection.insert_document(
#     document=user,
#     expire_sec=300, persistent=True
# ))

# print(FirstCollection.delete_document(
#     document=user1
# ))
