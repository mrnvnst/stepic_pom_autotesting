from stepic_pom_autotesting.data import Urls as U
from stepic_pom_autotesting.pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = U.link
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

