from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

ops = Options()
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
ops.add_argument('User-Agent={}'.format(headers['User-Agent']))
driver = webdriver.Chrome(options=ops)
driver.get("http://10.100.164.47/admin/login")
sleep(2)
input = driver.find_elements(By.CSS_SELECTOR,".el-input__inner")
input[0].send_keys("admin")
input[1].send_keys("admin")
input=driver.find_element(By.CSS_SELECTOR,".el-button")
input.click()
sleep(1)


# driver.get("http://10.100.164.47/admin/cont-class")
# sleep(1)
# countBefore=len(driver.find_elements(By.CSS_SELECTOR,".el-table__row"))
#
# additon=driver.find_elements(By.CSS_SELECTOR,".iconfont")[6]
# ActionChains(driver).move_to_element(additon).click().perform()
# input=driver.find_elements(By.CSS_SELECTOR,".el-input__inner")
# inputName=input[countBefore*3+0]
# inputSequence=input[countBefore*3+1]
# inputName.send_keys("1")
# inputSequence.send_keys("2")
# sleep(1)
# confirmButton=driver.find_element(By.CSS_SELECTOR,".card-box__main>.el-button")
# confirmButton.click()
#
# countAfter=len(driver.find_elements(By.CSS_SELECTOR,".el-table__row"))
# sleep(3)
# input.send_keys("test")
# sleep(2)


driver.get("http://10.100.164.47/admin/cont-class")
sleep(1)
countBefore=len(driver.find_elements(By.CSS_SELECTOR,".el-table__row"))
deletebuttonList=driver.find_elements(By.CSS_SELECTOR,".el-popover__reference-wrapper>.el-button")
input=driver.find_elements(By.CSS_SELECTOR,".el-input__inner")
for i in range(countBefore):
    if(input[3*i].get_attribute("value")=="1"):
        deletebuttonList[i].click()
sleep(2)
deleteConfirm=driver.find_elements(By.CSS_SELECTOR,".el-popover>div>.el-button")
deleteConfirm[len(deleteConfirm)-1].click()
countAfter=len(driver.find_elements(By.CSS_SELECTOR,".el-table__row"))
sleep(2)