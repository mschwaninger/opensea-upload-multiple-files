from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# extension_path='C:\Users\mschwaninger\AppData\Local\Google\Chrome\User Data\Default\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn\10.2.0_0.crx'

def uploadFiles(startItemId, count, mnemonicString, walletPwd):
    extension_path='./10.2.0_0.crx'
    opt = webdriver.ChromeOptions()
    opt.add_extension(extension_path)

    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=opt)
    #driver = webdriver.Chrome(executable_path='./chromedriver')

    wait = WebDriverWait(driver, 60)
    url = 'https://opensea.io/asset/create'
    collName = 'Capricorn pixel art'
    driver.get(url)
    time.sleep(0.5)
    signIntoMeta(driver, wait, mnemonicString, walletPwd)

def signIntoMeta(driver, wait, mnemonicString, walletPwd): 
    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[0])
    time.sleep(0.5)
    button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/button')
    button.click()
    print('meta clicked')
    time.sleep(1)
    button = driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')
    button.click()
    print('import key clicked')
    button = driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]')
    button.click()
    print('Improve button clicked')
    time.sleep(1)

    mnemonicInput = driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input')
    mnemonicInput.send_keys(mnemonicString)
    pwd1Input = driver.find_element_by_xpath('//*[@id="password"]')
    pwd1Input.send_keys(walletPwd)
    pwd2Input = driver.find_element_by_xpath('//*[@id="confirm-password"]')
    pwd2Input.send_keys(walletPwd)

    checkbox = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div')
    checkbox.click()

    submit = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/button')
    submit.click()
    time.sleep(1.5)    

if __name__ == '__main__':
    uploadFiles(251, 4750,
                mnemonicString='0', 
                walletPwd='0'
                )

# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://opensea.io/")
# explore_bt = driver.find_element_by_class_name("gMiESj").click()
# time.sleep(1)
# input_input_min = driver.find_element(By.XPATH, '//input[@data-testid="Input"]')
# input_input_min.clear()
# input_input_min.send_keys("400")
# input_input_min.send_keys(Keys.RETURN)

# apply_bt = driver.find_element_by_class_name("kmCSYg").click()

# input_search_field2 = driver.find_element_by_xpath("//input[@type=’search’]")

# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
# element = driver.find_element_by_id("id-search-field")
