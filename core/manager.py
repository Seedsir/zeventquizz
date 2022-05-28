from storage.storage import MemoryStorage
from typing import Dict
import logging
from core.exceptions import ItemNotFoundException

logger = logging.getLogger(__name__)


class EntityManager:
    def __init__(self):
        self._storage = MemoryStorage()

    def get_all(self):
        return self._storage.get_all()

    def get(self, item_id: str) -> Dict:
        item = {}
        try:
            item = self._storage.get(item_id)
        except ItemNotFoundException as inf:
            logger.warning(f"item {item_id} not found")
        finally:
            return item

    def delete(self, item_id: str) -> Dict:
        item = self.get(item_id)
        if item:
            self._storage.delete(item_id)
        return item

    def create(self, item: Dict) -> Dict:
        return self._storage.add(item)

    def update(self, item: Dict) -> Dict:
        return self._storage.add(item)
