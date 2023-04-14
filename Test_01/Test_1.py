from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def read(path):
    with open(path,'r') as file:
        data=file.read()
        result =yaml.load(data,Loader=yaml.FullLoader)
        return result

tempSave = []
ops = Options()
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
ops.add_argument('User-Agent={}'.format(headers['User-Agent']))
driver = webdriver.Chrome(options=ops)
account= read ("account.yaml")
for i in range(len(account)):
    driver.get("http://10.100.164.47/user/register")
    sleep(1)
    input = driver.find_elements(By.CSS_SELECTOR,"div .dzq-input .dzq-input__inner")
    inputbutton=driver.find_elements(By.CSS_SELECTOR,"div .dzq-button")[2]
    input1 = input[1]
    input2 = input[2]
    input3 = input[3]
    input4 = input[4]
    input1.send_keys(account[i]["acc"])
    input2.send_keys(account[i]["pwd"])
    input3.send_keys(account[i]["pwd"])
    input4.send_keys(account[i]["name"])
    inputbutton.click()
    sleep(1)
driver.quit()
