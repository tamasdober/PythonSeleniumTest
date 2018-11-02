class BasePage:
    def __init__(self, driver, base_path):
        self.base_path = base_path
        self.driver = driver
        # base_path = environ.get("base_path")
        print("base_path was: {}".format(base_path))

    @property
    def url(self):
        return "http://{}/console".format(self.base_path)

    def load(self):
        self.driver.get(self.url)
