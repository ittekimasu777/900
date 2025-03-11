from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_search_issues_by_title():
    try:
        driver.get("https://github.com/microsoft/vscode/issues")
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search issues']"))
        )
        search_input.clear()
        search_input.send_keys("in:title bug")
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)
    finally:
        driver.quit()

def test_filter_issues_by_author():
    try:
        driver.get("https://github.com/microsoft/vscode/issues")
        author_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "summary[aria-label='Author filter']"))
        )
        author_button.click()
        author_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "author-filter-field"))
        )
        author_input.send_keys("bpasero")
        author_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[title='bpasero']"))
        )
        author_option.click()
        time.sleep(5)
    finally:
        driver.quit()

def test_advanced_search():
    try:
        driver.get("https://github.com/search/advanced")
        language_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_language"))
        )
        language_input.send_keys("Python")
        stars_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_stars"))
        )
        stars_input.send_keys(">20000")
        filename_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_filename"))
        )
        filename_input.send_keys("environment.yml")
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        search_button.click()
        time.sleep(5)
    finally:
        driver.quit()

def test_skillbox_courses():
    try:
        driver.get("https://skillbox.ru/code/")
        profession_radio = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Профессия')]"))
        )
        profession_radio.click()
        duration_slider = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".duration-slider"))
        )
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(duration_slider, 50, 0).perform()
        theme_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Программирование')]"))
        )
        theme_checkbox.click()
        time.sleep(5)
    finally:
        driver.quit()

def test_commit_activity():
    try:
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        graph = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "canvas"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(graph).perform()
        time.sleep(5)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_search_issues_by_title()
    test_filter_issues_by_author()
    test_advanced_search()
    test_skillbox_courses()
    test_commit_activity()



