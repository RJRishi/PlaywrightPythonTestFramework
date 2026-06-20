import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='module')
def browserpage(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    yield page

    page.close()
    context.close()
    browser.close()
    playwright.stop()

