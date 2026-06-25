from playwright.sync_api import Page

class homeScrEle:

    def __init__(self, page:Page):

        self.page = page

        self.element = {

            'homepage': ('heading', 'Automation')
        }


    def getElement(self, eleName:str):

        selector, value = self.element[eleName]

        if selector == 'heading':
            return self.page.get_by_role(selector, input=value)

