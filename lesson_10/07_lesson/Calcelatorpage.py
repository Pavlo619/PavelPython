import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.result_locator = (By.CSS_SELECTOR, "#result")

    @allure.step("Открытие формы")
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Выставление задержки")
    def set_delay(self, delay):
        delay_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_field.clear()
        delay_field.send_keys(delay)

    @allure.step("Проверка работы кнопки")
    def click_button(self, button_text):
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']"))
        )
        button.click()

    @allure.step("Текст с результатом")
    def get_result_text(self):
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(self.result_locator, "15")
        )
        return self.driver.find_element(*self.result_locator).text
