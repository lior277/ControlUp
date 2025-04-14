import os
import sys

import pytest
from tests.test_suit_Base import TestSuitBase


@pytest.fixture(scope='function')
def browser():
    driver = TestSuitBase.get_driver()
    yield driver
    TestSuitBase.driver_dispose(driver=driver)




sys.path.append(os.path.dirname(os.path.abspath(__file__)))