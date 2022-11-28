from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


base_url = "https://www.netflix.com/tr/"

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.acceptButton_CSS = "button[data-uia='cookie-disclosure-button-accept']"
        self.heroTitle_CSS = "h1[data-uia='hero-title']"
        self.emailInput_ID = "id_email_hero_fuji"
        self.startButton_CSS = "button[data-uia='our-story-cta-hero_fuji']"
        self.accountVerify1_CSS = "h1[data-uia='stepTitle']"
        self.continueButton_CSS = "button[data-uia='cta-continue-registration']"
        self.accountVerify2_CSS = "h1[data-uia='stepTitle']"


    def get_acceptButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.acceptButton_CSS)
    def get_heroTitle_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.heroTitle_CSS)
    def get_emailInput_ID(self):
        return self.driver.find_element(By.ID, self.emailInput_ID)
    def get_startButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.startButton_CSS)
    def get_accountVerify1_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.accountVerify1_CSS)
    def get_continueButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.continueButton_CSS)

    def scrollToElementMid(self, element):
        scrollElementIntoMiddle = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
        "var elementTop = arguments[0].getBoundingClientRect().top;"
        "window.scrollBy(0, elementTop-(viewPortHeight/2));"
        self.driver.execute_script(scrollElementIntoMiddle, element)

    def scrollToElement(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def moveToElement(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scrollHeight(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def findAndClick(self, strElement):
        match strElement:
            case "acceptButton_CSS": self.myElement = self.get_acceptButton_CSS()
            case "startButton_CSS": self.myElement = self.get_startButton_CSS()
            case "continueButton_CSS": self.myElement = self.get_continueButton_CSS()
        self.scrollToElementMid(self.myElement)
        EC.element_to_be_clickable(self.myElement)
        self.myElement.click()

    def findAndSend(self, strElement, strText):
        match strElement:
            case "emailInput_ID": self.myElement = self.get_emailInput_ID()
        self.scrollToElementMid(self.myElement)
        EC.visibility_of(self.myElement)
        self.myElement.send_keys(strText)

    def findAndVerify(self, strElement, textElement):
        match strElement:
            case "heroTitle_CSS": self.myElement = self.get_heroTitle_CSS()
            case "accountVerify1_CSS": self.myElement = self.get_accountVerify1_CSS()
        self.scrollToElementMid(self.myElement)
        EC.visibility_of(self.myElement)
        assert textElement in self.myElement.text

    @staticmethod
    def get_base_url():
        return base_url
