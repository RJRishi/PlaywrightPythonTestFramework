import pytest
from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import Page


scenarios('../Features')


@given('Open the Login page')
def login_page(browserpage:Page):
    browserpage.goto('https://rahulshettyacademy.com/client/#/auth/login')


@when('enter Username and password')
def username_pwd(browserpage:Page):
    yield


@when('click on Login button')
def login_btn(browserpage:Page):
    yield


@then('verify user able to land on Homescreen page')
def homescreen(browserpage:Page):
    yield