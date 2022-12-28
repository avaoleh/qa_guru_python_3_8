from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model.controls import drop_down, modal, date_picker, radio_button, check_boxes
from demoqa_tests.utils import path_to_file


state = browser.element('#state')

def given_opened():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def set_name(value):
    browser.element('#firstName').type(value)


def set_last_name(value):
    browser.element('#lastName').type(value)


def set_email(value):
    browser.element('#userEmail').type(value)


def set_gender(gender):
    # browser.all('[for^=gender-radio]').by(
    #     have.exact_text(gender)
    # ).first.click()
    radio_button.select_by_value(browser.all('[name=gender]'), gender)


def set_phone_number(value):
    browser.element('#userNumber').type(value)


def set_date_of_birth(*, month, year, day):
    browser.element('#dateOfBirthInput').click()
    date_picker.select_date(month, year, day)


def upload_picture(value):
    # browser.element('#uploadPicture').send_keys(os.path.abspath(value))
    path_to_file.create_path('#uploadPicture', value)


def set_address(value):
    browser.element('#currentAddress').type(value)


def set_hobbies(*text):
    # browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()
    check_boxes.select(browser.all('[for^=hobbies-checkbox]'), *text)


def set_subjects(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def set_state(value):
    drop_down.select(browser.element('#state'), value)


def set_city(value):
    drop_down.select(browser.element('#city'), value)


def scroll_to_bottom():
    state.perform(command.js.scroll_into_view)


def submit():
    # browser.element('#submit').perform(command.js.click)
    browser.element('#submit').press_enter()


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
