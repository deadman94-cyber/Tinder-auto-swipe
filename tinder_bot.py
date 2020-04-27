from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        phone_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[1]/button')
        phone_btn.click()

        #switch to login window
        base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.window_handles[1])

        phone_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        phone_in.send_keys('9694073146')

        cont = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        cont.click()

        
        self.driver.switch_to_window(self.window_handles[1])

        allow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow.click()
        
        notify = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notify.click()

        sleep(5)

    def like(self):
        like = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like.click()



    def dislike(self):
        unlike = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        unlike.click()

    def autoswipe(self):
        while True:
            sleep(0.6)
            self.like()



bot = TinderBot()
bot.login()

