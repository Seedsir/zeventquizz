from uuid import uuid4
from typing import Dict

from questions.exceptions import ItemNotFoundException


class MemoryStorage:
    def __init__(self):
        self._storage = {}

    def get_id(self):
        return str(uuid4())

    def add(self, obj: Dict):
        obj["id"] = self.get_id()
        self._storage[obj["id"]] = obj
        return obj

    def get_all(self):
        return self._storage.values()

    def get(self, id: str):
        item = self._storage.get(id, None)
        if item is None:
            raise ItemNotFoundException
        return item

    def delete(self, id: str) -> None:
        del self._storage[id]
