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

    
 #TC_recruitment_candidates_002
    def test_a_TC_recruitment_candidates_002(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"candidateSearch[jobTitle]"))
        select.select_by_value("7")
        time.sleep(1)
        browser.find_element(By.ID,"btnSrch").click()
        time.sleep(1)

        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[1]/td[2]').text
        
        self.assertIn("Software Engineer",response_data)

#TC_recruitment_candidates_003
    def test_a_TC_recruitment_candidates_003(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"candidateSearch[jobVacancy]"))
        select.select_by_value("4")
        time.sleep(1)
        browser.find_element(By.ID,"btnSrch").click()
        time.sleep(1)

        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[2]/td[2]').text
        
        self.assertIn("Associate IT Manager",response_data)

 #TC_recruitment_candidates_008
    def test_a_TC_recruitment_candidates_008(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_firstName").send_keys("Dwijayan")
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_lastName").send_keys("N")
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_email").send_keys("dwija@gmail.com")
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"addCandidate[vacancy]"))
        select.select_by_value("4")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data = browser.find_element(By.NAME,"addCandidate[firstName]").text
        
        self.assertIn("Dwijayan",response_data)

 #TC_recruitment_candidates_009
    def test_a_TC_recruitment_candidates_009(self):

        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_firstName").send_keys("Dwijayan")
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_lastName").send_keys("N")
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_email").send_keys("")
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"addCandidate[vacancy]"))
        select.select_by_value("4")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(2)

        response_data = browser.find_element(By.XPATH,'//*[@id="frmAddCandidate"]/fieldset/ol[1]/li[2]/span').text
        
        self.assertIn("Required",response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
