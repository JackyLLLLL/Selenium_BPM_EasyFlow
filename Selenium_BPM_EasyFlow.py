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
#driver.maximize_window() #視窗最大化

job_number_xpath = (r"""//*[@id="txtUserId"]""")
password_xpath = (r"""//*[@id="txtPassword"]""")
job_number = "W220002"
password = "Rockerokandko2!"
process_subject = "Test Selenium"

driver.find_element("xpath",job_number_xpath).send_keys(job_number)
driver.find_element("xpath",password_xpath).send_keys(password)

login_xpath = (r'//*[@id="frmSecurityLogin"]/table[1]/tbody/tr[2]/td[3]/table/tbody/tr[7]/td[4]/button[1]')
driver.find_element("xpath",login_xpath).click()

print("登入成功")

driver.execute_script("javascript:prepareProcessData('PART','BPMN')")#點擊料號申請單(JavaScript)
print("點擊料號申請單")
driver.implicitly_wait(1)#等待網站載入(最多等6秒
driver.switch_to.frame("ifmFucntionLocation") #切換到嵌入的網頁
driver.find_element("name","txtSubject").send_keys(process_subject) #輸入流程主旨


driver.switch_to.frame("ifmAppLocation") #切換到嵌入的網頁
driver.find_element("xpath","""//*[@id="rbSales_1"]""").click() #點擊外銷單選框
driver.find_element("xpath","""//*[@id="rbAppType_1"]""").click() #點選外購單選框
driver.find_element("xpath","""//*[@id="rbFactory"]/tbody/tr/td[4]/label""").click() #點選Cougar專用
driver.find_element("xpath","""//*[@id="rbAppType3_0"]""").click() #點選 CASE
driver.find_element("xpath","""//*[@id="rbItemType2"]/tbody/tr/td[1]/label""").click() #點選商品(買進賣出)
driver.find_element("xpath","""//*[@id="rbBOM_0"]""").click() #不建立下階BOM表
driver.find_element("xpath","""//*[@id="rbBOM2_0"]""").click() #不轉內外銷BOM表
driver.find_element("xpath","""//*[@id="rbOPT_0"]""").click() #不同步拋轉至力韡

#申請備品的話客戶料號無須填寫

driver.find_element("xpath","""//*[@id="rbProjectCode3_0"]""").click() #申請依據點選其他

driver.find_element("name","txtDescription").send_keys("這邊未來撈Execl資料") #產品描述
driver.find_element("xpath","""//*[@id="cbPlusS_0"]""").click() #把尾碼+S給打勾起來
driver.find_element("xpath","""//*[@id="btnReference_LFE"]""").click() #點選參考料號
windows = driver.window_handles
driver.switch_to.window(windows[-1]) #切換到當前最新的視窗


driver.find_element("xpath","""//*[@id="_cuzDataChooser_criteria_0"]""").send_keys("3MGC1NXB.0001S") #查詢參考料號
driver.find_element("xpath","""//*[@id="_btnCustomDataChooser_query"]""").click() #點擊搜尋

#driver.find_element("xpath","""""").click()

print("Progarm finish")






