from driver import driver, wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# funtion params
title_search = "DuckDuckGo — "
search_word = "Selenium"

# locators
text_box = (By.ID, "searchbox_input")
submit = (By.XPATH, "//*[@id='searchbox_homepage']//*[@type='submit']")
result = (By.XPATH, "//*[@data-testid='mainline']//*[@data-testid='result']")

def test_title(title_search):
    wait.until(expected_conditions.title_contains(title_search))
    print("file2 test case1 completed")

def test_search(search_word):
    search_input = wait.until(expected_conditions.visibility_of_element_located(text_box))
    search_input.clear()
    search_input.send_keys(search_word)
    search_button = wait.until(expected_conditions.element_to_be_clickable(submit))
    search_button.click()
    wait.until(expected_conditions.presence_of_all_elements_located(result))
    driver.save_screenshot("results.png")
    print("file2 test case2 completed")

driver.quit()

