"""
A simple selenium test example written by python
"""

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Find and click Repositories tab"""
        try:
            self.driver.get('https://github.com/quan-vu')
            el_tabs = self.driver.find_elements_by_class_name('UnderlineNav-item')
            for el in el_tabs:
                if el.text and el.text.strip() == 'Repositories':
                    print('Found: %s' % el.text)
                    el.click()
                    print('Sleep 30 seconds for tab Repositories is loaded')
                    sleep(30)
                    break
            self.driver.save_screenshot('test_github_profile_repositories.png')
        except NoSuchElementException as ex:
            self.fail(ex.msg)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)