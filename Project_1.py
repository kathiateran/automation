#Google Search Test
from selenium import webdriver
import unittest


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/Users/kathiateran/Downloads/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_search_autotest(self):
        self.driver.get("http://google.com/")
        self.driver.find_element_by_name("q").send_keys("how is automation useful")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Auto test completed")

