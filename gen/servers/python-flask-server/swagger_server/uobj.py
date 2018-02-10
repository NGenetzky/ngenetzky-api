from .models.universal_object import UniversalObject
from .models.register import Register
from tinydb import TinyDB
from tinydb import where
from uuid import uuid1

def create_reg(args=None):
    r = Register('uint', 0)
    o = post_object(r)
    return o

def post_object(model, t: str=None):
    if t is None:
        t = model.__class__.__name__

    db = TinyDB('/data/db.json')

    d = model.to_dict()
    i = db.table(t).insert(d)

    u = uuid1()
    o  = UniversalObject( uuid=str(u), type=t, id=i )
    db.table(o.__class__.__name__).insert(o.to_dict())

    return o
