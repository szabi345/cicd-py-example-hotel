import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
import pytest


class TestHootel(object):
    def setup_method(self):
        URL = 'http://hotel-v3.progmasters.hu/'
        options = Options()
        options.add_argument("--headless")  #nem nyílik meg a böngésző csak a háttérben fog futni ezzel
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        #self.browser.maximize.window()  #ezzel még nem lesz elég nagy az ablak
        #self.browser.set_window_size(992,600)  #szabadon beállítható ablakméret
        print(self.browser.get_windows_size())  #megadja a megnyitott ablak méretet (alapértelmezetten 780x580 a headless méret)
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    @allure.title("Hootel Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("login")
    def test_login_window_size_992px(self):
        self.browser.set_window_size(991, 600)
        login_btn = self.browser.find_element(By.XPATH, '//a[@class="nav-link"]')
        login_btn.click()

        email_input = self.browser.find_element(By.ID, 'email')
        email_input.send_keys('hiwasi1765@wisnick.com')

        password_input = self.browser.find_element(By.ID, 'password')
        password_input.send_keys('tesztelek2021')

        submit_btn = self.browser.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(1)

        logout_btn = self.browser.find_element(By.ID, 'logout-link')

        assert logout_btn.text == "Kilépés"

    def test_hotel_list(self):
        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

        hotel_list = self.browser.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
        assert len(hotel_list) != 0
        assert len(hotel_list) == 10

    @allure.title("Hootel Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("login")
    def test_login_win_size_991(self):
        self.browser.set_window_size(991, 600)
        login_hamburger_menu = self.browser.find_element(By.XPATH, '//span[@class="navbar-toggler-icon"]')
        login_hamburger_menu.click()
        time.sleep(2)  #megkell várni amíg a menü lenyílik
        login_btn = self.browser.find_element(By.XPATH, '//a[@class="nav-link"]')
        login_btn.click()

        email_input = self.browser.find_element(By.ID, 'email')
        email_input.send_keys('hiwasi1765@wisnick.com')

        password_input = self.browser.find_element(By.ID, 'password')
        password_input.send_keys('tesztelek2021')

        submit_btn = self.browser.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(1)

        logout_btn = self.browser.find_element(By.ID, 'logout-link')

        assert logout_btn.text == "Kilépés"