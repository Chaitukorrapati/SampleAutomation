import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page_object_model.locaters import *
import pytest
from selenium.webdriver.support.select import Select
# from Test_Cases.Conftest import setup

class Test_LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome()


    def Test_login_page(self,Email,Password):
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, input_email_box_xpath).clear()
        driver.find_element(By.XPATH, input_email_box_xpath).send_keys(Email)
        driver.find_element(By.XPATH, input_password_box_xpath).clear()
        driver.find_element(By.XPATH, input_password_box_xpath).send_keys(Password)
        driver.find_element(By.XPATH, click_on_signin_button_xpath).click()
        time.sleep(5)
        driver.close()
        time.sleep(5)
        # driver.find_element(By.XPATH, click_on_logout_button_xpath).click()


    def Test_CustomersPage(self, Email, Password,role,gender,Email_id,Password1,firstname,lastname,date,Companyname,value,description):
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, input_email_box_xpath).clear()
        driver.find_element(By.XPATH, input_email_box_xpath).send_keys(Email)
        driver.find_element(By.XPATH, input_password_box_xpath).clear()
        driver.find_element(By.XPATH, input_password_box_xpath).send_keys(Password)
        driver.find_element(By.XPATH, click_on_signin_button_xpath).click()
        driver.find_element(By.XPATH,Click_on_customer_main_menu_xpath).click()
        time.sleep(5)
        driver.find_element(By.XPATH,click_on_customer_sub_menu_xpath).click()
        driver.find_element(By.XPATH,click_on_add_new_button_xpath).click()
        # driver.find_element(By.XPATH,click_on_Email_xpath).send_keys(Email_id)
        # driver.find_element(By.XPATH,click_on_Password_xpath).send_keys(Password1)
        # driver.find_element(By.XPATH,click_on_first_name_xpath).send_keys(firstname)
        # driver.find_element(By.XPATH,click_on_last_name_xpath).send_keys(lastname)
        # if gender == "male":
        #     driver.find_element(By.XPATH,click_on_gender_male_xpath).click()
        #
        # elif gender == "Female":
        #     driver.find_element(By.XPATH,click_on_gender_female_xpath).click()
        #
        # else:
        #     driver.find_element(By.XPATH, click_on_gender_male_xpath).click()
        #
        # driver.find_element(By.XPATH, click_on_date_picker_xpath).send_keys(date)
        #
        # driver.find_element(By.XPATH,click_on_company_name_xpath).send_keys(Companyname)
        # driver.find_element(By.XPATH,click_on_news_letter_xpath).click()
        # driver.find_element(By.XPATH,click_on_test_store2_xpath).click()
        time.sleep(5)
        driver.find_element(By.XPATH,click_on_Customers_role_xpath).click()
        if role =="Registered":
            listitems = driver.find_element(By.XPATH,click_on_Registered_xpath).click()

        elif role == "Administrators":
            listitems = driver.find_element(By.XPATH,click_on_Administrator_xpath).click()

        elif role == "Guests":
            driver.find_element(By.XPATH,"//span[@title='delete']").click()
            # time.sleep(5)
            listitems = driver.find_element(By.XPATH,click_on_Guests_xpath).click()


        elif role == "Registered":
            listitems = driver.find_element(By.XPATH,click_on_Registered_xpath).click()

        elif role == "Vendors":
            listitems = driver.find_element(By.XPATH,click_on_vendors_xpath).click()

        else:
            listitems = driver.find_element(By.XPATH, click_on_Guests_xpath).click()
        # listitems.click();
        driver.execute_script("arguments[0].click:",listitems)

        # here it will start first name
        driver.find_element(By.XPATH, click_on_first_name_xpath).send_keys(firstname)
        driver.find_element(By.XPATH, click_on_last_name_xpath).send_keys(lastname)
        if gender == "male":
            driver.find_element(By.XPATH, click_on_gender_male_xpath).click()

        elif gender == "Female":
            driver.find_element(By.XPATH, click_on_gender_female_xpath).click()

        else:
            driver.find_element(By.XPATH, click_on_gender_male_xpath).click()

        driver.find_element(By.XPATH, click_on_date_picker_xpath).send_keys(date)

        driver.find_element(By.XPATH, click_on_company_name_xpath).send_keys(Companyname)
        driver.find_element(By.XPATH, click_on_news_letter_xpath).click()
        driver.find_element(By.XPATH, click_on_test_store2_xpath).click()
        time.sleep(5)

        drp = Select(driver.find_element(By.XPATH,click_on_manager_vendor_xpath))
        drp.select_by_visible_text(value)

        driver.find_element(By.XPATH,click_on_Admin_content_xpath).send_keys(description)
        driver.find_element(By.XPATH,click_on_save_button_xpath).click()










