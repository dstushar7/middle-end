import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def take_data_from_json(elements,*args):
    f = open(elements)
    data = json.load(f)
    f.close()
    return (data[arg] for arg in args)


def output_json_incorporate(filename,exists,notExist):
        json_output = {
            'Exists' : exists,
            "Don't Exist" : list(notExist)
        }
        with open(filename, "w") as outfile:
            outfile.write(json.dumps(json_output))


class SearchItems:

    def __init__(self,
                itemList,
                searchField,
                credPath,
                clickXPath,
                entryField,
                searchTag,
                ) -> None:
        self.searchField = searchField
        self.itemList = itemList
        self.credPath = credPath
        self.clickXPath = clickXPath # Link to enter
        self.entryField = entryField # where to entry
        self.searchTag = searchTag # td, which tag to count to check existence


    def login_to_site(self,driver):
        cred = self.credPath
        url, username, password = take_data_from_json(cred,'url','username','password')
        driver.get(url)
        usernameField = driver.find_element(By.NAME,'username')
        usernameField.send_keys(username)
        passField = driver.find_element(By.NAME,'password')
        passField.send_keys(password)
        driver.find_element(By.TAG_NAME,'button').click()
        return driver




    def getting_search_element(self):
        elements = self.itemList
        f = open(elements)
        elements = list()
        for line in f:
            element = line.rstrip("\n").replace(" ","")
            elements.append(element)
        f.close()
        return elements


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


    def existenceChecker(self,log_in,elements):
        # Working process
        exists, notExist = self.check_item(log_in,elements)
        notExistUnique = set(notExist)
        output_json_incorporate("result.json",exists,notExistUnique)
        print(notExistUnique)
        print(len(notExistUnique)," item do not exist. \nCheck result.json file for more info")
        return list(notExistUnique)




    def check_profile(self,elements):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        log_in = self.login_to_site(driver) #Login in to dcrm
        items = self.getting_search_element(elements)
        return self.existenceChecker(log_in,items)

