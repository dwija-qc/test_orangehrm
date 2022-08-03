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

    
 #TC_performance_configureKPI_002
    def test_a_TC_performance_configureKPI_002(self):

        browser = self.browser  
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu__Performance").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_Configure").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_performance_searchKpi"]').click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"kpi360SearchForm[jobTitleCode]"))
        select.select_by_value("10")
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(1)

        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[1]/td[3]').text
        
        self.assertIn("IT Manager",response_data)

    #TC_performance_configureKPI_003
    def test_b_TC_performance_configureKPI_003(self):

        browser = self.browser  
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu__Performance").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_Configure").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_performance_searchKpi"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"defineKpi360[jobTitleCode]"))
        select.select_by_value("10")
        time.sleep(1)
        browser.find_element(By.ID,"defineKpi360_keyPerformanceIndicators").send_keys("Testing UI")
        time.sleep(1)
        browser.find_element(By.ID,"defineKpi360_minRating").clear()
        browser.find_element(By.ID,"defineKpi360_minRating").send_keys("20")
        time.sleep(1)
        browser.find_element(By.ID,"defineKpi360_maxRating").clear()
        browser.find_element(By.ID,"defineKpi360_maxRating").send_keys("100")
        time.sleep(1)
        browser.find_element(By.ID,"defineKpi360_makeDefault").click()
        time.sleep(1)
        browser.find_element(By.ID,"saveBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"resultTable").text
        
        self.assertIn("Testing UI",response_data)


 #TC_performance_configureKPI_004
    def test_c_TC_performance_configureKPI_004(self):

        browser = self.browser  
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu__Performance").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_Configure").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_performance_searchKpi"]').click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        select = Select(browser.find_element(By.NAME,"defineKpi360[jobTitleCode]"))
        select.select_by_value("10")
        time.sleep(1)
        browser.find_element(By.ID,"defineKpi360_keyPerformanceIndicators").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"saveBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.XPATH,'//*[@id="searchKpi"]/fieldset/ol/li[2]/span').text
        
        self.assertIn("Required",response_data)

 #TC_performance_configureKPI_005
    def test_d_TC_performance_configureKPI_005(self):

        browser = self.browser  
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID, "btnLogin").click() 
        time.sleep(3)
        browser.find_element(By.ID,"menu__Performance").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_Configure").click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="menu_performance_searchKpi"]').click()
        time.sleep(1)
        kpi = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[1]/td[2]/a').text
        browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[1]/td[2]/a').click()
        time.sleep(1)
        browser.find_element(By.XPATH,'//*[@id="defineKpi360_keyPerformanceIndicators"]').clear()
        browser.find_element(By.XPATH,'//*[@id="defineKpi360_keyPerformanceIndicators"]').send_keys(kpi + " Edit")
        time.sleep(1)
        browser.find_element(By.ID,"saveBtn").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"resultTable").text
        
        self.assertIn(kpi + " Edit",response_data)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
