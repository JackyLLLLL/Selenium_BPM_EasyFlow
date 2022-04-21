import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup


"""
by_id -> find_element("id","")

by_xpath -> find_element("xpath","")

by_link_text -> find_element("link text","")

by_partial_text -> find_element("partial link text","")

by_name -> find_element("name","")

by_tag_name -> find_element("tag name","")

by_class_name -> find_element("class name","")

by_css_selector -> find_element("css selector","")
"""

url = r"http://bpm.hec-group.com.tw:8086/NaNaWeb/GP//ForwardIndex?hdnMethod=findIndexForward"



# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
driver = webdriver.Chrome()
driver.get(url)
#driver.maximize_window()
job_number_xpath = (r"""//*[@id="txtUserId"]""")
password_xpath = (r"""//*[@id="txtPassword"]""")
job_number = "W220002"
password = "Rockerokandko2!"

driver.find_element("xpath",job_number_xpath).send_keys(job_number)
driver.find_element("xpath",password_xpath).send_keys(password)

login_xpath = (r'//*[@id="frmSecurityLogin"]/table[1]/tbody/tr[2]/td[3]/table/tbody/tr[7]/td[4]/button[1]')
driver.find_element("xpath",login_xpath).click()

print("登入成功")


####################################################

# 獲得開啟的第一個視窗控制代碼
window_1 = driver.current_window_handle
# 獲得開啟的所有的視窗控制代碼
windows = driver.window_handles
# 切換到最新的視窗
for current_window in windows:
    #print(current_window)
    #print(window_1,windows)
    if current_window != window_1:
        driver.switch_to.window(current_window)
        print("切換視窗成功")
####################################################

driver.execute_script("javascript:prepareProcessData('PART','BPMN')")#點擊料號申請單(JavaScript)
print("點擊料號申請單")
driver.implicitly_wait(1)#等待網站載入(最多等6秒
#driver.manage().timeouts().implicitlyWait(3, TimeUnit.SECONDS)

container = driver.find_element("id","container")
x=container.find_element("id","tblMenuContent")
print(x)
print("選擇外銷")






