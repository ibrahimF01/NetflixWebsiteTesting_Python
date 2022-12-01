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
        self.accountVerify3_CSS = "div[data-uia='contextRowDone']"
        self.accountVerify4_CSS = "div[data-uia='contextRowPaperWork']"
        self.passwordInput_ID = "id_password"
        self.accountVerify5_CSS = "label[for='cb_emailPreference']"
        self.binaryInput_CSS = "div[class='ui-binary-input']"
        self.continueButton2_CSS = "button[data-uia='cta-registration']"
        self.accountVerify6_XPATH = "//h1[text()='Planınızı seçin.']"
        self.accountVerify7_XPATH = "//span[starts-with(text(),'Taahhüt yok')]"
        self.accountVerify8_XPATH = "//span[starts-with(text(),'Tek ve düşük bir ücretle')]"
        self.accountVerify9_XPATH = "//span[starts-with(text(),'Tüm cihazlarınızda')]"
        self.continueButton3_CSS = "button[data-uia='continue-button']"
        self.accountVerify10_XPATH = "//h1[starts-with(text(),'Kendinize uygun')]"
        self.accountVerify11_XPATH = "//span[starts-with(text(),'Canınız neyi isterse')]"
        self.accountVerify12_XPATH = "//span[starts-with(text(),'Sadece sizin için')]"
        self.accountVerify13_XPATH = "//span[starts-with(text(),'Planınızı istediğiniz zaman')]"
        self.continueButton4_CSS = "button[data-uia='cta-plan-selection']"
        self.accountVerify14_XPATH = "//h1[starts-with(text(),'Tercih ettiğiniz ödeme')]"
        self.accountVerify15_XPATH = "//div[starts-with(text(),'Ödeme yönteminiz')]"
        self.accountVerify16_XPATH = "//div[starts-with(text(),'Endişelenmeyin')]"
        self.accountVerify17_XPATH = "//div[starts-with(text(),'İstediğiniz zaman')]"
        self.creditCardButton_ID = "creditOrDebitCardDisplayStringId"
        self.accountVerify18_XPATH = "//h1[starts-with(text(),'Ödemenizi ayarlayın')]"
        self.firstNameInput_ID = "id_firstName"
        self.lastNameInput_ID = "id_lastName"
        self.creditCardNumberInput_ID = "id_creditCardNumber"
        self.creditExpirationMonthInput_ID = "id_creditExpirationMonth"
        self.creditCardSecurityCodeInput_ID = "id_creditCardSecurityCode"
        self.hasAcceptedInput_XPATH = "//span[text()='Kabul ediyorum.']"
        self.continueButton5_CSS = "button[data-uia='action-submit-payment']"

        self.homepageVerify1_CSS = "div[class='text-0']"
        self.homepageVerify2_CSS = "div[class='text-1']"
        self.homepageVerify3_XPATH = "//h1[starts-with(text(),'Çevrimdışı izlemek için')]"
        self.homepageVerify4_XPATH = "//h2[starts-with(text(),'En sevdiğiniz içerikleri')]"
        self.homepageVerify5_XPATH = "//h1[starts-with(text(),'Sıkça Sorulan')]"
        self.faqQuestionButton1_XPATH = "(//button[@class='faq-question'])[1]"
        self.faqQuestionButton2_XPATH = "(//button[@class='faq-question'])[2]"
        self.faqQuestionButton3_XPATH = "(//button[@class='faq-question'])[3]"
        self.faqQuestionButton4_XPATH = "(//button[@class='faq-question'])[4]"
        self.faqQuestionButton5_XPATH = "(//button[@class='faq-question'])[5]"
        self.faqQuestionButton6_XPATH = "(//button[@class='faq-question'])[6]"
        self.faqAnswerVerify1_XPATH = "(//div[starts-with(@class,'faq-answer')]/span)[1]"
        self.faqAnswerVerify2_XPATH = "(//div[starts-with(@class,'faq-answer')]/span)[2]"
        self.faqAnswerVerify3_XPATH = "(//div[starts-with(@class,'faq-answer')]/span)[3]"
        self.faqAnswerVerify4_XPATH = "(//div[starts-with(@class,'faq-answer')]/span)[4]"
        self.faqAnswerVerify5_XPATH = "(//div[starts-with(@class,'faq-answer')]/span)[5]"
        self.faqAnswerVerify6_XPATH = "(//div[starts-with(@class,'faq-answer')]/span)[6]"

        self.SSSButton_XPATH = "//span[starts-with(text(),'SSS')]"
        self.SSSVerify1_CSS = "h1[class='kb-title']"
        self.SSSVerify2_XPATH = "//h2[text()='Diziler ve Filmler']"
        self.SSSVerify3_XPATH = "//h2[text()='Desteklenen Cihazlar']"
        self.SSSVerify4_XPATH = "//h2[text()='Planlar ve Ücretler']"
        self.SSSVerify5_XPATH = "//h2[text()='Başlayın']"
        self.linkButton1_XPATH = "//button[text()='Evet']"
        self.textAreaInput_CSS = "textarea[class='form-control']"
        self.sendButton_CSS = "button[class$='btn-primary']"
        self.phoneContactButton_ID = "phone-contact"
        self.SSSVerify6_CSS = "div[class$='title-in-app']"
        self.closeButton1_CSS = "button[class$='popover-close']"
        self.chatContactButton_ID = "startChatTrigger"
        self.SSSVerify7_XPATH = "//h1[starts-with(text(),'Sohbete başlamadan')]"
        self.closeButton2_CSS = "div[class^='chat-avatar']+button[class^='chat-end-button']"
        self.homePageButton_CSS = "a[title='Netflix']"

        self.investorsButton_CSS = "a[placeholder='footer_responsive_link_relations']"
        self.investorsTitLink1_XPATH = "(//a[@class='sf-with-ul'])[1]"
        self.investorsTitLink2_XPATH = "(//a[@class='sf-with-ul'])[2]"
        self.investorsTitLink3_XPATH = "(//a[@class='sf-with-ul'])[3]"
        self.investorsTitLink4_XPATH = "(//a[@class='sf-with-ul'])[4]"
        self.investorsTitLink5_XPATH = "(//a[@class='sf-with-ul'])[5]"
        self.investorsTitLink6_XPATH = "(//a[@class='sf-with-ul'])[6]"
        self.investorsVerify1_CSS = "div[class='module-slider_title']>h1"
        self.investorsVerify2J_CSS = "h1[class='module_title']"
        self.kullanimKosButton_CSS = "a[placeholder='footer_responsive_link_terms']"




        self.oturumAcBtn_CSS = "a[data-uia='header-login-link']"
        self.userLogin_ID = "id_userLoginId"
        self.userPassword_ID = "id_password"
        self.oturumAcBtn2_CSS = "button[data-uia='login-submit-button']"
        self.loginNegativeVerifyMessage_CSS = "div[data-uia='text']"
        self.loginEmptyVerifyMessage1_CSS = "div[data-uia='login-field+error']"
        self.loginEmptyVerifyMessage2_CSS = "div[data-uia='password-field+error']"
        self.yardimMerkeziBtn_XPATH = "//span[text()='Yardım Merkezi']"
        self.yardimMerkeziVerify_CSS = "div[class='logo-wrapper'] a"
        self.popularTopicsBtn1_XPATH = "(//a[@rel='noreferrer'])[1]"
        self.popularTopicsBtn2_XPATH = "(//a[@rel='noreferrer'])[2]"
        self.popularTopicsBtn3_XPATH = "(//a[@rel='noreferrer'])[3]"
        self.popularTopicsBtnsVerify_CSS = "h1[class='kb-title']"
        self.platformVerify1_XPATH = "(//a[@role='button'])[1]"
        self.platformVerify2_XPATH = "(//a[@role='button'])[2]"
        self.platformVerify3_XPATH = "(//a[@role='button'])[3]"
        self.platformVerify4_XPATH = "(//a[@role='button'])[4]"
        self.platformVerify5_XPATH = "(//a[@role='button'])[5]"
        self.netflixPlansChart1_XPATH = "(//div[@class='c-wrapper']//h3)[1]"
        self.netflixPlansChart2_XPATH = "(//div[@class='c-wrapper']//p)[3]"
        self.netflixPlansChart3_XPATH = "(//div[@class='c-wrapper']//p)[4]"
        self.netflixPlansChart4_XPATH = "(//div[@class='c-wrapper']//p)[5]"
        self.isImkanlariBtn_XPATH = "//span[text()='İş İmkanları']"
        self.isImkanlariVerify_CSS = "h1[spacing='[object Object]']"
        self.isImkanlariTitleVerify1_XPATH = "(//h2[@spacing='[object Object]'])[1]"
        self.isImkanlariTitleMsgVerify1_XPATH = "(//p[@spacing='[object Object]'])[1]"
        self.isImkanlariTitleVerify2_XPATH = "(//h2[@spacing='[object Object]'])[2]"
        self.isImkanlariTitleMsgVerify2_XPATH = "(//p[@spacing='[object Object]'])[2]"
        self.gizlilikBtn_XPATH = "//span[text()='Gizlilik']"
        self.gizlilikVerify_XPATH = "(//div[@class='c-wrapper']//p)[1]"
        self.hizTestiBtn_XPATH = "//span[text()='Hız Testi']"
        self.hizTestiDetails_ID = "show-more-details-link"
        self.hizTestiSpeedValue_ID = "speed-value"
        self.orta3Element = "div[data-uia-nmhp='watchOnDevice']"
        self.orta1Element_CSS = "div[data-uia-nmhp='watchOnTv']"



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

    def get_accountVerify2_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.accountVerify2_CSS)

    def get_accountVerify3_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.accountVerify3_CSS)

    def get_accountVerify4_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.accountVerify4_CSS)

    def get_passwordInput_ID(self):
        return self.driver.find_element(By.ID, self.passwordInput_ID)

    def get_accountVerify5_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.accountVerify5_CSS)

    def get_binaryInput_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.binaryInput_CSS)

    def get_continueButton2_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.continueButton2_CSS)

    def get_accountVerify6_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify6_XPATH)

    def get_accountVerify7_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify7_XPATH)

    def get_accountVerify8_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify8_XPATH)

    def get_accountVerify9_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify9_XPATH)

    def get_continueButton3_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.continueButton3_CSS)

    def get_accountVerify10_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify10_XPATH)

    def get_accountVerify11_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify11_XPATH)

    def get_accountVerify12_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify12_XPATH)

    def get_accountVerify13_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify13_XPATH)

    def get_continueButton4_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.continueButton4_CSS)

    def get_accountVerify14_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify14_XPATH)

    def get_accountVerify15_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify15_XPATH)

    def get_accountVerify16_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify16_XPATH)

    def get_accountVerify17_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify17_XPATH)

    def get_creditCardButton_ID(self):
        return self.driver.find_element(By.ID, self.creditCardButton_ID)

    def get_accountVerify18_XPATH(self):
        return self.driver.find_element(By.XPATH, self.accountVerify18_XPATH)

    def get_firstNameInput_ID(self):
        return self.driver.find_element(By.ID, self.firstNameInput_ID)

    def get_lastNameInput_ID(self):
        return self.driver.find_element(By.ID, self.lastNameInput_ID)

    def get_creditCardNumberInput_ID(self):
        return self.driver.find_element(By.ID, self.creditCardNumberInput_ID)

    def get_creditExpirationMonthInput_ID(self):
        return self.driver.find_element(By.ID, self.creditExpirationMonthInput_ID)

    def get_creditCardSecurityCodeInput_ID(self):
        return self.driver.find_element(By.ID, self.creditCardSecurityCodeInput_ID)

    def get_hasAcceptedInput_XPATH(self):
        return self.driver.find_element(By.XPATH, self.hasAcceptedInput_XPATH)

    def get_continueButton5_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.continueButton5_CSS)
    def get_homepageVerify1_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.homepageVerify1_CSS)
    def get_homepageVerify2_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.homepageVerify2_CSS)
    def get_homepageVerify3_XPATH(self):
        return self.driver.find_element(By.XPATH, self.homepageVerify3_XPATH)
    def get_homepageVerify4_XPATH(self):
        return self.driver.find_element(By.XPATH, self.homepageVerify4_XPATH)
    def get_homepageVerify5_XPATH(self):
        return self.driver.find_element(By.XPATH, self.homepageVerify5_XPATH)
    def get_faqQuestionButton1_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqQuestionButton1_XPATH)
    def get_faqQuestionButton2_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqQuestionButton2_XPATH)
    def get_faqQuestionButton3_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqQuestionButton3_XPATH)
    def get_faqQuestionButton4_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqQuestionButton4_XPATH)
    def get_faqQuestionButton5_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqQuestionButton5_XPATH)
    def get_faqQuestionButton6_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqQuestionButton6_XPATH)
    def get_faqAnswerVerify1_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqAnswerVerify1_XPATH)
    def get_faqAnswerVerify2_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqAnswerVerify2_XPATH)
    def get_faqAnswerVerify3_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqAnswerVerify3_XPATH)
    def get_faqAnswerVerify4_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqAnswerVerify4_XPATH)
    def get_faqAnswerVerify5_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqAnswerVerify5_XPATH)
    def get_faqAnswerVerify6_XPATH(self):
        return self.driver.find_element(By.XPATH, self.faqAnswerVerify6_XPATH)
    def get_SSSButton_XPATH(self):
        return self.driver.find_element(By.XPATH, self.SSSButton_XPATH)
    def get_SSSVerify1_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.SSSVerify1_CSS)
    def get_SSSVerify2_XPATH(self):
        return self.driver.find_element(By.XPATH, self.SSSVerify2_XPATH)
    def get_SSSVerify3_XPATH(self):
        return self.driver.find_element(By.XPATH, self.SSSVerify3_XPATH)
    def get_SSSVerify4_XPATH(self):
        return self.driver.find_element(By.XPATH, self.SSSVerify4_XPATH)
    def get_SSSVerify5_XPATH(self):
        return self.driver.find_element(By.XPATH, self.SSSVerify5_XPATH)
    def get_linkButton1_XPATH(self):
        return self.driver.find_element(By.XPATH, self.linkButton1_XPATH)
    def get_textAreaInput_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.textAreaInput_CSS)
    def get_sendButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.sendButton_CSS)
    def get_phoneContactButton_ID(self):
        return self.driver.find_element(By.ID, self.phoneContactButton_ID)
    def get_SSSVerify6_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.SSSVerify6_CSS)
    def get_closeButton1_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.closeButton1_CSS)
    def get_chatContactButton_ID(self):
        return self.driver.find_element(By.ID, self.chatContactButton_ID)
    def get_SSSVerify7_XPATH(self):
        return self.driver.find_element(By.XPATH, self.SSSVerify7_XPATH)
    def get_closeButton2_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.closeButton2_CSS)
    def get_homePageButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.homePageButton_CSS)
    def get_investorsButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.investorsButton_CSS)
    def get_investorsVerify1_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.investorsVerify1_CSS)
    def get_investorsTitLink1_XPATH(self):
        return self.driver.find_element(By.XPATH, self.investorsTitLink1_XPATH)
    def get_investorsTitLink2_XPATH(self):
        return self.driver.find_element(By.XPATH, self.investorsTitLink2_XPATH)
    def get_investorsTitLink3_XPATH(self):
        return self.driver.find_element(By.XPATH, self.investorsTitLink3_XPATH)
    def get_investorsTitLink4_XPATH(self):
        return self.driver.find_element(By.XPATH, self.investorsTitLink4_XPATH)
    def get_investorsTitLink5_XPATH(self):
        return self.driver.find_element(By.XPATH, self.investorsTitLink5_XPATH)
    def get_investorsTitLink6_XPATH(self):
        return self.driver.find_element(By.XPATH, self.investorsTitLink6_XPATH)
    def get_investorsVerify2J_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.investorsVerify2J_CSS)
    def get_kullanimKosButton_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.kullanimKosButton_CSS)



    def get_oturumAcBtn_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.oturumAcBtn_CSS)
    def get_userLogin_ID(self):
        return self.driver.find_element(By.ID, self.userLogin_ID)
    def get_userPassword_ID(self):
        return self.driver.find_element(By.ID, self.userPassword_ID)
    def get_oturumAcBtn2_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.oturumAcBtn2_CSS)
    def get_loginNegativeVerifyMessage_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.loginNegativeVerifyMessage_CSS)
    def get_loginEmptyVerifyMessage1_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.loginEmptyVerifyMessage1_CSS)
    def get_loginEmptyVerifyMessage2_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.loginEmptyVerifyMessage2_CSS)
    def get_yardimMerkeziBtn_XPATH(self):
        return self.driver.find_element(By.XPATH, self.yardimMerkeziBtn_XPATH)
    def get_yardimMerkeziVerify_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.yardimMerkeziVerify_CSS)
    def get_popularTopicsBtn1_XPATH(self):
        return self.driver.find_element(By.XPATH, self.popularTopicsBtn1_XPATH)
    def get_popularTopicsBtn2_XPATH(self):
        return self.driver.find_element(By.XPATH, self.popularTopicsBtn2_XPATH)
    def get_popularTopicsBtn3_XPATH(self):
        return self.driver.find_element(By.XPATH, self.popularTopicsBtn3_XPATH)
    def get_popularTopicsBtnsVerify_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.popularTopicsBtnsVerify_CSS)
    def get_platformVerify1_XPATH(self):
        return self.driver.find_element(By.XPATH, self.platformVerify1_XPATH)
    def get_platformVerify2_XPATH(self):
        return self.driver.find_element(By.XPATH, self.platformVerify2_XPATH)
    def get_platformVerify3_XPATH(self):
        return self.driver.find_element(By.XPATH, self.platformVerify3_XPATH)
    def get_platformVerify4_XPATH(self):
        return self.driver.find_element(By.XPATH, self.platformVerify4_XPATH)
    def get_platformVerify5_XPATH(self):
        return self.driver.find_element(By.XPATH, self.platformVerify5_XPATH)
    def get_netflixPlansChart1_XPATH(self):
        return self.driver.find_element(By.XPATH, self.netflixPlansChart1_XPATH)
    def get_netflixPlansChart2_XPATH(self):
        return self.driver.find_element(By.XPATH, self.netflixPlansChart2_XPATH)
    def get_netflixPlansChart3_XPATH(self):
        return self.driver.find_element(By.XPATH, self.netflixPlansChart3_XPATH)
    def get_netflixPlansChart4_XPATH(self):
        return self.driver.find_element(By.XPATH, self.netflixPlansChart4_XPATH)
    def get_isImkanlariBtn_XPATH(self):
        return self.driver.find_element(By.XPATH, self.isImkanlariBtn_XPATH)
    def get_isImkanlariVerify_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.isImkanlariVerify_CSS)
    def get_isImkanlariTitleVerify1_XPATH(self):
        return self.driver.find_element(By.XPATH, self.isImkanlariTitleVerify1_XPATH)
    def get_isImkanlariTitleVerify2_XPATH(self):
        return self.driver.find_element(By.XPATH, self.isImkanlariTitleVerify2_XPATH)
    def get_isImkanlariTitleMsgVerify1_XPATH(self):
        return self.driver.find_element(By.XPATH, self.isImkanlariTitleMsgVerify1_XPATH)
    def get_isImkanlariTitleMsgVerify2_XPATH(self):
        return self.driver.find_element(By.XPATH, self.isImkanlariTitleMsgVerify2_XPATH)
    def get_gizlilikBtn_XPATH(self):
        return self.driver.find_element(By.XPATH, self.gizlilikBtn_XPATH)
    def get_gizlilikVerify_XPATH(self):
        return self.driver.find_element(By.XPATH, self.gizlilikVerify_XPATH)
    def get_hizTestiBtn_XPATH(self):
        return self.driver.find_element(By.XPATH, self.hizTestiBtn_XPATH)
    def get_hizTestiDetails_ID(self):
        return self.driver.find_element(By.ID, self.hizTestiDetails_ID)
    def get_hizTestiSpeedValue_ID(self):
        return self.driver.find_element(By.ID, self.hizTestiSpeedValue_ID)
    def get_orta3(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.orta3Element)
    def get_orta1Element_CSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.orta1Element_CSS)

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
            case "binaryInput_CSS": self.myElement = self.get_binaryInput_CSS()
            case "continueButton2_CSS": self.myElement = self.get_continueButton2_CSS()
            case "continueButton3_CSS": self.myElement = self.get_continueButton3_CSS()
            case "continueButton4_CSS": self.myElement = self.get_continueButton4_CSS()
            case "creditCardButton_ID": self.myElement = self.get_creditCardButton_ID()
            case "hasAcceptedInput_XPATH": self.myElement = self.get_hasAcceptedInput_XPATH()
            case "continueButton5_CSS": self.myElement = self.get_continueButton5_CSS()
            case "continueButton5_CSS": self.myElement = self.get_continueButton5_CSS()
            case "passwordInput_ID": self.myElement = self.get_passwordInput_ID()
            case "faqQuestionButton1_XPATH": self.myElement = self.get_faqQuestionButton1_XPATH()
            case "faqQuestionButton2_XPATH": self.myElement = self.get_faqQuestionButton2_XPATH()
            case "faqQuestionButton3_XPATH": self.myElement = self.get_faqQuestionButton3_XPATH()
            case "faqQuestionButton4_XPATH": self.myElement = self.get_faqQuestionButton4_XPATH()
            case "faqQuestionButton5_XPATH": self.myElement = self.get_faqQuestionButton5_XPATH()
            case "faqQuestionButton6_XPATH": self.myElement = self.get_faqQuestionButton6_XPATH()
            case "SSSButton_XPATH": self.myElement = self.get_SSSButton_XPATH()
            case "linkButton1_XPATH": self.myElement = self.get_linkButton1_XPATH()
            case "sendButton_CSS": self.myElement = self.get_sendButton_CSS()
            case "phoneContactButton_ID": self.myElement = self.get_phoneContactButton_ID()
            case "closeButton1_CSS": self.myElement = self.get_closeButton1_CSS()
            case "chatContactButton_ID": self.myElement = self.get_chatContactButton_ID()
            case "closeButton2_CSS": self.myElement = self.get_closeButton2_CSS()
            case "homePageButton_CSS": self.myElement = self.get_homePageButton_CSS()
            case "investorsButton_CSS": self.myElement = self.get_investorsButton_CSS()
            case "investorsTitLink1_XPATH": self.myElement = self.get_investorsTitLink1_XPATH()
            case "investorsTitLink2_XPATH": self.myElement = self.get_investorsTitLink2_XPATH()
            case "investorsTitLink3_XPATH": self.myElement = self.get_investorsTitLink3_XPATH()
            case "investorsTitLink4_XPATH": self.myElement = self.get_investorsTitLink4_XPATH()
            case "investorsTitLink5_XPATH": self.myElement = self.get_investorsTitLink5_XPATH()
            case "investorsTitLink6_XPATH": self.myElement = self.get_investorsTitLink6_XPATH()
            case "kullanimKosButton_CSS": self.myElement = self.get_kullanimKosButton_CSS()

            case "oturumAcBtn_CSS": self.myElement = self.get_oturumAcBtn_CSS()
            case "oturumAcBtn2_CSS": self.myElement = self.get_oturumAcBtn2_CSS()
            case "yardimMerkeziBtn_XPATH": self.myElement = self.get_yardimMerkeziBtn_XPATH()
            case "popularTopicsBtn1_XPATH": self.myElement = self.get_popularTopicsBtn1_XPATH()
            case "popularTopicsBtn2_XPATH": self.myElement = self.get_popularTopicsBtn2_XPATH()
            case "popularTopicsBtn3_XPATH": self.myElement = self.get_popularTopicsBtn3_XPATH()
            case "isImkanlariBtn_XPATH": self.myElement = self.get_isImkanlariBtn_XPATH()
            case "gizlilikBtn_XPATH": self.myElement = self.get_gizlilikBtn_XPATH()
            case "hizTestiBtn_XPATH": self.myElement = self.get_hizTestiBtn_XPATH()
            case "hizTestiDetails_ID": self.myElement = self.get_hizTestiDetails_ID()
        self.scrollToElementMid(self.myElement)
        EC.element_to_be_clickable(self.myElement)
        self.myElement.click()

    def findAndSend(self, strElement, strText):
        match strElement:
            case "emailInput_ID": self.myElement = self.get_emailInput_ID()
            case "passwordInput_ID": self.myElement = self.get_passwordInput_ID()
            case "firstNameInput_ID": self.myElement = self.get_firstNameInput_ID()
            case "lastNameInput_ID": self.myElement = self.get_lastNameInput_ID()
            case "creditCardNumberInput_ID": self.myElement = self.get_creditCardNumberInput_ID()
            case "creditExpirationMonthInput_ID": self.myElement = self.get_creditExpirationMonthInput_ID()
            case "creditCardSecurityCodeInput_ID": self.myElement = self.get_creditCardSecurityCodeInput_ID()
            case "textAreaInput_CSS": self.myElement = self.get_textAreaInput_CSS()

            case "userLogin_ID": self.myElement = self.get_userLogin_ID()
            case "userPassword_ID": self.myElement = self.get_userPassword_ID()
        self.scrollToElementMid(self.myElement)
        EC.visibility_of(self.myElement)
        self.myElement.send_keys(strText)

    def findAndVerify(self, strElement, textElement):
        match strElement:
            case "heroTitle_CSS": self.myElement = self.get_heroTitle_CSS()
            case "accountVerify1_CSS": self.myElement = self.get_accountVerify1_CSS()
            case "accountVerify2_CSS": self.myElement = self.get_accountVerify2_CSS()
            case "accountVerify3_CSS": self.myElement = self.get_accountVerify3_CSS()
            case "accountVerify4_CSS": self.myElement = self.get_accountVerify4_CSS()
            case "accountVerify5_CSS": self.myElement = self.get_accountVerify5_CSS()
            case "accountVerify6_XPATH": self.myElement = self.get_accountVerify6_XPATH()
            case "accountVerify7_XPATH": self.myElement = self.get_accountVerify7_XPATH()
            case "accountVerify8_XPATH": self.myElement = self.get_accountVerify8_XPATH()
            case "accountVerify9_XPATH": self.myElement = self.get_accountVerify9_XPATH()
            case "accountVerify10_XPATH": self.myElement = self.get_accountVerify10_XPATH()
            case "accountVerify11_XPATH": self.myElement = self.get_accountVerify11_XPATH()
            case "accountVerify12_XPATH": self.myElement = self.get_accountVerify12_XPATH()
            case "accountVerify13_XPATH": self.myElement = self.get_accountVerify13_XPATH()
            case "accountVerify14_XPATH": self.myElement = self.get_accountVerify14_XPATH()
            case "accountVerify15_XPATH": self.myElement = self.get_accountVerify15_XPATH()
            case "accountVerify16_XPATH": self.myElement = self.get_accountVerify16_XPATH()
            case "accountVerify17_XPATH": self.myElement = self.get_accountVerify17_XPATH()
            case "accountVerify18_XPATH": self.myElement = self.get_accountVerify18_XPATH()
            case "homepageVerify1_CSS": self.myElement = self.get_homepageVerify1_CSS()
            case "homepageVerify2_CSS": self.myElement = self.get_homepageVerify2_CSS()
            case "homepageVerify3_XPATH": self.myElement = self.get_homepageVerify3_XPATH()
            case "homepageVerify4_XPATH": self.myElement = self.get_homepageVerify4_XPATH()
            case "homepageVerify5_XPATH": self.myElement = self.get_homepageVerify5_XPATH()
            case "faqAnswerVerify1_XPATH": self.myElement = self.get_faqAnswerVerify1_XPATH()
            case "faqAnswerVerify2_XPATH": self.myElement = self.get_faqAnswerVerify2_XPATH()
            case "faqAnswerVerify3_XPATH": self.myElement = self.get_faqAnswerVerify3_XPATH()
            case "faqAnswerVerify4_XPATH": self.myElement = self.get_faqAnswerVerify4_XPATH()
            case "faqAnswerVerify5_XPATH": self.myElement = self.get_faqAnswerVerify5_XPATH()
            case "faqAnswerVerify6_XPATH": self.myElement = self.get_faqAnswerVerify6_XPATH()
            case "SSSVerify1_CSS": self.myElement = self.get_SSSVerify1_CSS()
            case "SSSVerify2_XPATH": self.myElement = self.get_SSSVerify2_XPATH()
            case "SSSVerify3_XPATH": self.myElement = self.get_SSSVerify3_XPATH()
            case "SSSVerify4_XPATH": self.myElement = self.get_SSSVerify4_XPATH()
            case "SSSVerify5_XPATH": self.myElement = self.get_SSSVerify5_XPATH()
            case "SSSVerify6_CSS": self.myElement = self.get_SSSVerify6_CSS()
            case "SSSVerify7_XPATH": self.myElement = self.get_SSSVerify7_XPATH()
            case "investorsVerify1_CSS": self.myElement = self.get_investorsVerify1_CSS()
            case "investorsVerify2J_CSS": self.myElement = self.get_investorsVerify2J_CSS()

            case "loginNegativeVerifyMessage_CSS": self.myElement = self.get_loginNegativeVerifyMessage_CSS()
            case "loginEmptyVerifyMessage1_CSS": self.myElement = self.get_loginEmptyVerifyMessage1_CSS()
            case "loginEmptyVerifyMessage2_CSS": self.myElement = self.get_loginEmptyVerifyMessage2_CSS()
            case "yardimMerkeziVerify_CSS": self.myElement = self.get_yardimMerkeziVerify_CSS()
            case "popularTopicsBtnsVerify_CSS": self.myElement = self.get_popularTopicsBtnsVerify_CSS()
            case "platformVerify1_XPATH": self.myElement = self.get_platformVerify1_XPATH()
            case "platformVerify2_XPATH": self.myElement = self.get_platformVerify2_XPATH()
            case "platformVerify3_XPATH": self.myElement = self.get_platformVerify3_XPATH()
            case "platformVerify4_XPATH": self.myElement = self.get_platformVerify4_XPATH()
            case "platformVerify5_XPATH": self.myElement = self.get_platformVerify5_XPATH()
            case "netflixPlansChart1_XPATH": self.myElement = self.get_netflixPlansChart1_XPATH()
            case "netflixPlansChart2_XPATH": self.myElement = self.get_netflixPlansChart2_XPATH()
            case "netflixPlansChart3_XPATH": self.myElement = self.get_netflixPlansChart3_XPATH()
            case "netflixPlansChart4_XPATH": self.myElement = self.get_netflixPlansChart4_XPATH()
            case "isImkanlariVerify_CSS": self.myElement = self.get_isImkanlariVerify_CSS()
            case "isImkanlariTitleVerify1_XPATH": self.myElement = self.get_isImkanlariTitleVerify1_XPATH()
            case "isImkanlariTitleVerify2_XPATH": self.myElement = self.get_isImkanlariTitleVerify2_XPATH()
            case "isImkanlariTitleMsgVerify1_XPATH": self.myElement = self.get_isImkanlariTitleMsgVerify1_XPATH()
            case "isImkanlariTitleMsgVerify2_XPATH": self.myElement = self.get_isImkanlariTitleMsgVerify2_XPATH()
            case "gizlilikVerify_XPATH": self.myElement = self.get_gizlilikVerify_XPATH()
            case "orta3Element": self.myElement = self.get_orta3()
            case "orta1Element_CSS": self.myElement = self.get_orta1Element_CSS()
        self.scrollToElementMid(self.myElement)
        EC.visibility_of(self.myElement)
        assert textElement in self.myElement.text
        print("Verified text: "+self.myElement.text)

    @staticmethod
    def get_base_url():
        return base_url
