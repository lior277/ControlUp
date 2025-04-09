from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from infrastructure.infra.dal.web_driver_extension.web_driver_extension import DriverEX
from infrastructure.objects.objects_ui.interfaceses.products_page_ui_interface import IProductsPage


class ProductsPageUi(IProductsPage):
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    # locators
        self.__inventory = By.CSS_SELECTOR, "div[data-test='inventory-item']"
        self.__add_to_cart_btn = By.CSS_SELECTOR, "button[id*='add-to-cart']"
        self.__cart_count = By.CSS_SELECTOR, "span[class*='shopping_cart_badge']"

    def get_inventory_items(self) -> int:
        return len(DriverEX.search_elements(driver=self.__driver, by=self.__inventory))

    def click_on_add_to_cart_btn_by_index(self, item_index: int):
        buttons = DriverEX.search_elements(driver=self.__driver, by=self.__add_to_cart_btn)
        DriverEX.force_click(driver=self.__driver, element=buttons[item_index])
        return self

    def get_cart_count(self) -> str:
        return DriverEX.get_element_text(driver=self.__driver, by=self.__cart_count)
