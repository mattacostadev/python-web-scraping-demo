from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER as selenium_logger
from urllib3.connectionpool import log as url_lib_logger

import logging
import time

selenium_logger.setLevel(logging.NOTSET)
url_lib_logger.setLevel(logging.NOTSET)

class WebSurfer:
    # Constructor
    def __init__(self):
        # Configure headless webdriver
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')

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
