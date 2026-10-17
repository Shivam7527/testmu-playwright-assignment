from pages.base_page import BasePage


class SimpleFormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # the id "user-message" is reused on the page, so use the placeholder instead
        self.message_box = page.get_by_placeholder("Please enter your Message")
        self.show_button = page.get_by_role("button", name="Get Checked Value")

    def send_message(self, text):
        self.message_box.fill(text)
        self.show_button.click()

    def shown_message(self, expected_text):
        """Find the text that appeared in the right-hand 'Your Message' panel."""
        # ignore hidden copies of the text, only look at what a user can see
        output = self.page.get_by_text(expected_text).filter(visible=True).first
        output.wait_for(state="visible")
        return output.inner_text().strip()