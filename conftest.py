import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,help="Choose language: ru,en-gb,fr,es")
    parser.addoption('--pause', action='store', default=0, help="Включение паузы после загрузки")
    


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        language = request.config.getoption("language")
        options = webdriver.chrome.options.Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def pause_time(request):
    pause_mode = request.config.getoption("pause")
    return pause_mode
