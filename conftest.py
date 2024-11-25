import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    #parser.addoption("--url", "-U", action="store", default="http://localhost/", help="choose your url")

# задаем браузер через cli
@pytest.fixture(autouse=True)
def driver(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1200")
        #options.add_argument('--headless')
        #options.page_load_strategy= 'eager'
        driver = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{request.param} is not supported!")
    #driver.get(request.config.getoption("--url"))
    request.cls.driver = driver
    request.addfinalizer(driver.close)
    

# задаем браузеры через параметры фикстуры
@pytest.fixture(params=["chrome", "firefox"])
def parametrize_browser(request):
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(20)
    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))

    return driver
