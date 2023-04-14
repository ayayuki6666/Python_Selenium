from time import sleep

from poium import Page,Element


class AnswerPage(Page):
    url="http://10.100.164.47/thread/"
    answer_input=Element(css="div:nth-child(2) > div > div> div > textarea",timeout=5)
    answer_button=Element(css="div> div div:nth-child(2) > div > div > button",timeout=5)
    total_value=Element(xpath="//div/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/div[1]",timeout=5)

    def open_page(self,sequence):
        self.open(self.url+str(sequence))
        sleep(1)
    def answer(self,content):
        sleep(1)
        value_text_before=self.total_value.text[:-3]
        if(value_text_before=="暂"):
            value_before=0
        else:
            value_before=int(value_text_before)
        if(content!=None):
            self.answer_input.send_keys(content)
        self.answer_button.click()
        value_text_after=self.total_value.text[:-3]
        if(value_text_before=="暂"):
            value_after=0
        else:
            value_after=int(value_text_after)
        return (value_after==(value_before+1))