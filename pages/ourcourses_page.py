#import all the necessary modules
from selenium.webdriver.common.by import By
import time


#Define class for Our Courses Page
class OurCoursesPage:
    def __init__(self,driver):
        self.driver = driver
        self.search_field = By.XPATH,"//input[@name='searchTerm']"
        self.search_button = By.XPATH,"//button[@class='btn-simple']//*[name()='svg']"
        self.search_result = By.XPATH,"//section[1]//div[2]//div[1]//ul[1]//li[1]//a[1]"


    def open_page(self,url):
        self.driver.get(url)

    def scroll_window(self):
        target_y = 4000
        scroll_distance = 1000
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(1)

    def enter_searchfield(self,search):
        self.driver.find_element(*self.search_field).send_keys(search)

    def click_searchbutton(self):
        self.driver.find_element(*self.search_button).click()

    def click_searchresult(self):
        self.driver.find_element(*self.search_result).click()
