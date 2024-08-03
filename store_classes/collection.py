from store import Store
import json

class Collection:
    collection_name: str = None
    persistent: bool = False
    exp_sec: int = 0
    command: str = ""

    @classmethod
    def select_store(cls, store: Store) -> None:
        cls.store_name = store.store_name
        cls.username = store.username
        cls.password = store.password
        cls.host = store.host
        cls.port = store.port
        cls.store_type = store.store_type
    
    @classmethod
    def _convert_to_binary(cls, document: dict = None, expire_sec: int = 0, bulk: list = None):
        return json.dumps({
            "username": cls.username, 
            "password": cls.password, 
            "store_type": cls.store_type, #db_type
            "store_name": cls.store_name, #db_name
            "persistent": cls.persistent, 
            "collection": cls.collection_name, 
            "document": document.__dict__,
            "command": cls.command, 
            "expire": expire_sec,
            "bulk": {"bulk": bulk},
            }).encode('utf-8')
    
    @classmethod
    def create_collection(cls, persistent: bool = False):
        cls.command = "create_collection"
        cls.persistent = persistent
        return cls._convert_to_binary(collection=cls.collection_name)
    
    @classmethod
    def drop_collection(cls):
        cls.command = "drop_collection"
        return cls._convert_to_binary(collection=cls.collection_name)
    
    @classmethod
    def insert_document(cls, document: dict, expire_sec: int = 0, persistent: bool = False):
        cls.command = "insert_document"
        cls.persistent=persistent
        return cls._convert_to_binary(document=document, expire_sec=expire_sec)
    
    @classmethod
    def delete_document(cls, document: dict):
        cls.command = "delete_document"
        return cls._convert_to_binary(document=document)
