from playwright.sync_api import Page


class loginScrEle:

    def __init__(self, page:Page):
        self.page = page

        self.elements = {

            'username': ('locator', '#userEmail'),
            'password': ('locator', '#userPassword'),
            'loginBtn': ('locator', '#login')

        }

    @property
    def getElements(self, eleName:str):

        selector, value = self.elements[eleName]

        if selector == 'locator':
            return self.page.locator(value)
