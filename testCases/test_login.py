import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=readConfig.getApplicationURL() #gets from the utilities file which connected to the ini file
    username=readConfig.getUsermail() #gets from the utilities file which connected to the ini file
    password=readConfig.getPassword() #gets from the utilities file which connected to the ini file

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info('****************** Test_001_Login******************')
        self.logger.info('****************** Verifing Home Page******************')
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info('****************** Home Page Title test Passed!******************')


        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error('****************** Home Page Title test Failed!!!******************')

            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info('****************** Verifing Login Test******************')
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title =='Dashboard / nopCommerce administration':
            assert True
            self.logger.info('****************** Login Test is Passed! ******************')
            self.driver.close()


        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error('****************** Login Test is Failed!!!******************')
            assert False




