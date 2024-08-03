from engine import Engine

def connect_engine_(cls: type, engine: Engine) -> None:
    cls.username = engine.username
    cls.password = engine.password
    cls.host = engine.host
    cls.port = engine.port

def create_store_(cls: type) -> None:
    return print('CREATE', cls.store_name, cls.store_type)

def drop_store_(cls: type) -> None:
    return print('DROP', cls.store_name, cls.store_type)

def show_store_properties_(cls: type) -> None:
    return print(cls.store_name, cls.store_type, cls.username, cls.password, cls.host, cls.port)
