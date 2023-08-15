from selene.support.shared import browser
from selene import be, have

def test_google_search(set_windows_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_google_search_some(set_windows_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('asdasdasdasdsadasdasdasd123123123').press_enter()
    browser.element('[id="botstuff"]').should(have.text('Страницы, содержащие все слова запроса, не найдены.'))