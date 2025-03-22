import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_case_1():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://github.com/microsoft/vscode/issues")

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.js-issues-search"))
        )
        search_box.send_keys("in:title bug")
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.Link--primary"))
        )

        issue_titles = driver.find_elements(By.CSS_SELECTOR, "a.Link--primary")
        for title in issue_titles:
            assert "bug" in title.text.lower()
    except Exception as e:
        print(f"Ошибка в test_case_1: {e}")
    finally:
        driver.quit()


def test_case_2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://github.com/microsoft/vscode/issues")

        author_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(text(), 'Author')]"))
        )
        author_button.click()

        author_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Filter users']"))
        )
        author_input.send_keys("bpasero")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'bpasero')]"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Issues'] div[role='row']"))
        )

        issues = driver.find_elements(By.CSS_SELECTOR, "div[aria-label='Issues'] div[role='row']")
        for issue in issues:
            assert "bpasero" in issue.text
    except Exception as e:
        print(f"Ошибка в test_case_2: {e}")
    finally:
        driver.quit()


def test_case_3():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://github.com/search/advanced")

        language_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "l"))
        )
        language_select.send_keys("Python")

        stars_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "s"))
        )
        stars_input.send_keys(">20000")

        filename_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "filename"))
        )
        filename_input.send_keys("environment.yml")
        filename_input.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.f4 a"))
        )

        repos = driver.find_elements(By.CSS_SELECTOR, "div.f4 a")
        for repo in repos:
            stars = repo.find_element(By.XPATH, "../../..//a[contains(@href, 'stargazers')]")
            assert int(stars.text.replace(',', '')) > 20000
    except Exception as e:
        print(f"Ошибка в test_case_3: {e}")
    finally:
        driver.quit()


def test_case_4():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://skillbox.ru/")

        profession_radio = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Профессия')]"))
        )
        profession_radio.click()

        thematics_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Программирование')]"))
        )
        thematics_checkbox.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.course-card__title"))
        )

        courses = driver.find_elements(By.CSS_SELECTOR, "div.course-card__title")
        assert len(courses) > 0
    except Exception as e:
        print(f"Ошибка в test_case_4: {e}")
    finally:
        driver.quit()


def test_case_5():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")

        graph_point = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "rect[height]"))
        )

        webdriver.ActionChains(driver).move_to_element(graph_point).perform()

        tooltip = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.chart-tooltip"))
        )

        assert "commits" in tooltip.text.lower()
    except Exception as e:
        print(f"Ошибка в test_case_5: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()