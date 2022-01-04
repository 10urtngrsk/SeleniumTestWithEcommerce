from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_xpath = '//*[@id="txtUserName"]'
        self.password_textbox_xpath = '//*[@id="txtPassword"]'
        self.homepage_log_in_button_xpath = '//*[@id="login"]'
        self.log_in_button_after_username_enter_xpath = '//*[@id="btnLogin"]'
        self.log_in_button_after_password_enter_xpath = '//*[@id="btnEmailSelect"]'
        self.invalid_username_enter_alert_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[4]/div/div/div[1]/div[2]'
        self.invalid_email_enter_alert_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]'

    def make_button_visible(self):
        self.driver.execute_script("arguments[0].style.visibility = 'visible';",
                                   self.driver.find_element(By.XPATH,self.homepage_log_in_button_xpath))

    def click_homepage_log_in_button(self):
        self.driver.find_element(By.XPATH,self.homepage_log_in_button_xpath).click()

    def enter_username(self,username):
        self.driver.find_element(By.XPATH,self.username_textbox_xpath).send_keys(username)

    def click_log_in_after_username_enter(self):
        self.driver.find_element(By.XPATH,self.log_in_button_after_username_enter_xpath).click()

    def click_log_in_after_password_enter(self):
        self.driver.find_element(By.XPATH,self.log_in_button_after_password_enter_xpath).click()

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.password_textbox_xpath).send_keys(password)
