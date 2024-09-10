#import all the necessary modules
from selenium.webdriver.common.by import By
import time


#Define class for Placement Partner Page
class PlacementPartnerPage:
    def __init__(self,driver):
        self.driver = driver

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