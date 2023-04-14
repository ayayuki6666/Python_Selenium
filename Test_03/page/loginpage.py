from time import sleep

from poium import Page, Element


class LoginPage(Page):
    url="http://10.100.164.47/user/username-login"
    input_account=Element(css="div > div > div> div > div > div > div > div> div > div:nth-child(3) > input",timeout=5)
    input_password=Element(css="div > div > div> div > div > div > div > div> div > div:nth-child(5) > input",timeout=5)
    input_submit=Element(css="div > div > div> div > div > div > div > div > div > button",timeout=5)

    def login(self,account,password):
        self.open(self.url)
        if(account!=None):
            self.input_account.send_keys(account)
        if(password!=None):
            self.input_password.send_keys(password)
        sleep(2)
        self.input_submit.click()
        sleep(2)