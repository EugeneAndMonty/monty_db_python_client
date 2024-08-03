from store_classes.sql import generic_tab
from store_classes.kv import generic_kv
from store_classes.doc import generic_doc

class Store:
    store_name: str = None
    
    class doc(generic_doc):
        __init__ = generic_doc.__init__

    class kv(generic_kv):
        __init__ = generic_kv.__init__

    class sql(generic_tab):
        __init__ = generic_tab.__init__



