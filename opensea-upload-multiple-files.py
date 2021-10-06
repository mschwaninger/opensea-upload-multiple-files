from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions

import time
import sys
import os

def uploadFiles(startItemId, count, mnemonicString, walletPwd):
    extension_path='./10.2.0_0.crx'
    opt = webdriver.ChromeOptions()
    opt.add_extension(extension_path)

    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=opt)

    wait = WebDriverWait(driver, 60)
    url = 'https://opensea.io/asset/create'
    collName = 'Capricorn pixel art'
    driver.get(url)
    time.sleep(0.5)
    signIntoMeta(driver, wait, mnemonicString, walletPwd)

    tabs2 = driver.window_handles
    print('switch tab started')
    driver.switch_to.window(tabs2[1])
    print('switch tab completed')

    time.sleep(4)

    createButtonXpath = '//*[@id="__next"]/div[1]/div[1]/nav/ul/div[1]/li[4]/a'
    wait.until(ExpectedConditions.presence_of_element_located(
    (By.XPATH, createButtonXpath)))
    createPage = driver.find_element_by_xpath(createButtonXpath)
    createPage.click()
    filePath = 'capricorn_986.png'
    wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, '//*[@id="media"]')))
    imageUpload = driver.find_element_by_xpath('//*[@id="media"]')
    imagePath = os.path.abspath(filePath)
    imageUpload.send_keys(imagePath)

    while(True):{}

def signIntoMeta(driver, wait, mnemonicString, walletPwd): 
    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[0])
    time.sleep(0.5)
    button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/button')
    button.click()
    print('meta clicked')
    time.sleep(2)
    button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')
    button.click()
    print('import key clicked')
    button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]')
    button.click()
    print('Improve button clicked')
    time.sleep(4)

    mnemonicInput = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input')
    mnemonicInput.send_keys(mnemonicString)
    pwd1Input = driver.find_element_by_xpath('//*[@id="password"]')
    pwd1Input.send_keys(walletPwd)
    pwd2Input = driver.find_element_by_xpath('//*[@id="confirm-password"]')
    pwd2Input.send_keys(walletPwd)

    checkbox = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div')
    checkbox.click()
    time.sleep(4)

    submit = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/button')
    submit.click()
    time.sleep(8)    

    #alles erledigt button
    alldone = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/button')
    alldone.click()

    time.sleep(4)    
    #Modal dialog whats new
    xmodal = driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button')
    xmodal.click()
    time.sleep(4)

    #Switch tab to Opensea
    driver.switch_to.window(tabs2[1])
    time.sleep(4)

    #Open Wallet Menu
    oswalleticon = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[1]/nav/ul/div[2]/li/button')
    oswalleticon.click()
    time.sleep(4)    

    #Open Metamesk Wallet Menu
    metaicon = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/aside/div[2]/div/div[2]/ul/li[1]/button')
    metaicon.click()
    time.sleep(4)    

    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[2])
    print(tabs2)
    time.sleep(4)    

    connectnext = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]')
    connectnext.click()
    time.sleep(4)

    connect = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')
    connect.click()
    time.sleep(10)

    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[2]) 
    print(tabs2)
    sign = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')
    sign.click()
    time.sleep(4)

    # tabs2 = driver.window_handles
    # driver.switch_to.window(tabs2[1])
    # driver.switch_to.window(tabs2[2])
    # print(tabs2)
    # print(driver.title)
    # print('sign into meta completed')
    time.sleep(10) 

if __name__ == '__main__':
    # seed1 = str(sys.argv[1])
    # seed2 = str(sys.argv[2])
    # seed3 = str(sys.argv[3])
    # seed4 = str(sys.argv[4])
    # seed5 = str(sys.argv[5])
    # seed6 = str(sys.argv[6])
    # seed7 = str(sys.argv[7])
    # seed8 = str(sys.argv[8])
    # seed9 = str(sys.argv[9])
    # seed10 = str(sys.argv[10])
    # seed11 = str(sys.argv[11])
    # seed12 = str(sys.argv[12])
    # seed = "{} {} {} {} {} {} {} {} {} {} {} {}".format(seed1,seed2,seed3,seed4,seed5,seed6,seed7,seed8,seed9,seed10,seed11,seed12)
    # password  = str(sys.argv[13])

    uploadFiles(251, 4750,seed, password)


