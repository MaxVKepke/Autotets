from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class OlxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.olx.ua')

    def test_1_AuthorizationTest(self):
        driver = self.driver
        login_field = driver.find_element_by_xpath("//*[text()='Мой профиль']")
        login_field.click()
        mail_field = driver.find_element_by_id("userEmail")
        mail_field.send_keys("borcshewskiymax@gmail.com")
        password_field = driver.find_element_by_id("userPass")
        password_field.send_keys("111111")
        button_login = driver.find_element_by_id("se_userLogin")
        button_login.click()

    def test_2_Search(self):
        driver = self.driver
        login_field = driver.find_element_by_xpath("//*[text()='Мой профиль']")
        login_field.click()
        mail_field = driver.find_element_by_id("userEmail")
        mail_field.send_keys("borcshewskiymax@gmail.com")
        password_field = driver.find_element_by_id("userPass")
        password_field.send_keys("111111")
        button_login = driver.find_element_by_id("se_userLogin")
        button_login.click()

        logo_field = driver.find_element_by_id("headerLogo")
        logo_field.click()

        search_field = driver.find_element_by_class_name("autosuggest-input")
        search_field.send_keys("телефон")
        button_search = driver.find_element_by_id("submit-searchmain")
        button_search.click()
        assert "телефон" in driver.page_source
        time.sleep(5)
        button_close = driver.find_element_by_class_name("highlight-close")
        button_close.click()
        time.sleep(10)

        button_paginate = driver.find_element_by_xpath("//div[@class='pager rel clr']/span[4]/a/span")
        driver.execute_script("arguments[0].scrollIntoView(true);", button_paginate)
        time.sleep(10)
        driver.execute_script("arguments[0].click();", button_paginate)
        time.sleep(10)
        button_paginate = driver.find_element_by_xpath("//div[@class='pager rel clr']/span[3]/a/span")
        driver.execute_script("arguments[0].scrollIntoView(true);", button_paginate)
        time.sleep(5)
        driver.execute_script("arguments[0].click();", button_paginate)
        time.sleep(10)
        button_order = driver.find_element_by_xpath("//table[@id='offers_table']//tr[3]//a")
        driver.execute_script("arguments[0].click();", button_order)
        time.sleep(5)

    def test_3_EditSeting(self):
        driver = self.driver
        login_field = driver.find_element_by_xpath("//*[text()='Мой профиль']")
        login_field.click()
        mail_field = driver.find_element_by_id("userEmail")
        mail_field.send_keys("borcshewskiymax@gmail.com")
        password_field = driver.find_element_by_id("userPass")
        password_field.send_keys("111111")
        button_login = driver.find_element_by_id("se_userLogin")
        button_login.click()

        settings_field = driver.find_element_by_id("se_accountShop")
        settings_field.click()
        contact_field = driver.find_element_by_class_name("hvline")
        contact_field.click()
        city_field = driver.find_element_by_id("geoCity")
        city_field.send_keys(Keys.CONTROL+"a")
        city_field.send_keys(Keys.DELETE)
        city_field.send_keys("Винниця")
        city_field.send_keys(Keys.ENTER)
        name_field = driver.find_element_by_id("defaultPerson")
        name_field.send_keys(Keys.CONTROL + "a")
        name_field.send_keys(Keys.DELETE)
        name_field.send_keys("Max")
        button_save = driver.find_element_by_id("submitDefault")
        button_save.click()

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()