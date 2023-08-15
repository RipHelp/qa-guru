from selene import browser, have, command
from os import path


def test_form_demoqa(browser_management):
    browser.open("/automation-practice-form")

    # Заполнение формы
    browser.element("#firstName").perform(command.js.type('Vasya'))
    browser.element("#lastName").perform(command.js.type('Pupkin'))
    browser.element("#userEmail").perform(command.js.type('qa-engineer@example.ru'))
    browser.element(".custom-radio [for=gender-radio-1]").click()
    browser.element("#userNumber").perform(command.js.type('8005553535'))
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select").send_keys("1953")
    browser.element(".react-datepicker__month-select").send_keys("March")
    browser.element("[aria-label='Choose Thursday, March 5th, 1953']").click()
    browser.element('#subjectsInput').send_keys('Computer Science').press_tab()
    browser.all("#hobbiesWrapper .custom-control-label").element_by(have.exact_text('Sports')).click()
    browser.all("#hobbiesWrapper .custom-control-label").element_by(have.exact_text('Reading')).click()
    browser.element('#uploadPicture').send_keys(path.abspath("img/img1.png"))
    browser.element("#currentAddress").perform(command.js.type('Russia, Moscow'))
    browser.element('#state').click()
    browser.all('[id^=react-select]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select]').element_by(have.exact_text('Karnal')).click()

    browser.element("#submit").click()

    #Проверка формы
    browser.element('[class="modal-title h4"]').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text('Vasya Pupkin'))
    browser.element('.table-responsive').should(have.text('qa-engineer@example.ru'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('8005553535'))
    browser.element('.table-responsive').should(have.text('05 March,1953'))
    browser.element('.table-responsive').should(have.text('Computer Science'))
    browser.element('.table-responsive').should(have.text('Sports, Reading'))
    browser.element('.table-responsive').should(have.text('img1.png'))
    browser.element('.table-responsive').should(have.text('Russia, Moscow'))
    browser.element('.table-responsive').should(have.text('Haryana Karnal'))

    browser.element("#closeLargeModal").click()