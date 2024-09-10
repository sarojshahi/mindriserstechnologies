#import all the necessary modules
from selenium.webdriver.common.by import By
import time

class PostPlusTwoPage:
    def __init__(self,driver):
        self.driver = driver
        self.course_card = By.XPATH,"//li[2]//a[1]//div[1]"

    def open_page(self,url):
        self.driver.get(url)

    def scroll_window(self):
        target_y = 1800
        scroll_distance = 800
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)

    def open_card(self):
        self.driver.find_element(*self.course_card).click()

