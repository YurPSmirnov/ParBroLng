import time
from selenium.webdriver.common.by import By

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def is_element_present(browser, how, what):
    try: browser.find_element(by=how, value=what)
    except NoSuchElementException: return False
    return True

def test_should_see_button_add_to_basket(browser,pause_time):
    browser.get(link)
    #time.sleep(30)
    # Для добавления паузы необходимо при запуске добавить опцию --pause
    # Например: pytest --language=fr --pause=30 test_items.py
    #  Скопировано с достоинством у @Дмитрий_Сивков
    if pause_time:
        print(f'Включена автопауза на {pause_time} секунд')
        time.sleep(int(pause_time))
    assert is_element_present( browser, By.CSS_SELECTOR, "button.btn-add-to-basket"), "No Add_to_basket button"
