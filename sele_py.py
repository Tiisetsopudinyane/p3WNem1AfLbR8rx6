from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://twitter.com/explore')

# sleep is for the page to load all the elements of the page
time.sleep(5)
searchBarPath=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input')
# delete any placeholder text in the seach_box if found
searchBarPath.send_keys(Keys.CONTROL+'a')
searchBarPath.send_keys(Keys.DELETE)

tweetss="request for startup"
searchBarPath.send_keys(tweetss)
searchBarPath.send_keys(Keys.ENTER)
time.sleep(3)
# Page is defined as Request For SartUp twitter Page
page=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[3]/div/div')
page.send_keys(Keys.ENTER)
driver.get('https://twitter.com/Request4Startup')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)

mytweets=driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div')

def get_tweets_info(mytweets, max_tweet=10):
    lst_tweets = [] # return list

    lst_tweets_driver = []
    for index in range(1,max_tweet):
        # name_of_user = mytweets.find_elements_by_xpath(f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[{index}]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]')
        elm_tweet = mytweets.find_elements_by_xpath(f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[{index}]')
        if(len(elm_tweet)>0):
            lst_tweets_driver.append(elm_tweet[0])
        
    for mytweet in lst_tweets_driver:
        # first tweet
        first=mytweet.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article')
        # username
        username=mytweet.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]/a/div/div[1]/div[1]/span/span').text
        # handlename
        handle=mytweet.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]/a/div/div[2]/div/span').text
        # time posted
        postTime=mytweet.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/a/time').text
        # tweet comment
        x=mytweet.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]').text
        # content
        y=mytweet.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]').text
        z=x+y
        # replies
        replies=mytweet.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div').text
        # retweets
        retweets=mytweet.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div').text
        # likes
        likes=mytweet.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div').text


        tweet=dict(username=username,handle=handle,postTime=postTime,z=z,replies=replies,retweets=retweets,likes=likes)
        lst_tweets.append(tweet)
        pass
    return lst_tweets
    pass
print(get_tweets_info(mytweets))