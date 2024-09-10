#import all the necessary selenium modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

#import all the pages
from pages.home_page import HomePage
from pages.ourcourses_page import OurCoursesPage
from pages.postplustwocourses_page import PostPlusTwoPage
from pages.placementpartner_page import PlacementPartnerPage
from pages.successfulstories_page import SuccessfulStoriesPage
from pages.Blogs_page import BlogsPage
from pages.contactus_page import ContactUsPage
from pages.AdmissionPage import AdmissionPage


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
    ourcourses.click_searchresult()
    time.sleep(3)

    print("Our Courses has been tested successfully!!")

def test_postplustwo_page(driver):
    postplustwo = PostPlusTwoPage(driver)
    postplustwo.open_page("https://www.mindrisers.com.np/after+2-courses")
    driver.maximize_window()
    time.sleep(1)
    postplustwo.scroll_window()
    time.sleep(2)
    postplustwo.open_card()
    time.sleep(2)

    
    print("Our Courses has been tested successfully!!")


def test_placementpartner(driver):
    placementpartner = PlacementPartnerPage(driver)
    placementpartner.open_page("https://www.mindrisers.com.np/placement-partner")
    driver.maximize_window()
    time.sleep(1)
    placementpartner.scroll_window()
    time.sleep(2)

    print("Placement Partner Page has been tested successfully!!")


def test_successfulstories(driver):
    successfulstories = SuccessfulStoriesPage(driver)
    successfulstories.open_page("https://www.mindrisers.com.np/success-gallery")
    driver.maximize_window()
    time.sleep(1)
    successfulstories.scroll_window()
    time.sleep(2)

    print("Successful Stories Page has been tested successfully!!")


def test_blogs(driver):
    blogs = BlogsPage(driver)
    blogs.open_page("https://www.mindrisers.com.np/blogs")
    driver.maximize_window()
    time.sleep(1)
    blogs.scroll_window()
    time.sleep(1)

    print("Blogs Page has been tested successfully!!")


def test_contactus(driver):
    contactus = ContactUsPage(driver)
    contactus.open_page("https://www.mindrisers.com.np/contact-us")
    driver.maximize_window()
    time.sleep(1)
    contactus.scroll_window()
    time.sleep(2)

    print("Contact Us Page has been tested successfully!!")


def test_admission(driver):
    admission = AdmissionPage(driver)
    admission.open_page("https://www.mindrisers.com.np/online-admission")
    driver.maximize_window()
    time.sleep(1)
    admission.scroll_window()
    time.sleep(1)

    print("Admission Page has been tested successfully!!")