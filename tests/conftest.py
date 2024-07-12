from selene import browser
import pytest
from selenium import webdriver
from utils import attach



@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/' #исправил
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_width = 1200
    browser.config.window_height = 1200
    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
