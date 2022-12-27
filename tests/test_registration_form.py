from demoqa_tests.model.pages import registration_form

def test_submit_registration_form():
    #GIVEN
    registration_form.given_opened()

    # WHEN
    registration_form.set_name('Test')
    registration_form.set_last_name('Testov')
    registration_form.set_email('test@test.com')
    registration_form.set_gender('Male')
    registration_form.set_phone_number('1234567890')
    registration_form.set_date_of_birth(day='27', month='7', year='1997')
    registration_form.set_subjects('Computer Science')
    registration_form.set_hobbies('Reading')
    registration_form.upload_picture('resources/photo.png')
    registration_form.set_address('SPB 61')
    registration_form.scroll_to_bottom()
    registration_form.set_state('NCR')
    registration_form.set_city('Delhi')

    registration_form.submit()

    # THEN
    registration_form.should_have_submitted(
        [
            ('Student Name', 'Test Testov'),
            ('Student Email', 'test@test.com'),
            ('Gender', 'Male'),
            ('Mobile', '1234567890'),
            ('Date of Birth', '27 July,1997'),
            ('Subjects', 'Computer Science'),
            ('Hobbies', 'Reading'),
            ('Picture', 'photo.png'),
            ('Address', 'SPB 61'),
            ('State', 'NCR Delhi'),
        ],
    )