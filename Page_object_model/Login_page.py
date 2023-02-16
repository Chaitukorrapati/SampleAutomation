from selenium import webdriver
from selenium.webdriver.common.by import By

class Loginpage:
    input_email_box_xpath = "//input[@id='Email']"
    input_password_box_xpath = "//input[@id='Password']"
    click_on_signin_button_xpath = "//button[text()='Log in']"
    click_on_logout_button_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver



    def setusername(self,Email):
        self.driver.find_element(By.XPATH, self.input_email_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_email_box_xpath).send_keys(Email)

    def setpassword(self,Password):
        self.driver.find_element(By.XPATH, self.input_password_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_password_box_xpath).send_keys(Password)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.click_on_signin_button_xpath).click()

    def click_on_logout(self):
        self.driver.find_element(By.XPATH, self.click_on_logout_button_xpath).click()
