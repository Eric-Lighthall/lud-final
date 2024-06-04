import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_py
import time

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox") # needed for linux enviroments
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("https://letsusedata.com/index.html")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.letsusedata.com/index.html")

        username_field = driver.find_element(By.ID, "txtUser")
        password_field = driver.find_element(By.ID, "txtPassword")
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")

        username_field.send_keys("test1")
        password_field.send_keys("Test12456")
        login_button.click()

        time.sleep(3)

        expected_url = "https://www.letsusedata.com/CourseSelection.html"
        self.assertEqual(driver.current_url, expected_url)

    def test_login_2(self):
        driver = self.driver
        driver.get("https://www.letsusedata.com/index.html")

        username_field = driver.find_element(By.ID, "txtUser")
        password_field = driver.find_element(By.ID, "txtPassword")
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")

        username_field.send_keys("test1")
        password_field.send_keys("test1234")
        login_button.click()

        time.sleep(3)

        expected_url = "https://www.letsusedata.com/CourseSelection.html"
        self.assertEqual(driver.current_url, expected_url)


if __name__ == "__main__":
    unittest.main(verbosity=2)
