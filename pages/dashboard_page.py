#Import all the neccessary modules
from selenium.webdriver.common.by import By


#Define Class for Dashboard Page
class Dashboard_Page:
    def __init__(self, driver):
        self.driver = driver
        self.interested_course_field = By.XPATH,""
        self.name_field = By.XPATH,""
        self.email_field = By.XPATH,""
        self.phone_field = By.XPATH,""

    def enter_course(self):
        self.driver.find_element(*self.interested_course_field)
