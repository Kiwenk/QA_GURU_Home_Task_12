from selene import browser, Browser, Config
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import attach


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/'  # исправил
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_width = 1200
    browser.config.window_height = 1200

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

    BR = Browser(Config(driver))

    yield BR

    attach.add_screenshot(BR)
    attach.add_logs(BR)
    attach.add_html(BR)
    attach.add_video(BR)

    browser.quit()
