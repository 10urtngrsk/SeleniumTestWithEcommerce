import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Web_Pages.Orders_Page import OrdersPage
from Tests.Login_Page_Test import LoginTest

class OrdersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_my_orders_1(self):
        driver = self.driver
        self.driver.get("https://hepsiburada.com")

        orders = OrdersPage(driver)
        login = LoginTest.test_login_with_valid_user(self)
        time.sleep(5)
        print("Succesfuly logged in system.")
        orders.click_orders_page_button()
        assert "Siparişlerim" in self.driver.title
        time.sleep(5)

    def test_my_favourites_1(self):
        driver = self.driver
        self.driver.get("https://hepsiburada.com")

        orders = OrdersPage(driver)
        login = LoginTest.test_login_with_valid_user(self)
        time.sleep(5)
        print("Succesfuly logged in system.")
        orders.click_orders_page_button()
        time.sleep(5)
        orders.click_favourite_list()
        assert "Listem" in self.driver.title
        time.sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed.")

if __name__ == '__main__':
    unittest.main()