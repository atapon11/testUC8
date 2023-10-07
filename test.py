from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.chrome.service import Service

class YourTest(unittest.TestCase):

    def setUp(self):
        # กำหนดค่า WebDriver ของ Chrome โดยใช้ Service
        service = Service('C:/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
           
    def tearDown(self):
        # ปิดเบราว์เซอร์
        self.driver.quit()

    def test_login(self):
        # เปิดเว็บไซต์
        self.driver.get("https://online-web-mauve.vercel.app/")

        # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # ค้นหา input fields ของรหัสประจำตัวประชาชนและรหัสผ่าน และป้อนค่า
        id_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
        password_input = self.driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")
        id_input.send_keys("7777777777777")
        password_input.send_keys("123456")

        # คลิกปุ่ม "เข้าสู่ระบบ"
        login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
        login_button.click()
        time.sleep(5)

        # คลิกที่ <div> "ดูข้อมูลการจองคิว"
        div_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "ดูข้อมูลการจองคิว")]')
        div_element.click()
        time.sleep(5)

        # คุณสามารถเพิ่มการตรวจสอบเพิ่มเติมหรือการตรวจสอบได้ที่นี่หากต้องการ

if __name__ == "__main__":
    unittest.main()
