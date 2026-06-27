
from POMfiles import *
from playwright.sync_api import Page
from pytest_bdd import then, when, given, scenarios


scenarios('../Features')



@then('verify user able to land on Homescreen page')
def homescreen(browserpage:Page):

    hse = homeScrEle(browserpage)
    assert hse.getElement('homepage').inner_text() == 'Automation'