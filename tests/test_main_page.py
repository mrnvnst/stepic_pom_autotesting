from selenium.webdriver.common.by import By
from stepic_pom_autotesting.data import Urls as U


def test_guest_can_go_to_login_page(browser):
    browser.get(U.link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

