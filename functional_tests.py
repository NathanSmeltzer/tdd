from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        ##edith goes to check out online todo list
        browser.get('http://localhost:8000')

        #she notices the page title header meniions to-do lists
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!')

browser = webdriver.Firefox()





#she is inveted to ener a to-do item righ away

#hshe types 'buy peacock feathers' int oa text box (her hobby)

#when she hits enter, the page updateds and now th epage lists:
#"1: buy peakcock feathers" as an item in the tod-do list

#there is still atext box invieting her to add another item and she entereds "use peacock feathers to make a fly"

#the page updates again, and now shows both items on her list

#dith wonder wheterh the site will mremember her liste. Then she sees the site has gnerated a uqnie url for her - - with some explanatary text

#she fivitst that url - her to-do list is still there

#then she leaves

if __name__ == '__main__':
    unittest.main(warnings='ignore')
