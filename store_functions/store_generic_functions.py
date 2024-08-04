from engine import Engine, send_data
import asyncio
import json

def connect_engine_(cls: type, engine: Engine) -> None:
    cls.username = engine.username
    cls.password = engine.password
    cls.host = engine.host
    cls.port = engine.port

def _convert_to_binary(cls: type):
    return json.dumps({
        "request": cls.request,
        "username": cls.username, 
        "password": cls.password, 
        "command": cls.command,
        "store_type": cls.store_type,
        "store_name": cls.store_name,
        }).encode('utf-8')

def run_query(cls: type):
    query = _convert_to_binary(cls)
    print(query)
    return asyncio.run(send_data(cls.host, cls.port, query))

def create_store_(cls: type) -> None:
    cls.command = "create_store"
    cls.request = "utils"
    return run_query(cls)

def drop_store_(cls: type) -> None:
    cls.reuest = "utils"
    return print('DROP', cls.store_name, cls.store_type)

def show_store_properties_(cls: type) -> None:
    return print(cls.store_name, cls.store_type, cls.username, cls.password, cls.host, cls.port)
