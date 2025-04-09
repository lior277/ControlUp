from infrastructure.infra.dal.data_reposetory.data_rep import DataRep
from infrastructure.infra.utils.assert_utils import CustomAssert
from infrastructure.objects.objects_ui.login_page_ui import LoginPageUi
from infrastructure.objects.objects_ui.products_page_ui import ProductsPageUi
from tests.test_suit_Base import TestSuitBase

class TestVerifyInventoryItemsCountUi(TestSuitBase):
    @classmethod
    def setup_class(cls):
        # This runs once for the class
        cls.driver = cls.get_driver()
        cls.driver.get(DataRep.saucedemo_url)

        # Initialize page objects
        cls.login_page_ui = LoginPageUi(cls.driver)

        # Perform login
        cls.login_page_ui \
            .set_user_name(DataRep.user_name) \
            .set_password(DataRep.password) \
            .click_on_login_btn()

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver_dispose(driver=cls.driver)

    def test_verify_inventory_items_count(self):
        product_page = ProductsPageUi(self.driver)

        inventory_items = product_page \
            .get_inventory_items()

        CustomAssert.assert_true(
            inventory_items == 6,
            f"Expected inventory items: 6, Actual inventory items: {inventory_items}"
        )

