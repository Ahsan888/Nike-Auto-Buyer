import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import selenium.webdriver.chrome.options
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
# options.add_argument("C:\\Users\\Lenovo\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-user-media-security=true")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--disable-popup-blocking")
#options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=options)
action = ActionChains(driver)

a=1
time.sleep(3)
while a==1:
    try:# In place of nl kindly write the name or letters of your contry website
        driver.get("https://www.nike.com/nl/launch/t/sacai-vaporwaffle-sesame-blue-void")
        time.sleep(3)
        driver.maximize_window()

        driver.find_element_by_xpath("//*[contains(text(), 'EU 40')]").click()

        bag = driver.find_element_by_class_name("mt2-sm").click()
        bag = driver.find_element_by_class_name("mt2-sm").click()
        time.sleep(4)
        # In place of nl kindly write the name or letters of your contry website
        driver.get("https://www.nike.com/nl/en/checkout/tunnel")
        time.sleep(5)

        driver.find_element_by_id("qa-guest-checkout").click()
        time.sleep(5)
        fname = driver.find_element_by_id("firstName").click()
        #type First Name between comas
        pyautogui.typewrite("",interval=0.05)
        #type last Name between comas
        lastName = driver.find_element_by_id("lastName").click()
        pyautogui.typewrite("", interval=0.05)

        driver.find_element_by_id("addressSuggestionOptOut").click()

        ##type House number and street between comas
        street = driver.find_element_by_id("address1").click()
        pyautogui.typewrite("", interval=0.05)
        # Type post code between comas
        postalCode = driver.find_element_by_id("postalCode").click()
        pyautogui.typewrite("", interval=0.05)
        #type city between comas
        city = driver.find_element_by_id("city").click()
        pyautogui.typewrite("", interval=0.05)
        #type your email between comas
        email = driver.find_element_by_id("email").click()
        pyautogui.typewrite("", interval=0.05)
        #type your number between comas
        phoneNumber = driver.find_element_by_id("phoneNumber").click()
        pyautogui.typewrite("", interval=0.05)

        driver.find_element_by_class_name("js-next-step").click()
        time.sleep(5)


        continue1 = driver.find_element_by_class_name("js-next-step").click()

        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 500)")
        iframe = driver.find_element_by_xpath("//iframe[@title='Credit Card Form']")
        driver.switch_to.frame(iframe)
        
        #type your card number between comas
        card = driver.find_element_by_id("creditCardNumber").click()
        pyautogui.typewrite("", interval=0.05)
        #type card expiry date
        cardd = driver.find_element_by_id("expirationDate").click()
        pyautogui.typewrite("", interval=0.05)
        # type card cvv
        cardc = driver.find_element_by_id("cvNumber").click()
        pyautogui.typewrite("", interval=0.05)

        driver.switch_to.default_content()

        driver.find_element_by_class_name("continueOrderReviewBtn").click()
        time.sleep(5)

        try:
            final = driver.find_element_by_class_name("placeOrderBtn").click()
        except:
            final = driver.find_element_by_class_name("placeOrderBtn")
            driver.execute_script("arguments[0].click();", final)
        a=2
        driver.close()
        break
    except:
        pass
    try:
        #change nl to your country code
        driver.get("https://www.nike.com/nl/launch/t/sacai-vaporwaffle-dark-iris")
        time.sleep(3)
        driver.maximize_window()

        driver.find_element_by_xpath("//*[contains(text(), 'EU 40')]").click()

        bag = driver.find_element_by_class_name("mt2-sm").click()
        bag = driver.find_element_by_class_name("mt2-sm").click()
        time.sleep(4)
        #change nl to your country code
        driver.get("https://www.nike.com/nl/en/checkout/tunnel")
        time.sleep(5)

        driver.find_element_by_id("qa-guest-checkout").click()
        time.sleep(5)
        fname = driver.find_element_by_id("firstName").click()
        pyautogui.typewrite("", interval=0.05)

        lastName = driver.find_element_by_id("lastName").click()
        pyautogui.typewrite("", interval=0.05)

        driver.find_element_by_id("addressSuggestionOptOut").click()

        street = driver.find_element_by_id("address1").click()
        pyautogui.typewrite("", interval=0.05)

        postalCode = driver.find_element_by_id("postalCode").click()
        pyautogui.typewrite("", interval=0.05)

        city = driver.find_element_by_id("city").click()
        pyautogui.typewrite("", interval=0.05)

        email = driver.find_element_by_id("email").click()
        pyautogui.typewrite("", interval=0.05)

        phoneNumber = driver.find_element_by_id("phoneNumber").click()
        pyautogui.typewrite("", interval=0.05)

        driver.find_element_by_class_name("js-next-step").click()
        time.sleep(5)

        continue1 = driver.find_element_by_class_name("js-next-step").click()

        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 500)")
        iframe = driver.find_element_by_xpath("//iframe[@title='Credit Card Form']")
        driver.switch_to.frame(iframe)
        card = driver.find_element_by_id("creditCardNumber").click()
        pyautogui.typewrite("", interval=0.05)

        cardd = driver.find_element_by_id("expirationDate").click()
        pyautogui.typewrite("", interval=0.05)

        cardc = driver.find_element_by_id("cvNumber").click()
        pyautogui.typewrite("", interval=0.05)

        driver.switch_to.default_content()

        driver.find_element_by_class_name("continueOrderReviewBtn").click()
        time.sleep(5)

        try:
            final = driver.find_element_by_class_name("placeOrderBtn").click()
        except:
            final = driver.find_element_by_class_name("placeOrderBtn")
            driver.execute_script("arguments[0].click();", final)
        a = 2
        driver.close()
        break
    except:
        pass





