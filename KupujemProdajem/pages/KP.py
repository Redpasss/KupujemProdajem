from lib.base_page import BasePage
from lib.base_element import BaseElement
from selenium.webdriver.common.by import By
from lib.locator import Locator


class KP(BasePage):
    url = "https://www.kupujemprodajem.com/login?data[remember]=0"

    def element(self, loc):
        locator = Locator(By.XPATH, loc)
        return BaseElement(driver=self.driver, locator=locator)


