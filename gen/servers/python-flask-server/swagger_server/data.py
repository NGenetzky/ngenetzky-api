
from tinydb import TinyDB
from tinydb import where

class Db():
    def __init__(self):
        self.db = TinyDB('/data/db.json')

    def post(self, table, json):
        t = self.db.table(table)
        return t.insert(json)

    def put(self, table, id_, json):
        t = self.db.table(table)
        return t.upsert(json, where('id') == json['id'])

    def get(self, table, id_):
        t = self.db.table(table)
        return t.get(where('id') == id_)

