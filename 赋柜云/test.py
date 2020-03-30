from selenium import webdriver
import time
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
driver = webdriver.Chrome("../chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)  # 元素等待
driver.get("http://dk203.idictec.com/qrcodeshop/weixin/login/main.htm")
input_blanks = driver.find_elements_by_css_selector("input")
input_blanks[0].clear()
input_blanks[0].send_keys("18512813888")
input_blanks[1].send_keys("666666")
driver.find_element_by_css_selector("[class='login_btn mui-text-center']").click()
time.sleep(1)
driver.find_element_by_css_selector("[id='tab_setting']").click()
time.sleep(1)
btn = driver.find_elements_by_css_selector("a[class='mui-navigate-right']")[0]
print(btn.get_attribute("href"))
# driver.execute_script("arguments[0].click();", btn)
webdriver.ActionChains(driver).move_to_element(btn).click(btn).perform()