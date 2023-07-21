from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
from creds import user, passwd

class Bot():

    links = []

    comments = ['Great post!', 'Awesome!', 'Amazing!']

    def __init__(self):
        self.login(user, passwd)
        self.like_comment_by_hashtag('tech')

    def login(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get('https://instagram.com/')
        sleep(6)
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(6)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
        sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        sleep(3)

    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        sleep(6) # Wait for page to full load
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        
        ### For Debug Only ###
        for link in links:
            href = post.get_attribute('href')
            links.append(href)
        
        print(links)
        self.driver.quit()
        ### For Debug Only ###
        
        # def condition(link):
        #     return '/p/' in link.get_attribute('href')
    
        # valid_links = list(filter(condition, links))

        # for i in range(5):
        #     link = valid_links[i].get_attribute('href')
        #     if link not in self.links:
        #         self.links.append(link)
        
        # for link in self.links:
        #     self.driver.get(link)
        #     # like
        #     sleep(3)
        #     self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
        #     sleep(5)
        #     # comment
        #     self.driver.find_element(By.NAME, 'RxpZH').click() 
        #     sleep(1)
        #     self.driver.find_element(By.XPATH, "//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
        #     sleep(1)
        #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

def main():
    while True:
        my_bot = Bot()
        #sleep(3600) # sleep for one hour

if __name__ == '__main__':
    main()