import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_is_visible(browser):
    # Открываем страницу товара
    browser.get(link)
    # для визуального анализа страницы
    time.sleep(5)
    # поиск кнопки
    assert browser.find_element_by_css_selector("button.btn-add-to-basket"), "Button is none"
