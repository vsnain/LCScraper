# code from @--smallguy89--'s template

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def new_driver():
  chrome_options = Options()
  # chrome_options.headless = True
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window()
  driver.implicitly_wait(10)
  return driver


def scroll_to_bottom(driver):
  driver.execute_script('window.scrollBy(0,document.body.scrollHeight);')


def get_html(url, driver):
  driver.get(url)
  time.sleep(3)
  return driver.page_source


def get(url, driver):
  driver.get(url)
  time.sleep(3)
  return


def close_chrome(driver):
  driver.quit()
