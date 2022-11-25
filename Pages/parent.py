from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)


def scrollToElementMid(element):
    scrollElementIntoMiddle = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
    "var elementTop = arguments[0].getBoundingClientRect().top;"
    "window.scrollBy(0, elementTop-(viewPortHeight/2));"
    driver.execute_script(scrollElementIntoMiddle, element)

def scrollToElement(element):
   driver.execute_script("arguments[0].scrollIntoView();", element)

def moveToElement(element):
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

def scrollHeight():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")