from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions

import time
import sys
import os
import json
from undetected_chromedriver.options import ChromeOptions
import undetected_chromedriver.v2 as uc

attributlist = []
attributdict = {} 
data = 0
driver = 0

def uploadFiles(startitem, enditem, mnemonicString, walletPwd):
    statisticCreator()
    global attributdict
    global driver

#------------------------
    # options = uc.ChromeOptions()

    # extension_path='./10.2.0_0.crx'
    # options.user_data_dir = "c:\\temp\\profile"
    # options.add_extension(extension_path)
    # options.add_argument('--user-data-dir=c:\\temp\\profile2')
    # options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    # driver = uc.Chrome(executable_path='./chromedriver',options=options)
    # with driver:
    #     driver.get('https://opensea.io/asset/create')  
#------------------------

    
    extension_path='./10.2.0_0.crx'
    opt = webdriver.ChromeOptions()
    opt.add_extension(extension_path)
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=opt)
    wait = WebDriverWait(driver, 60)
    url = 'https://opensea.io/asset/create'
    driver.get(url)

    collName = 'Mysterious Capricorn pixel art'
    time.sleep(2.5)
    signIntoMeta(driver, wait, mnemonicString, walletPwd)
    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[1]) 

    for _data in data: # Iteration over all items in JSON        
        if(int(_data['edition']) >= startitem and  int(_data['edition']) <= enditem ):
            print('start:   ----> '+_data['name'] ) 
            createButtonXpath = '//*[@id="__next"]/div[1]/div[1]/nav/ul/div[1]/li[4]/a'
            wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, createButtonXpath)))
            createPage = driver.find_element_by_xpath(createButtonXpath)
            createPage.click()
            #upload image       
            filePath = _data['image'] 
            wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, '//*[@id="media"]')))
            imageUpload = driver.find_element_by_xpath('//*[@id="media"]')
            imagePath = os.path.abspath(filePath)
            imageUpload.send_keys(imagePath)
            name = driver.find_element_by_xpath('//*[@id="name"]')
            name.send_keys(_data['name'])
            description = driver.find_element_by_xpath('//*[@id="description"]')
            description.send_keys(_data['description'])        
            driver.execute_script("window.scrollTo(0, 600)")
            collectionName = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div/form/div[5]/div/div/input')
            collectionName.send_keys(collName)
            # collectionButton = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div/form/div[5]/div/div[2]/div/i')
            # collectionButton.click()            

            collectionButtonFromListName = '//button[normalize-space()="{}"]'.format(collName)
            time.sleep(1)
            try:
                wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, collectionButtonFromListName)))
                collectionButtonFromList = driver.find_element_by_xpath(collectionButtonFromListName)
            except:
                collectionName.send_keys(Keys.CONTROL + "a")
                collectionName.send_keys(Keys.DELETE)
                collectionName.send_keys(collName)
                wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, collectionButtonFromListName)))
                collectionButtonFromList = driver.find_element_by_xpath(collectionButtonFromListName)      
             
            try:
                time.sleep(4)
                collectionButtonFromList.click()
            except:
                time.sleep(4)   
                collectionButtonFromList.click()
            driver.execute_script("window.scrollTo(0, 600)")
            time.sleep(2)        
            propertiesPlusButton = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div/form/section[1]/div[1]/div/div[2]/button')
            propertiesPlusButton.click()
            time.sleep(2)        
            propertyIndex = 0
            for _attributes in _data['attributes']: 
                propertyIndex = propertyIndex + 1          

                propDivNum = 3
                propKeyInputXpath = '/html/body/div[{}]/div/div/div/section/table/tbody/tr[{}]/td[1]/div/div/input'.format(
                    propDivNum, propertyIndex)
                if len(driver.find_elements_by_xpath(propKeyInputXpath)) <= 0:
                    propDivNum = 2
                    propKeyInputXpath = '/html/body/div[{}]/div/div/div/section/table/tbody/tr[{}]/td[1]/div/div/input'.format(
                        propDivNum, propertyIndex)
                if len(driver.find_elements_by_xpath(propKeyInputXpath)) <= 0:
                    propDivNum = 5
                    propKeyInputXpath = '/html/body/div[{}]/div/div/div/section/table/tbody/tr[{}]/td[1]/div/div/input'.format(
                        propDivNum, propertyIndex)

                propKeyInputXpath = '/html/body/div[{}]/div/div/div/section/table/tbody/tr[{}]/td[1]/div/div/input'.format(propDivNum, propertyIndex)
                propertiesKey = driver.find_element_by_xpath(propKeyInputXpath)
                propertiesKey.send_keys(_attributes['trait_type'])

                propValueInputXpath = '/html/body/div[{}]/div/div/div/section/table/tbody/tr[{}]/td[2]/div/div/input'.format(propDivNum, propertyIndex)
                propertiesValue = driver.find_element_by_xpath(propValueInputXpath)
                propertiesValue.send_keys(_attributes['value'])           
                    
                wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add more"]')))
                collectionAddPropButton = driver.find_element_by_xpath('//button[normalize-space()="Add more"]')
                collectionAddPropButton.click()             
            time.sleep(2)
            propSave = driver.find_element_by_xpath('/html/body/div[{}]/div/div/div/footer/button'.format(propDivNum))
            propSave.click()    
            time.sleep(2)      
            driver.execute_script("window.scrollTo(0, 2300)")     
            time.sleep(2) 
            createNFT = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div/form/div/div[1]/span/button')
            createNFT.click()
            time.sleep(8)   
            closeCreateModal = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button')
            closeCreateModal.click()  
            imageSaler()      
            time.sleep(1)  
            print('complete:    ----> '+_data['name'] )               
    while(True):{}

def imageSaler():
    global driver
    time.sleep(4)
    sellButtonXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div/span[2]/a')
    sellButtonXpath.click()
    time.sleep(5)
    
    #Fixprice
    # fixPriceButtonXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div[2]/div/div/form/div/div/div[2]/button[1]')
    # time.sleep(0.2)
    # fixPriceButtonXpath.click()

    amountValueInputXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div[2]/div/div/form/div[2]/div/div[2]/div/div/div[2]/input')
    amountValueInputXpath.send_keys("0.0001")

    #Auction
    # timedAuctionButtonXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div[2]/div/div/form/div/div/div[2]/button[2]')
    # timedAuctionButtonXpath.click()

    # bidderMethodInputXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div[2]/div/div/form/div[2]/div/div[2]/input')
    # bidderMethodInputXpath.send_keys("Sell to highest bidder")

    # amountValueInputXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div[2]/div/div/form/div[3]/div/div[2]/div/div/div[2]/input')
    # amountValueInputXpath.send_keys("0.02")

    # driver.execute_script("window.scrollTo(0, 0)")  
    # time.sleep(0.5)
    # moreOptionButtonXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div[2]/div/div/form/button')
    # moreOptionButtonXpath.click()    

    # reservePriceButtonXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div[2]/div/div/form/div[5]/div/div/div/label/div/div/label/input')
    # reservePriceButtonXpath.click()  

    # time.sleep(0.5)
    # reservePriceInputXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div[2]/div/div/form/div[5]/div/div/div[2]/div/div/div[2]/input')
    # reservePriceInputXpath.send_keys("1.0")

    # driver.execute_script("window.scrollTo(0, 600)")

    driver.execute_script("window.scrollTo(0, 350)")
    time.sleep(5) 
    completeListingButtonXpath = driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[3]/div/div[2]/div/div/form/div[5]/button')
    completeListingButtonXpath.click()

    time.sleep(15)
    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[2]) 

    sign = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')
    sign.click()    

    time.sleep(8)   
    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[1])     
    closeCreateModal = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button')
    closeCreateModal.click()     

def statisticCreator():
    global attributdict
    global attributlist
    global data
    with open("./build/metadata.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for _data in data: 
        for _attributes in _data['attributes']: 
            attributlist.append(_attributes["value"])
            if _attributes["value"] not in attributdict.keys():
                attributdict[_attributes["value"]] = 0

    for _attributdict in attributdict.keys(): 
        attributdict[_attributdict] = 100/len(attributlist) * attributlist.count(_attributdict)

def signIntoMeta(driver, wait, mnemonicString, walletPwd): 
    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[0])
    time.sleep(0.5)
    button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/button')
    button.click()
    time.sleep(2)
    button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')
    button.click()
    button = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]')
    button.click()
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
    time.sleep(5)    

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
    time.sleep(4)    

    connectnext = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]')
    connectnext.click()
    time.sleep(4)

    connect = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')
    connect.click()
    time.sleep(60)

    tabs2 = driver.window_handles
    driver.switch_to.window(tabs2[2]) 
    time.sleep(4)
    sign = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]')
    sign.click()
    time.sleep(5) 

if __name__ == '__main__':
    print("Key: ")
    seed = input()
    print("Password: ")
    password = input()    
    uploadFiles(2, 2,seed, password)