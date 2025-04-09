import pytest
from tests.test_suit_Base import TestSuitBase


@pytest.fixture(scope='function')
def browser():
    driver = TestSuitBase.get_driver()
    yield driver
    TestSuitBase.driver_dispose(driver=driver)




