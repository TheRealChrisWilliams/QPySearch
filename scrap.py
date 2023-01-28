from selenium import webdriver
from selenium.webdriver.common.by import By


def traverseWeb(driver):
    web_table = {}
    tbody = driver.find_element(By.ID,'ctl00_ctl00_chmain_MITContent_FileGridCS_gvFiles').find_element(By.TAG_NAME,'tbody')
    #print(tbody)
    for ele in tbody.find_elements(By.TAG_NAME,'tr'):
        try:
            link = ele.find_element(By.TAG_NAME,'td').find_element(By.TAG_NAME,'a')
            web_table[link.get_attribute('id')] = link.text
        except Exception as e:
            pass

    for ele_id in web_table:
        if ('..' in web_table[ele_id]):
            pass
            #print("Ignoring parent")
        elif (len(web_table[ele_id]) == 0):
            dummyele = driver.find_element(By.ID,ele_id)
            trueele = dummyele.find_element(By.XPATH,'..').find_element(By.CSS_SELECTOR,"a[target='_blank']")
            print("Found file:",trueele.get_attribute('href'))
        else:
            #print("Traversing into folder: ",web_table[ele_id],"with ID:",ele_id)
            driver.find_element(By.ID,ele_id).click()
            traverseWeb(driver)
            driver.back()

driver = webdriver.Chrome()
import time

driver.get("https://libportal.manipal.edu/MIT/Question%20Paper.aspx")


traverseWeb(driver)
time.sleep(1)