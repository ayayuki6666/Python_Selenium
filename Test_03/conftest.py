import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Test_03.page.loginpage import LoginPage


@pytest.fixture(scope="session",autouse=True)
def driver():
    ops = Options()
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    ops.add_argument('User-Agent={}'.format(headers['User-Agent']))
    driver=webdriver.Chrome(options=ops)
    driver.get("http://10.100.164.47")
    yield driver
    driver.quit()

@pytest.fixture(scope="session",autouse=True)
def user_driver():
    ops = Options()
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    ops.add_argument('User-Agent={}'.format(headers['User-Agent']))
    driver = webdriver.Chrome(options=ops)
    page=LoginPage(driver)
    account="yaolin6666"
    password="qwerty123"
    page.login(account,password)
    # 登录代码
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_driver():
    ops = Options()
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    ops.add_argument('User-Agent={}'.format(headers['User-Agent']))
    driver = webdriver.Chrome(options=ops)
    yield driver
    driver.quit()
