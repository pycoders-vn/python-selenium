"""
A simple crawler example use selenium written by python
"""
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class GitHubCrawler():

    def __init__(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    def stop(self):
        """Stop web driver"""
        self.driver.quit()
        print("Stop web driver")

    def crawl(self):
        print("Crawling a github profile...")
        try:
            data = {
                'github': 'https://github.com/quan-vu'
            }

            self.driver.get(data['github'])
            
            el_fullname = self.driver.find_element_by_class_name('vcard-fullname')
            if el_fullname:
                data['fullname'] = el_fullname.text

            el_bio = self.driver.find_element_by_class_name('user-profile-bio')
            if el_bio:
                data['bio'] = el_bio.text

            el_avatar = self.driver.find_element_by_class_name('avatar')
            if el_avatar:
                data['avatar'] = el_avatar.get_attribute('src')
            
            print("============================")
            print(json.dumps(data, indent=4))
            print("============================")

        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    crawler = GitHubCrawler()
    crawler.crawl()
    crawler.stop()