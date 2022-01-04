import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
from Web_Pages.Login_Page import LoginPage
from Utils.Users import get_username


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_with_valid_user(self):
        driver = self.driver
        self.driver.get("https://hepsiburada.com")

        login = LoginPage(driver)
        login.make_button_visible()
        login.click_homepage_log_in_button()
        user = get_username("valid_user")
        login.enter_username(user["email"])
        login.click_log_in_after_username_enter()
        time.sleep(5)
        login.enter_password(user["password"])
        login.click_log_in_after_password_enter()
        time.sleep(5)
        assert "Online "in driver.title

    def test_login_with_invalid_user_1(self):
        driver = self.driver
        self.driver.get("https://hepsiburada.com")

        login = LoginPage(driver)
        login.make_button_visible()
        login.click_homepage_log_in_button()
        user = get_username("invalid_user")
        login.enter_username(user["email"])
        login.click_log_in_after_username_enter()
        time.sleep(5)
        login.enter_password(user["password"])
        login.click_log_in_after_password_enter()
        time.sleep(5)
        element = self.driver.find_element(By.XPATH,login.invalid_username_enter_alert_xpath).text
        assert "Girdiğiniz şifre eksik veya hatalı." in element

    def test_login_with_invalid_user_2(self):
        driver = self.driver
        self.driver.get("https://www.hepsiburada.com")

        login = LoginPage(driver)
        login.make_button_visible()
        login.click_homepage_log_in_button()
        user = get_username("invalid_user_2")
        login.enter_username(user["email"])
        login.click_log_in_after_username_enter()
        time.sleep(10)
        element = self.driver.find_element(By.XPATH,login.invalid_email_enter_alert_xpath).text
        assert "E-posta adresi eksik veya hatalı." in element

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed.")

if __name__ == '__main__':
    unittest.main()
