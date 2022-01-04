import time
from selenium import webdriver
import unittest
from Web_Pages.Home_Page import HomePage
from Tests.Login_Page_Test import LoginTest

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://hepsiburada.com")
        cls.driver.maximize_window()

    def test_home_page_1(self):
        driver = self.driver
        self.driver.get("https://hepsiburada.com")
        home_page = HomePage(driver)
        home_page.search_with_input("Iphone 13")
        home_page.click_search_button()
        time.sleep(5)
        assert "Iphone 13" in driver.title

    def test_home_page_2(self):
        driver = self.driver
        self.driver.get("https://hepsiburada.com")
        home_page = HomePage(driver)
        home_page.click_search_button()
        home_page.search_with_input("Apple Watch SE")
        home_page.click_search_button()
        time.sleep(5)
        assert "Apple Watch SE" in self.driver.title

    def test_home_page_3(self):
        driver = self.driver
        self.driver.get("https://hepsiburada.com")
        home_page = HomePage(driver)
        home_page.scroll_down_page(3000)
        time.sleep(5)
        home_page.click_return_to_top_button()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed.")

if __name__ == '__main__':
    unittest.main()