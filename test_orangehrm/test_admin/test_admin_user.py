import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class admin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #TC_admin_user_001
    def test_a_TC_admin_user_001(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("Arjun")
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertIn('Arjun',response_data)

    #TC_admin_user_002
    def test_c_TC_admin_user_002(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("dilshad")
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertIn('dilshad',response_data)

    #TC_admin_user_003
    def test_b_TC_admin_user_003(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"searchSystemUser[userType]"))
        select.select_by_value("1")
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertNotIn('ESS',response_data)

    #TC_admin_user_005
    def test_d_TC_admin_user_005(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"searchSystemUser[status]"))
        select.select_by_value("1")
        time.sleep(2)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(3)

        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertNotIn('Disable',response_data)

    #TC_admin_user_008
    def test_d_TC_admin_user_008(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(2)
        select = Select(browser.find_element(By.NAME,"systemUser[userType]"))
        select.select_by_value("1")
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Admin A"),
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_userName").send_keys("name12")
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"systemUser[status]"))
        select.select_by_value("1")
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_password").send_keys("adinda123"),
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_confirmPassword").send_keys("adinda123")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertIn('name12',response_data)

        

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()

