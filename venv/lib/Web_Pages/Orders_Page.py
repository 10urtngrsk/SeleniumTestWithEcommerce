from selenium.webdriver.common.by import By

class OrdersPage():
    def __init__(self,driver):
        self.driver = driver
        self.orders_button_link_text = "Siparişlerim"
        self.favourites_list_xpath = "/html/body/div/div[4]/div/div/div/div[4]/aside/div/div/div/div/div[3]/div[2]/div/a/div[2]"

    def click_orders_page_button(self):
        self.driver.find_element(By.LINK_TEXT,self.orders_button_link_text).click()

    def click_favourite_list(self):
        self.driver.find_element(By.CSS_SELECTOR,".customerAccount-MyListMenuItem-3zatc").click()




