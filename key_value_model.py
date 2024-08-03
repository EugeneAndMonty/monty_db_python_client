# from engine import Engine, send_data
# import asyncio
# import json

# class KeyValueModel:
#     # def __init__(self, engine: Engine, db_name: str, persistent: bool = False):
#     # self.type = "store_kv"
#     # engine = None
#     # store_name = None
#     persistent = False

#     @classmethod
#     def select_store(cls, store) -> None:
#         cls.store_name = store.store_name
#         cls.store_type = store.store_type
#         cls.username = store.username
#         cls.password = store.password
#         cls.host = store.host
#         cls.port = store.port

#     def binary(self, key = "", value = None, expire_sec: int = 0, bulk: dict = None):
#         return json.dumps({
#             "username": self.engine.username, 
#             "password": self.engine.password, 
#             "model": self.type,
#             "db_name": self.db_name,
#             "persistent": self.persistent, 
#             "key": key, 
#             "value": value,
#             "command": self.command, 
#             "expire": expire_sec,
#             "bulk": {"bulk": bulk},
#             }).encode('utf-8') #type #persistent #command #key #value
    
#     def insert_key(self, key: str, expire_sec: int = 0):
#         self.command = "insert_key"
#         return asyncio.run(send_data(self.engine, self.binary(key, None, expire_sec))) #True or False

#     def insert_key_value(self, key: str, value, expire_sec: int = 0):
#         self.command = "insert_key_value"
#         return asyncio.run(send_data(self.engine, self.binary(key, value, expire_sec))) #True or False
    
#     def get_value(self, key: str):
#         self.command = "get_value"
#         return asyncio.run(send_data(self.engine, self.binary(key))) #value or "Key not found"
    
#     def get_keys(self):
#         self.command = "get_keys"
#         return asyncio.run(send_data(self.engine, self.binary())) #[]
    
#     def delete_key(self, key: str):
#         self.command = "delete_key"
#         return asyncio.run(send_data(self.engine, self.binary(key))) #True or False
    
#     def update_value(self, key: str, value, expire_sec: int = 0):
#         self.command = "update_value"
#         return asyncio.run(send_data(self.engine, self.binary(key, value, expire_sec))) #True or False
    
#     def insert_bulk(self, key_value_pairs: dict, expire_sec: int = 0):
#         self.command = "insert_bulk"
#         return asyncio.run(send_data(self.engine, self.binary("", None, expire_sec, key_value_pairs))) #True or False
    
#     def get_bulk(self, keys: list):
#         self.command = "get_bulk"
#         return asyncio.run(send_data(self.engine, self.binary("", None, 0, keys))) #{"key1": "value1", "key2": "value2"} or "Key not found"
    
#     def delete_bulk(self, keys: list):
#         self.command = "delete_bulk"
#         return asyncio.run(send_data(self.engine, self.binary("", None, 0, keys))) #{"key1": "value1", "key2": "value2"} or "Key not found"

# class KeyValueModel:
#     def __init__(self, engine: Engine, db_name: str, persistent: bool = False):
#         self.type = "store_kv"
#         self.engine = engine
#         self.db_name = db_name
#         self.persistent = persistent

#     def binary(self, key = "", value = None, expire_sec: int = 0, bulk: dict = None):
#         return json.dumps({
#             "username": self.engine.username, 
#             "password": self.engine.password, 
#             "model": self.type,
#             "db_name": self.db_name,
#             "persistent": self.persistent, 
#             "key": key, 
#             "value": value,
#             "command": self.command, 
#             "expire": expire_sec,
#             "bulk": {"bulk": bulk},
#             }).encode('utf-8') #type #persistent #command #key #value
    
#     def insert_key(self, key: str, expire_sec: int = 0):
#         self.command = "insert_key"
#         return asyncio.run(send_data(self.engine, self.binary(key, None, expire_sec))) #True or False

#     def insert_key_value(self, key: str, value, expire_sec: int = 0):
#         self.command = "insert_key_value"
#         return asyncio.run(send_data(self.engine, self.binary(key, value, expire_sec))) #True or False
    
#     def get_value(self, key: str):
#         self.command = "get_value"
#         return asyncio.run(send_data(self.engine, self.binary(key))) #value or "Key not found"
    
#     def get_keys(self):
#         self.command = "get_keys"
#         return asyncio.run(send_data(self.engine, self.binary())) #[]
    
#     def delete_key(self, key: str):
#         self.command = "delete_key"
#         return asyncio.run(send_data(self.engine, self.binary(key))) #True or False
    
#     def update_value(self, key: str, value, expire_sec: int = 0):
#         self.command = "update_value"
#         return asyncio.run(send_data(self.engine, self.binary(key, value, expire_sec))) #True or False
    
#     def insert_bulk(self, key_value_pairs: dict, expire_sec: int = 0):
#         self.command = "insert_bulk"
#         return asyncio.run(send_data(self.engine, self.binary("", None, expire_sec, key_value_pairs))) #True or False
    
#     def get_bulk(self, keys: list):
#         self.command = "get_bulk"
#         return asyncio.run(send_data(self.engine, self.binary("", None, 0, keys))) #{"key1": "value1", "key2": "value2"} or "Key not found"
    
#     def delete_bulk(self, keys: list):
#         self.command = "delete_bulk"
#         return asyncio.run(send_data(self.engine, self.binary("", None, 0, keys))) #{"key1": "value1", "key2": "value2"} or "Key not found"