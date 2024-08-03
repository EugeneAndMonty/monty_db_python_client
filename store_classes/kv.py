from engine import Engine, send_data
from store_functions.store_generic_functions import connect_engine_, create_store_, drop_store_, show_store_properties_
import json
import asyncio

class generic_kv:
    store_type: str = "store_kv"
    command: str = ""
    persistent: bool = False

    @classmethod
    def _convert_to_binary(cls, key = "", value = None, expire_sec: int = 0, bulk: dict = None):
        return json.dumps({
            "username": cls.username, 
            "password": cls.password, 
            "store_type": cls.store_type, #model
            "store_name": cls.store_name, #db_name
            "persistent": cls.persistent, 
            "key": key, 
            "value": value,
            "command": cls.command, 
            "expire": expire_sec,
            "bulk": {"bulk": bulk},
            }).encode('utf-8')
    
    @classmethod
    def _run_query(cls, query: str):
        return asyncio.run(send_data(cls.host, cls.port, query))
    
    @classmethod
    def insert_key(cls, key: str, expire_sec: int = 0, persistent: bool = False):
        cls.command = "insert_key"
        cls.persistent = persistent
        query = cls._convert_to_binary(key, expire_sec=expire_sec)
        return cls._run_query(query)
    
    @classmethod
    def insert_key_value_pair(cls, key: str, value, expire_sec: int = 0, persistent: bool = False):
        cls.command = "insert_key_value_pair"
        cls.persistent = persistent
        query = cls._convert_to_binary(key, value, expire_sec=expire_sec)
        return cls._run_query(query)
    
    @classmethod
    def get_value(cls, key: str):
        cls.command = "get_value"
        query = cls._convert_to_binary(key)
        return cls._run_query(query)
        
    @classmethod
    def get_keys(cls):
        cls.command = "get_keys"
        query = cls._convert_to_binary()
        return cls._run_query(query)
    
    @classmethod
    def delete_key(cls, key: str):
        cls.command = "delete_key"
        query = cls._convert_to_binary(key)
        return cls._run_query(query)

    @classmethod
    def update_value(cls, key: str, value):
        cls.command = "update_value"
        query = cls._convert_to_binary(key, value)
        return cls._run_query(query)
    
    @classmethod
    def insert_bulk(cls, bulk: dict, expire_sec: int = 0, persistent: bool = False):    
        cls.command = "insert_bulk"
        persistent = persistent
        query = cls._convert_to_binary(bulk=bulk, expire_sec=expire_sec)
        return cls._run_query(query)
    
    @classmethod
    def delete_bulk(cls, bulk: list):
        cls.command = "delete_bulk"
        query = cls._convert_to_binary(bulk=bulk)
        return cls._run_query(query)
    
    @classmethod
    def get_bulk(cls, bulk: list):
        cls.command = "get_bulk"
        query = cls._convert_to_binary(bulk=bulk)
        return cls._run_query(query)
    
    @classmethod
    def connect_engine(cls, engine: Engine) -> None:
        connect_engine_(cls, engine)

    @classmethod  
    def create_store(cls):
        create_store_(cls)
    
    @classmethod
    def drop_store(cls):
        drop_store_(cls)

    @classmethod
    def show_store_properties(cls):
        show_store_properties_(cls)

