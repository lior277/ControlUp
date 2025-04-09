from abc import ABC, abstractmethod

class IProductsPage(ABC):
    @abstractmethod
    def get_inventory_items(self) -> int:
        pass

    @abstractmethod
    def click_on_add_to_cart_btn_by_index(self, item_index: int):
        pass

    @abstractmethod
    def get_cart_count(self) -> str:
        pass