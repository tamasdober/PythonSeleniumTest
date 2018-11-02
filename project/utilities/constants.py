import os

base_path = os.environ.get('base_path', 'undefined_base_path')
BASE_URL = 'http://' + base_path + '/console/'
CHROME_DRIVER = '/usr/local/bin/chromedriver'
