#import all the necessary selenium modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

#import all the pages
from pages.home_page import HomePage
from pages.ourcourses_page import OurCoursesPage


#Set Up the Chrome Driver Instance
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    #Yield the driver
    yield driver
    #Close the driver instance
    driver.quit()

def test_homepage(driver):
    homepage = HomePage(driver)
    homepage.open_page("https://www.mindrisers.com.np/")
    driver.maximize_window()
    time.sleep(1)
    homepage.scroll_window()
    time.sleep(1)
    homepage.enter_course()
    time.sleep(1)
    homepage.enter_name("Goku Supersaiyan")
    time.sleep(1)
    homepage.enter_email("goku@supersaiyan.com")
    time.sleep(1)
    homepage.enter_phone("9818123456")
    time.sleep(1)
    homepage.click_submit()
    time.sleep(4)

    print("Homepage has been tested successfully!!")

def test_ourcourses_page(driver):
    ourcourses = OurCoursesPage(driver)
    ourcourses.open_page("https://www.mindrisers.com.np/courses")
    driver.maximize_window()
    time.sleep(1)
    ourcourses.scroll_window()
    time.sleep(1)
    ourcourses.enter_searchfield("QA")
    time.sleep(2)
    ourcourses.click_searchbutton()
    time.sleep(4)