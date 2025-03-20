import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_search_issues_by_title(driver):
    driver.get("https://github.com/microsoft/vscode/issues")
    search_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search issues']")
    search_input.clear()
    search_input.send_keys("in:title bug")
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)

def test_filter_issues_by_author(driver):
    driver.get("https://github.com/microsoft/vscode/issues")
    author_button = driver.find_element(By.CSS_SELECTOR, "summary[aria-label='Author filter']")
    author_button.click()
    author_input = driver.find_element(By.ID, "author-filter-field")
    author_input.send_keys("bpasero")
    author_option = driver.find_element(By.CSS_SELECTOR, "span[title='bpasero']")
    author_option.click()
    time.sleep(5)

def test_advanced_search(driver):
    driver.get("https://github.com/search/advanced")
    language_input = driver.find_element(By.ID, "search_language")
    language_input.send_keys("Python")
    stars_input = driver.find_element(By.ID, "search_stars")
    stars_input.send_keys(">20000")
    filename_input = driver.find_element(By.ID, "search_filename")
    filename_input.send_keys("environment.yml")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    search_button.click()
    time.sleep(5)

def test_commit_activity(driver):
    driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
    graph = driver.find_element(By.CSS_SELECTOR, "canvas")
    actions = ActionChains(driver)
    actions.move_to_element(graph).perform()
    time.sleep(5)

def test_skillbox_courses(driver):
    driver.get("https://skillbox.ru/code/")
    profession_radio = driver.find_element(By.XPATH, "//label[contains(text(), 'Профессия')]")
    profession_radio.click()
    duration_slider = driver.find_element(By.CSS_SELECTOR, ".duration-slider")
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(duration_slider, 50, 0).perform()
    theme_checkbox = driver.find_element(By.XPATH, "//label[contains(text(), 'Программирование')]")
    theme_checkbox.click()
    time.sleep(5)
