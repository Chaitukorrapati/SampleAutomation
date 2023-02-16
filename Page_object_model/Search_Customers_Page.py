from selenium import webdriver
from selenium.webdriver.common.by import By



class SearchCustomer:
    text_email_xpath  = "//input[@id='SearchEmail']"
    text_First_name_xpath = "//input[@id='SearchFirstName']"
    text_last_name_xpath = "//input[@id='SearchLastName']"
    click_on_search_btn = "//button[@id='search-customers']"
    table_search_xpath = "//table[@role='grid]"
    table_xpath  = "//table[@id='customers-grid']"
    table_row_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.text_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_email_xpath).send_keys(email)

    def setFirstname(self,firstname):
        self.driver.find_element(By.XPATH,self.text_First_name_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_First_name_xpath).send_keys(firstname)

    def setlastname(self,lastname):
        self.driver.find_element(By.XPATH,self.text_last_name_xpath).clear()
        self.driver.find_element(By.XPATH,self.text_last_name_xpath).send_keya(lastname)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self. click_on_search_btn).click()

    def Getnoofrows(self):
        return len(self.driver.find_element(By.XPATH,self.table_row_xpath))

    def getnoofcolumns(self):
        return len(self.driver.find_element(By.XPATH,self.table_column_xpath))


    def SearchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.Getnoofrows()+1):
                table = self.driver.find_element(By.XPATH,(self.table_xpath))
                emailid= self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
                if emailid == email:
                    flag = True
                    break
                return flag

    def SearchCustomerByName(self,Name):
        flag = False
        for r in range(1,self.getnoofcolumns()+1):
            table = self.driver.find_element(By.XPATH,(self.table_xpath))
            name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag






















