from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import utility as util

class SearchItems:

    def __init__(self,
                itemListDirectory,
                searchField,
                credentialsPathDirectory,
                clickXPath,
                searchTag,
                ) -> None:
        self.searchField = searchField
        self.itemListDirectory = itemListDirectory
        self.credentialsPathDirectory = credentialsPathDirectory
        self.clickXPath = clickXPath # Link to enter
        self.searchTag = searchTag # td, which tag to count to check existence


    def login_to_site(self,driver):
        cred = self.credentialsPathDirectory
        url, username, password = util.take_data_from_json(cred,'url','username','password')
        driver.get(url)
        usernameField = driver.find_element(By.NAME,'username')
        usernameField.send_keys(username)
        passField = driver.find_element(By.NAME,'password')
        passField.send_keys(password)
        driver.find_element(By.TAG_NAME,'button').click()
        return driver




    def getting_search_element(self):
        elementPath = self.itemListDirectory
        f = open(elementPath)
        elementPath = list()
        for line in f:
            element = line.rstrip("\n").replace(" ","")
            elementPath.append(element)
        f.close()
        return elementPath


    def check_item(self,driver,item_list):
        no_profile = []
        existing_profile = []
        accountsLink = driver.find_element(By.XPATH, self.clickXPath).get_attribute("href")
        driver.get(accountsLink)
        for element in item_list:
            # Number must be string
            msisdnField = driver.find_element(By.ID, self.searchField)
            msisdnField.clear()
            msisdnField.send_keys(element)
            search_button = driver.find_element(By.TAG_NAME,'button')
            driver.find_element(By.XPATH,'//body').click() # Click on empty places to cancel out javascript
            search_button.click()
            driver.find_element(By.XPATH,'//body').click()
            profile_status = driver.find_elements(By.TAG_NAME,self.searchTag)
            if len(profile_status)>0:
                existing_profile.append(element)
            else:
                no_profile.append(element)
            driver.back()
        driver.close()
        return existing_profile, no_profile


    def existenceChecker(self,log_in,elementPath):
        # Working process
        exists, notExist = self.check_item(log_in,elementPath)
        notExistUnique = set(notExist)
        util.output_json_incorporate("result.json",exists,notExistUnique)
        print(notExistUnique)
        print(len(notExistUnique)," item do not exist. \nCheck result.json file for more info")
        return list(notExistUnique)




    def search_initiator(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        log_in = self.login_to_site(driver) #Login in to dcrm
        items = util.getting_search_element(self.itemListDirectory)
        return self.existenceChecker(log_in,items)

