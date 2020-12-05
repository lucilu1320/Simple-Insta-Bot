from selenium import webdriver
import os
import time

import configparser




class InstagramBot:

    """
    Initializes an instance of the Instagram clas. Call the log in method to authenticate an user with IG!
    Args:
        username:str: The Instagram username for a user
        password:str: The Instagram password for a user

    Attributes:
        driver:Selenium.webdriver.Firefox(): The Firefox driver that is used to automate browser actions
        Note: You can use chrome drivers too for this automation, if you get any errors or problems
        while installing chrome drivers or something else feel free to 
        open an issue wiithout any hesitation.
        Thank you!
        """
    

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.base_url = 'https://www.instagram.com' 
        self.login()

            

    def login(self):
        
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        
        self.driver.find_element_by_xpath("//div[contains(text(),'Log In')]").click()
        time.sleep(5)


   
    """
        Navigates the user page
    
    """

    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url, user))

        
    """
        Navigates the follow page and clicks 
    """
    def follow_user(self, user):
        self.nav_user(user)

        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0]
        
        follow_button.click()
            
    

if __name__ == '__main__':


    config_path ='./config.ini'

    cparser = configparser.ConfigParser()
    cparser.read(config_path)
    username = cparser['AUTH']['USERNAME']
    password = cparser['AUTH']['PASSWORD']

    ig_bot = InstagramBot(username, password)
    ig_bot.nav_user('@username_you_wanna_navigate')
    ig_bot.follow_user('@username_you_wanna_follow')

    
    
