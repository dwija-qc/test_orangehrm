from random import random
from select import select
from tkinter.tix import Select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class admin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #TC_PIM_configuration_customfield_002
    def test_a_TC_PIM_configuration_customfield_002(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_pim_listCustomFields"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"buttonAdd").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="customField_name"]').send_keys("Email Address")
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"customField[screen]"))
        select.select_by_value("contact")
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"customField[type]"))
        select.select_by_value("0")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"customFieldList").text

        self.assertIn("Email Address",response_data)

#TC_PIM_configuration_customfield_003
    def test_b_TC_PIM_configuration_customfield_003(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_pim_listCustomFields"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"buttonAdd").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="customField_name"]').send_keys("")
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"customField[screen]"))
        select.select_by_value("contact")
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"customField[type]"))
        select.select_by_value("0")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data = browser.find_element(By.XPATH,'//*[@id="frmCustomField"]/fieldset/ol/li[1]/span').text

        self.assertIn("Required",response_data)

    #TC_PIM_configuration_customfield_004
    def test_c_TC_PIM_configuration_customfield_004(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_pim_listCustomFields"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"buttonAdd").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="customField_name"]').send_keys("Email Address")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data = browser.find_element(By.XPATH,'//*[@id="frmCustomField"]/fieldset/ol/li[2]/span').text

        self.assertIn("Required",response_data)

    #TC_PIM_configuration_customfield_005
    def test_d_TC_PIM_configuration_customfield_005(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_pim_listCustomFields"]').click()
        time.sleep(1)
        fieldname = browser.find_element(By.XPATH,'//*[@id="customFieldList"]/tbody/tr[1]/td[2]/a').text
        browser.find_element(By.XPATH,'//*[@id="customFieldList"]/tbody/tr[1]/td[2]/a').click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="customField_name"]').clear()
        browser.find_element(By.XPATH,'//*[@id="customField_name"]').send_keys(fieldname + " Edit")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"customFieldList").text

        self.assertIn(fieldname + " Edit",response_data)

    #TC_PIM_configuration_customfield_006
    def test_e_TC_PIM_configuration_customfield_006(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_pim_listCustomFields"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="customFieldList"]/tbody/tr[1]/td[2]/a').click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="customField_name"]').clear()
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data = browser.find_element(By.XPATH,'//*[@id="frmCustomField"]/fieldset/ol/li[1]/span').text

        self.assertIn("Required",response_data)   

    #TC_PIM_configuration_customfield_006
    def test_e_TC_PIM_configuration_customfield_006(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_Configuration").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_pim_listCustomFields"]').click()
        time.sleep(1)
        fieldDel = browser.find_element(By.XPATH,'//*[@id="customFieldList"]/tbody/tr[1]/td[2]').text
        browser.find_element(By.XPATH,'//*[@id="customFieldList"]/tbody/tr[1]/td[1]/input').click()
        time.sleep(1)
        browser.find_element(By.ID,"buttonRemove").click()
        time.sleep(1)
        browser.find_element(By.ID,"dialogDeleteBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"customFieldList").text

        self.assertNotIn(fieldDel,response_data)   

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
