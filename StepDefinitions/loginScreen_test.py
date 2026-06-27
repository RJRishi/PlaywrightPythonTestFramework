import pytest
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page

from POMfiles import *


scenarios('../Features')


@given('Open the Login page')
def login_page(browserpage:Page):
    browserpage.goto('https://rahulshettyacademy.com/client/#/auth/login')


@when('enter Username and password')
def username_pwd(browserpage:Page, un, pwd):

    lse = loginScrEle(browserpage)
    lse.getElements('username').fill('rjrishi.35@gmail.com')
    lse.getElements('password').fill('abcdefgh')


@when('click on Login button')
def login_btn(browserpage:Page):

    lse = loginScrEle(browserpage)
    lse.getElements('loginBtn').click()


