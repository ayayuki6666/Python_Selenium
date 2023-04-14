import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from parameterized import parameterized
from XTestRunner import HTMLTestRunner
import yaml
def data_bulid():
    with open("input.yaml",'r') as file:
        data=file.read()
        result =yaml.load(data,Loader=yaml.FullLoader)
        data=[]
        for i in result:
            data.append((i["expected"],i["category"],i["sequence"]))
        return data
class Test_Case_01(unittest.TestCase):
            def setUp(self) -> None:
                ops = Options()
                headers = {
                    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
                ops.add_argument('User-Agent={}'.format(headers['User-Agent']))
                self.driver = webdriver.Chrome(options=ops)
                driver =self.driver
                driver.get("http://10.100.164.47/admin/login")
                sleep(2)
                input = driver.find_elements(By.CSS_SELECTOR, ".el-input__inner")
                input[0].send_keys("admin")
                input[1].send_keys("admin")
                input = driver.find_element(By.CSS_SELECTOR, ".el-button")
                input.click()
                sleep(1)

            def tearDown(self) -> None:
                sleep(2)
                self.driver.quit()

            @parameterized.expand(data_bulid())
            def test_1_Input(self,expect,category,sequence):
                driver=self.driver
                driver.get("http://10.100.164.47/admin/cont-class")
                sleep(1)
                countBefore=len(driver.find_elements(By.CSS_SELECTOR,".el-table__row"))
                additon=driver.find_elements(By.CSS_SELECTOR,".iconfont")[6]
                ActionChains(driver).move_to_element(additon).click().perform()
                input=driver.find_elements(By.CSS_SELECTOR,".el-input__inner")
                inputName=input[countBefore*3+0]
                inputSequence=input[countBefore*3+1]
                inputName.send_keys(category)
                inputSequence.send_keys(sequence)
                sleep(1)
                confirmButton=driver.find_element(By.CSS_SELECTOR,".card-box__main>.el-button")
                confirmButton.click()
                sleep(2)
                countAfter=len(driver.find_elements(By.CSS_SELECTOR,".el-table__row"))
                sleep(2)
                self.assertEqual(expect,(countBefore+1)==countAfter)

            @parameterized.expand(data_bulid())
            def test_2_Delete(self,expect,category,sequence):
                driver=self.driver
                driver.get("http://10.100.164.47/admin/cont-class")
                flag=False
                sleep(1)
                countBefore = len(driver.find_elements(By.CSS_SELECTOR, ".el-table__row"))
                deletebuttonList = driver.find_elements(By.CSS_SELECTOR, ".el-popover__reference-wrapper>.el-button")
                input = driver.find_elements(By.CSS_SELECTOR, ".el-input__inner")
                for i in range(countBefore):
                    if (input[3 * i].get_attribute("value") == category):
                        deletebuttonList[i].click()
                        flag=True
                sleep(2)
                if(flag):
                    deleteConfirm = driver.find_elements(By.CSS_SELECTOR, ".el-popover>div>.el-button")
                    deleteConfirm[len(deleteConfirm) - 1].click()
                    sleep(2)
                countAfter = len(driver.find_elements(By.CSS_SELECTOR, ".el-table__row"))
                sleep(2)
                self.assertEqual(expect,countAfter==(countBefore-1))


if __name__ == '__main__':
    suit = unittest.TestLoader().discover(
        # 找到被执行模块的路径
        start_dir="",
        # 加载路径下所有以test_开头的测试模块的文件
        pattern='UnitTest.py'  # 正则表达式
    )
    with(open('unit_result.html', 'wb')) as file:
        runner = HTMLTestRunner(
            stream=file,
            title='自动化测试报告',
            description=['类型：selenium', '操作系统：Windows', '浏览器：Chrome', '执行人：筱沫'],
            language='en',
        )
        runner.run(suit)