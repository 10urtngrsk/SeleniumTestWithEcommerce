from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.search_input_xpath = '//*[@id="SearchBoxOld"]/div/div/div[1]/div[2]/input'
        self.search_button_xpath =  '//*[@id="SearchBoxOld"]/div/div/div[2]'
        self.return_home_button_xpath = '//*[@id="oldHeader_845e6619-4b4c-4a9f-ae17-521432b665b8"]/div/div/div[2]/div[1]'
        self.return_to_top_button_xpath = '//*[@id="container"]/div/div/main/div[2]/span'

    def search_with_input(self,search_input):
        self.driver.find_element(By.XPATH,self.search_input_xpath).send_keys(search_input)

    def click_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def click_return_home_button(self):
        self.driver.find_element(By.XPATH,self.return_home_button_xpath).click()

    def scroll_down_page(self,vertical):
        self.driver.execute_script('window.scrollTo(0, {})'.format(vertical))

    def click_return_to_top_button(self):
        self.driver.find_element(By.XPATH,self.return_to_top_button_xpath).click()
