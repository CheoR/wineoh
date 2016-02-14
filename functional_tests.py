from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_enter_a_review_and_retrieve_it_later(self):
        # Sara has heard about a cool new on-line wine app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the funny page title
        self.assertIn('Winoh', self.browser.title)
        self.fail('Finish the test!')

    # She is invited to enter add a review straight away

    # She types "I like red wines" into a text box (Sara's hobby
    # is drinking.)

    # When she hits add, the page updates, and now the page includes her wine of
    # choice and a brief overview of its review
    # "Red wines make me happy"
    # and its rating by her (as a member)

    # There is still a text box inviting her to add another review. She
    # enters "White wines are good too" (Sara is very methodical)

    # The page updates again, and now shows both of her reviews (if 'read more' 
    # is expanded)

    # Sara wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.

    # She visits that URL - her reviews still there.

    # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')