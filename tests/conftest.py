from selene import browser as brw
import pytest
from selenium import webdriver
from utils import attach
from selene import Browser, Config
from selenium.webdriver.chrome.options import Options




@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    brw.config.base_url = 'https://demoqa.com/'
    brw.config.window_width = 1200
    brw.config.window_height = 1200
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
