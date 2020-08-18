import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from time import sleep
from selenium import webdriver
from tkinter import *

root = Tk()
driver = webdriver.Chrome(
    r"C:\Users\sandr\Desktop\Others\Html Css course\RedditBot\chromedriver.exe") #change path to chromedriver.exe


def Login():
    driver.get("https://www.reddit.com/login/")
    username = driver.find_element_by_xpath('//*[@id="loginUsername"]')
    username.send_keys(usernameID.get())

    password = driver.find_element_by_xpath('//*[@id="loginPassword"]')
    password.send_keys(passwordID.get())
    signIn = driver.find_element_by_xpath(
        '/html/body/div/div/div[2]/div/form/div/fieldset[5]/button')
    signIn.click()
    sleep(3)


def Check():
    driver.get('https://www.reddit.com/user/') #insert username here after "/"
    postari = driver.find_elements_by_class_name('imgq')
    for post in postari:
        clase = post.get_attribute("class")
        claseE = clase.split()
        idul = claseE[1]
        nrLikeuri = driver.find_element_by_xpath(
            '//*[@id="' + idul + '"]/div[1]/div[4]')
        timphtml = driver.find_element_by_xpath(
            '//*[@id="' + idul + '"]/div[2]/div[1]/p[2]/time')
        timpSplitted = timphtml.split()
        removeButton = driver.find_element_by_xpath(
            "//*[@id=" + idul + "]/div[2]/div[1]/ul/li[6]/form/span[1]/a")
        confirmDeleteButton = driver.find_element_by_xpath(
            "//*[@id=" + idul + "]/div[2]/div[1]/ul/li[6]/form/span[2]/a[1]")

        elTitle = driver.find_element_by_xpath(
            "//*[@id = " + idul + "]/div[2]/div/p[1]/a")

        if nrLikeuri < nrLikes.get() and (timpSplitted[1] != "hours" or timpSplitted[1] != "hours"):
            subredName = find_element_by_xpath(
                '//*[@id=' + idul + ']/div[2]/div[1]/p[2]/a[2]')
            title = find_element_by_xpath(
                '//*[@id=' + idul + ']/div[2]/div[1]/p[1]/a')
            photoLink = find_element_by_xpath(
                '//*[@id=' + idul + ']/div[2]/div[1]/p[1]/a').get_attribute("data-href-url")
            removeButton.click()
            confirmDeleteButton.click()
            sleep(2)
            Post(subredName, title, photoLink)


def Post(sub, title, picLink):
    driver.get("https://www.reddit.com/r/" + sub + "/submit")
    titleTextArea = driver.find_element_by_xpath(
        '//*[@id="title-field"]/div/textarea')
    titleTextArea.send_keys(title)
    URLTextArea = driver.find_element_by_xpath(
        '//*[@id="url"]')
    URLTextArea.send_keys(picLink)
    submitBTN = driver.find_element_by_xpath(
        '/html/body/div[4]/form/div[4]/button')
    submitBTN.click()
    sleep(5)


def StartBot():
    subreddits = subredd.get().split(", ")
    Login()
    sleep(5)
    for s in subreddits:
        Post(s, title.get(), link.get())
    while True:
        sleep(3600)
        Check()


u = Label(root, text="Username")
u.pack()
usernameID = Entry(root, width=25)
usernameID.pack()
p = Label(root, text="Passsword")
p.pack()
passwordID = Entry(root, width=25, show="*")
passwordID.pack()
t = Label(root, text="Title")
t.pack()
title = Entry(root, width=25)
title.pack()
l = Label(root, text="Link (.JPG/.PNG ending)")
l.pack()
link = Entry(root, width=50)
link.pack()
s = Label(root, text="Subreddit List")
s.pack()
subredd = Entry(root, width=25)
subredd.pack()
nrLikeuriMinim = Label(root, text="Nr. Like-uri Minime")
nrLikeuriMinim.pack()
nrLikes = Entry(root, width=25)
nrLikes.pack()

postBtn = Button(root, text="Start Posting", command=StartBot)
postBtn.pack()

root.mainloop()
