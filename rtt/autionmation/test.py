import pytest

from selenium.webdriver.common.by import By



class TestClass :
    @pytest.mark.parametrize('user,pwd',
                             [('student','Password123'),('student','password123'),('Student','Password'),('student12','password123')])
    def test_login(self,user,pwd,setup):
        self.driver = setup
        self.driver.get('https://practicetestautomation.com/practice-test-login/')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@name="username"]').send_keys(user)
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys(pwd)
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        try:
            self.status = self.driver.find_element(By.XPATH,'//h1[@class="post-title"]').is_displayed()
            self.driver.close()

            assert self.status == True


        except:
            assert False