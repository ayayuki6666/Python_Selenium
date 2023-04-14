import re
from time import sleep

import pytest
import yaml
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Test_03.page.answerpage import AnswerPage
from Test_03.page.loginpage import LoginPage
from Test_03.page.postpage import PostPage

def dataGenerate_Login():
    path= "data/login.yaml"
    with open(path,'r') as file:
        data=file.read()
        result =yaml.load(data,Loader=yaml.FullLoader)
        return result

def dataGenerate_Post():
    path= "data/post.yaml"
    with open(path,'r') as file:
        data=file.read()
        result =yaml.load(data,Loader=yaml.FullLoader)
        return result

def dataGenerate_Answer():
    path= "data/answer.yaml"
    with open(path,'r') as file:
        data=file.read()
        result =yaml.load(data,Loader=yaml.FullLoader)
        return result
def dataGenerate_Like():
    path= "data/like.yaml"
    with open(path,'r') as file:
        data=file.read()
        result =yaml.load(data,Loader=yaml.FullLoader)
        return result
#@pytest.mark.skip("暂时跳过")
@pytest.mark.parametrize('param', dataGenerate_Login())
def test_Login(driver,param):
    page=LoginPage(driver)
    page.login(param["account"],param["password"])
    assert param["expected"]==(driver.current_url=="http://10.100.164.47/")
    if(param["expected"]):
        driver.get("http://10.100.164.47/")
        ico = driver.find_element(By.CSS_SELECTOR, " div.dzq-dropdown > div")
        ActionChains(driver).move_to_element(ico).perform()
        button = driver.find_elements(By.CSS_SELECTOR, "li.dzq-dropdown-menu__item")[1]
        ActionChains(driver).move_to_element(button).click().perform()


#@pytest.mark.skip("暂时跳过")
@pytest.mark.parametrize('param', dataGenerate_Post())
def test_Post(user_driver,param):
    page=PostPage(driver=user_driver)
    page.post_content(param["Title"], param["Content"])
    sleep(2)
    assert param["expected"]==(not bool(re.match("http://10.100.164.47/thread/post",user_driver.current_url)))

#@pytest.mark.skip("暂时跳过")
@pytest.mark.parametrize('param', dataGenerate_Answer())
def test_Answer(user_driver,param):
    page=AnswerPage(user_driver)
    page.open_page(param["Sequence"])
    if(user_driver.current_url!="http://10.100.164.47/404"):
        assert_value=page.answer(param["Content"])
    else:
        assert_value=False
    assert param["expected"]==assert_value

#@pytest.mark.skip("暂时跳过")
@pytest.mark.parametrize('param', dataGenerate_Like())
def test_Like(user_driver,param):
    page=AnswerPage(user_driver)
    page.open_page(param["sequence"])
    if(user_driver.current_url!="http://10.100.164.47/404"):
        assert_value=page.like()
    else:
        assert_value=False
    assert param["expected"]==assert_value