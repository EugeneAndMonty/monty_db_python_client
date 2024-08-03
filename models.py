import json
from store import Store
from engine import Engine
from store_classes.collection import Collection

#connection
class Connection(Engine):
    username = "MONTY"
    password = "CAT"
    host = "127.0.0.1"
    port = 21210

#dbs
class DocsDb(Store.doc):
    store_name = "users"

class KvsDb(Store.kv):
    store_name = "temp"

class SqlDb(Store.sql):
    store_name = "sql_stuff"

#db connections
DocsDb.connect_engine(Connection)
KvsDb.connect_engine(Connection)
SqlDb.connect_engine(Connection)

#collections
class FirstCollection(Collection):
    collection_name = "first"

#collection selection
FirstCollection.select_store(DocsDb)
