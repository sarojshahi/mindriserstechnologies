#Import all the neccessary modules
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#Define Class for Dashboard Page
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.interested_course_field = By.ID,"course"
        self.name_field = By.XPATH,"//input[@placeholder='Full Name']"
        self.email_field = By.XPATH,"//input[@placeholder='Email']"
        self.phone_field = By.XPATH,"//input[@placeholder='Phone Number']"
        self.submit_button = By.XPATH,"//button[@name='name']"

    def open_page(self,url):
        self.driver.get(url)

    #Method To Scroll window Vertically
    def scroll_window(self):
        target_y = 8000
        scroll_distance = 2000
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)

    def enter_course(self):
        courses = self.driver.find_element(*self.interested_course_field)
        select = Select(courses).select_by_index(4)

    def enter_name(self,name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()