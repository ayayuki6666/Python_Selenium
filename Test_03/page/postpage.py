from time import sleep

from poium import Page,Element

class PostPage(Page):
    url="http://10.100.164.47/thread/post"
    post_title_input=Element(css="#dzq-threadpost-title > div > input",timeout=5)
    post_title_content=Element(css="div.vditor-wysiwyg > pre",timeout=5)
    post_title_confirm=Element(css="div > div > div> div> div> button.dzq-button.dzq-button--medium.dzq-button--primary",timeout=5)

    def post_content(self, title, content):
        self.open(self.url)
        sleep(2)
        if (title!=None):
            self.post_title_input.send_keys(title)
        if (content!= None):
            self.post_title_content.send_keys(content)
        self.post_title_confirm.click()
