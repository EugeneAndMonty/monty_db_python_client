from models import DocsDb, KvsDb, SqlDb, FirstCollection

DocsDb.create_store()
KvsDb.create_store()
SqlDb.create_store()
# FirstCollection.create_collection()

# DocsDb.drop_store()
# KvsDb.drop_store()
# SqlDb.drop_store()
# FirstCollection.drop_collection()



























# DocsDb.create_store()
# DocsDb.drop_store()

# from key_value_model import KeyValueModel
# from doc_model import CollectionModel

# engine = Engine("127.0.0.1", 21210, "MONTY", "CAT")
# kv_warehouse = KeyValueModel(engine, 'db2')
# collections_warehouse = CollectionModel(engine, 'db2')

# some_dict = {}
# for i in range(100):
#     some_dict[f"key{i}"] = f"value{i}"

# res = kv_warehouse.insert_bulk(some_dict, 300)

# print(res)
