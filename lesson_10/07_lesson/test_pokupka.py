import allure
import pytest
from selenium import webdriver
from pokupkapage import ShoppingCartPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.severity("normal")
@allure.description("Проверка формы покупки, для авторизованного пользователя")
@allure.title("Тестирование формы покупки")
def test_shopping_cart(driver):
    page = ShoppingCartPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")

    with allure.step("Проверка id товара"):
        for product_id in ["sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie"]:
            page.add_product_to_cart(product_id)

    page.go_to_cart()
    page.proceed_to_checkout()
    page.fill_checkout_form("Павел", "Дьяконов", "420087")

    with allure.step("Проверка итоговой цены"):
        assert page.get_total_price() == "Total: $58.29"
