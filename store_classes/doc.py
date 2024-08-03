from engine import Engine
from store_functions.store_generic_functions import connect_engine_, create_store_, drop_store_, show_store_properties_
import json

class generic_doc:
    store_type: str = "store_doc"

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
