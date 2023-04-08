from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

class WebSurfer:
    # Constructor
    def __init__(self):
        # Configure headless webdriver
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Instantiate webdriver w/ specified options
        self.webdriver = webdriver.Chrome(chrome_options=options)

    # Abstract scraper usage of webdriver away from user
    def get_page(self, url):
        try:
            # Navigate to webpage
            self.webdriver.get(url)
            print(f'Obtained page source for : {url}')

            # Return page HTML
            html = self.webdriver.page_source
            
            # Sleep thread to prevent rate-limiting
            print('Thread sleeps for 5 seconds to avoid PFR rate limiting')
            time.sleep(5)

            return html
        except Exception as e:
            print(e)

            return ''
