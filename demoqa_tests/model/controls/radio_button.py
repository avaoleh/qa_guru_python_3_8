from selene import have


def select_by_value(elements, text):
    elements.element_by(have.value(text)).element('..').click()