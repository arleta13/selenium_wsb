# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep
from termcolor import colored
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

valid_name = "Dick"
valid_surname = "Laurent"
gender = 'male'
valid_phone = '123234345'
invalid_phone = 'abc'
invalid_email = "dlaurent.isdead.com"
valid_password = "Qwerty111$"
valid_country = "Rosja"
valid_email = "dlaurent@isdead.com"

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        # Przeglądarka otwarta na https://wizzair.com/pl-pl#/
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def tearDown(self):
        self.driver.quit()

    def test_wrong_telephone(self):
        driver = self.driver
        # 1. Kliknij ZALOGUJ SIĘ
        zaloguj_btn= WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        # 2. Kliknij REJESTRACJA
        rejestracja_btn = driver.find_element_by_xpath('//button[text()="Rejestracja"]')
        rejestracja_btn.click()
        # 3. Wprowadź imię
        imie_input = driver.find_element_by_name("firstName")
        imie_input.send_keys(valid_name)
        # 4. Wprowadź nazwisko
        nazwisko_input = driver.find_element_by_css_selector('input[placeholder="Nazwisko"]')
        nazwisko_input.send_keys(valid_surname)
        # 5. Wybierz płeć
        #imie_input.click()
        if gender == 'male':
            imie_input.click()
            gender_switch = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            gender_switch.click()
        else:
            gender_switch = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            gender_switch.click()
        # 6. Wprowadź numer telefonu
        telephone_input = driver.find_element_by_xpath('//input[@placeholder="Telefon komórkowy"]')
        telephone_input.send_keys(invalid_phone)
        # 7. Wprowadź błędny adres e-mail (brak znaku '@')
        email_input = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_input.send_keys(valid_email)
        # 8. Wprowadź hasło
        passwd_input = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        passwd_input.send_keys(valid_password)
        # 9. Wybierz kraj
        narodowosc_input = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        narodowosc_input.click()
        #country_container = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]')
        #countries_list = country_container.find_elements_by_tag_name('label')
        # Lista krajów
        countries_list = driver.find_elements_by_xpath('//div[@class="register-form__country-container__locations"]/label')
        for label in countries_list:
            option = label.find_element_by_tag_name('strong')
            if option.get_attribute("innerText") == valid_country:
                option.location_once_scrolled_into_view
                option.click()
                break
        # 10. Zaznacz "Akceptuję Informację o polityce prywatności"
        privacy_policy = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        privacy_policy.click()
        # 11. Kliknij ZAREJESTRUJ SIĘ
        zarejestruj_btn = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        zarejestruj_btn.click()

        ### Oczekiwany rezultat ###
        # Użytkownik dostaje informację "Nieprawidłowy numer telefonu"

        # Wyszukuję wszystkie błędy
        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                # Dodaję widoczne błędy do listy visible_error_notices
                visible_error_notices.append(error)
        print(colored("\nUWAGA! - TEST ZNAJDUJE PRAWDZIWY BŁĄD (FAIL JEST ZAMIERZONY)!!!", "red"))
        # Sprawdzam, czy widoczny błąd jest tylko jeden
        self.assertEqual(len(visible_error_notices),1)
        # Sprawdzam poprawność treści błędu
        self.assertEqual(visible_error_notices[0].text, u"Nieprawidłowy numer telefonu")
        #sleep(1)


    def test_correct_registration(self): # BEZ KLIKANIA ZAREJESTRUJ
        driver = self.driver
        # 1. Kliknij ZALOGUJ SIĘ
        zaloguj_btn= WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        # 2. Kliknij REJESTRACJA
        rejestracja_btn = driver.find_element_by_xpath('//button[text()="Rejestracja"]')
        rejestracja_btn.click()
        # 3. Wprowadź imię
        imie_input = driver.find_element_by_name("firstName")
        imie_input.send_keys(valid_name)
        # 4. Wprowadź nazwisko
        nazwisko_input = driver.find_element_by_css_selector('input[placeholder="Nazwisko"]')
        nazwisko_input.send_keys(valid_surname)
        # 5. Wybierz płeć
        #imie_input.click()
        if gender == 'male':
            imie_input.click()
            gender_switch = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            gender_switch.click()
        else:
            gender_switch = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            gender_switch.click()
        # 6. Wprowadź numer telefonu
        telephone_input = driver.find_element_by_xpath('//input[@placeholder="Telefon komórkowy"]')
        telephone_input.send_keys(valid_phone)
        # 7. Wprowadź poprawny adres e-mail
        email_input = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_input.send_keys(valid_email)
        # 8. Wprowadź hasło
        passwd_input = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        passwd_input.send_keys(valid_password)
        # 9. Wybierz kraj
        narodowosc_input = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        narodowosc_input.click()
        #country_container = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]')
        #countries_list = country_container.find_elements_by_tag_name('label')
        # Lista krajów
        countries_list = driver.find_elements_by_xpath('//div[@class="register-form__country-container__locations"]/label')
        for label in countries_list:
            option = label.find_element_by_tag_name('strong')
            if option.get_attribute("innerText") == valid_country:
                option.location_once_scrolled_into_view
                option.click()
                break
        # Wyszukaj konkretny kraj (Polskę)
        # country_to_choose = driver.find_element_by_xpath('//label[@data-test="booking-register-country-label"][164]/strong')
        # country_to_choose.location_once_scrolled_into_view
        # country_to_choose.click()
        # 10. Zaznacz "Akceptuję Informację o polityce prywatności"
        privacy_policy = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        privacy_policy.click()
        # 11. Kliknij ZAREJESTRUJ SIĘ
        print(colored("\nPomijam klikanie zarejestruj, by nie zakładać konta Wizz Airowi", "yellow"))
        #zarejestruj_btn = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        #zarejestruj_btn.click()

        ### Oczekiwany rezultat ###
        #Brak błędów
        # Wyszukuję wszystkie błędy
        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                # Dodaję widoczne błędy do listy visible_error_notices
                visible_error_notices.append(error)
        # Sprawdzam, czy lista widocznych błędów jest pusta
        self.assertEqual(len(visible_error_notices),0)

    #@unittest.skip("Pomijam...")
    def test_wrong_email(self):
        driver = self.driver
        # 1. Kliknij ZALOGUJ SIĘ
        zaloguj_btn= WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        # 2. Kliknij REJESTRACJA
        rejestracja_btn = driver.find_element_by_xpath('//button[text()="Rejestracja"]')
        rejestracja_btn.click()
        # 3. Wprowadź imię
        imie_input = driver.find_element_by_name("firstName")
        imie_input.send_keys(valid_name)
        # 4. Wprowadź nazwisko
        nazwisko_input = driver.find_element_by_css_selector('input[placeholder="Nazwisko"]')
        nazwisko_input.send_keys(valid_surname)
        # 5. Wybierz płeć
        #imie_input.click()
        if gender == 'male':
            imie_input.click()
            gender_switch = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            gender_switch.click()
        else:
            gender_switch = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            gender_switch.click()
        # 6. Wprowadź numer telefonu
        telephone_input = driver.find_element_by_xpath('//input[@placeholder="Telefon komórkowy"]')
        telephone_input.send_keys(valid_phone)
        # 7. Wprowadź błędny adres e-mail (brak znaku '@')
        email_input = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_input.send_keys(invalid_email)
        # 8. Wprowadź hasło
        passwd_input = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        passwd_input.send_keys(valid_password)
        # 9. Wybierz kraj
        narodowosc_input = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        narodowosc_input.click()
        #country_container = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]')
        #countries_list = country_container.find_elements_by_tag_name('label')
        # Lista krajów
        countries_list = driver.find_elements_by_xpath('//div[@class="register-form__country-container__locations"]/label')
        for label in countries_list:
            option = label.find_element_by_tag_name('strong')
            if option.get_attribute("innerText") == valid_country:
                option.location_once_scrolled_into_view
                option.click()
                break
        # 10. Zaznacz "Akceptuję Informację o polityce prywatności"
        privacy_policy = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        privacy_policy.click()
        # 11. Kliknij ZAREJESTRUJ SIĘ
        zarejestruj_btn = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        zarejestruj_btn.click()

        ### Oczekiwany rezultat ###
        # Użytkownik dostaje informację "Nieprawidłowy adres e-mail"

        # Wyszukuję wszystkie błędy
        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        visible_error_notices = []
        for error in error_notices:
            if error.is_displayed():
                # Dodaję widoczne błędy do listy visible_error_notices
                visible_error_notices.append(error)

        # Sprawdzam, czy widoczny błąd jest tylko jeden
        self.assertEqual(len(visible_error_notices),1)
        # Sprawdzam poprawność treści błędu
        self.assertEqual(visible_error_notices[0].text, u"Nieprawidłowy adres e-mail")
        #sleep(1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
