from pages.playground_page import PlaygroundPage
from pages.input_form_page import InputFormPage

SUCCESS_TEXT = "Thanks for contacting us, we will get back to you shortly."

customer = {
    "name": "Rohit Verma",
    "email": "rohit.verma@example.com",
    "password": "Test@1234",
    "company": "Verma Testing Labs",
    "website": "https://www.vermatesting.com",
    "country": "United States",
    "city": "Austin",
    "address1": "21 Congress Avenue",
    "address2": "Suite 400",
    "state": "Texas",
    "zip": "73301",
}


def test_input_form_validation_and_submit(page):
    home = PlaygroundPage(page)
    home.open_playground()
    home.open_demo("Input Form Submit")

    form = InputFormPage(page)

    # submitting an empty form should complain about the required fields
    form.click_submit()
    error = form.validation_text()
    assert "fill" in error.lower(), f"unexpected validation text: {error!r}"

    # now fill everything properly and submit
    form.fill_form(customer)
    form.click_submit()

    assert form.success_msg.is_visible()
    assert SUCCESS_TEXT in form.success_msg.inner_text()
