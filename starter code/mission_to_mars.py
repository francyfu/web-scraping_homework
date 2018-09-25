
# coding: utf-8

# In[76]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt


# In[77]:





# In[78]:

browser = Browser("chrome", executable_path="/usr/local/bin/chromedriver", headless=True)

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="/usr/local/bin/chromedriver", headless=True)
    
    listings = {}
    listings["title"], listings["text"] = mars_news(browser)
    #listings["mars_weather"] = twitter_weather(browser)
    listings["link"] = featured_image(browser)

    # twitter_weather(browser)
    # hemispheres(browser)
    #print(listings)


# In[79]:


# browser = Browser("chrome", executable_path="/usr/local/bin/chromedriver", headless=True)


# In[80]:

def mars_news(browser):
    
    # return news_title, news_p
    
   # browser = init_browser()
    #listings = {}
    
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    news_title = soup.find("div", class_="content_title").a.text
    news_p = soup.find("div", class_="article_teaser_body").text

    #listings["news_title"] = news_title
    #listings["news_p"] = news_p
    return news_title, news_p


# In[81]:


# mars_news(browser)


# In[82]:


def featured_image(browser):

    # Find and click the full image button
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    full_image = browser.find_by_id("full_image")
    full_image.click()
    
    #info = browser.find_by_class("button")
   # info.click()
    browser.is_element_present_by_text('more info', wait_time=1)
    
    info = browser.find_link_by_partial_text('more info')
    info.click()
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #images = soup.find_all('', class_='text')
    
    #print(soup)
    featured_image = soup.find("figure", class_="lede").a["href"]

    link = "https://www.jpl.nasa.gov" + featured_image
    return link
    # listings["link"] = link
    # listings["news_p"] = soup.find("div", class_="article_teaser_body").get_text()
    
    # Use the base url to create an absolute url
   

    # return img_url

# featured_image(browser)


# In[83]:


def twitter_weather(browser):
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    
    #info = browser.find_by_class("button")
   # info.click()
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #images = soup.find_all('', class_='text')
    
    #print(soup)
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    link = soup.find("a", class_="lede")
    print(link)
    return link

    #print(mars_weather)
    # listings["news_p"] = soup.find("div", class_="article_teaser_body").get_text()
    
    # Use the base url to create an absolute url
   

    # return img_url
    # listings["mars_weather"] = mars_weather
# twitter_weather(browser)


# In[84]:


### Mars Facts

#Visit the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

# Use Pandas to convert the data to a HTML table string.


# In[103]:




def mars_facts():
    url = 'http://space-facts.com/mars/'
    df = pd.read_html(url)[0]
    df.columns=["a","b"]
    df.set_index("a",inplace=True)
    df
    df_html = df.to_html()
    df_html
# mars_facts()

       
    # Add some bootstrap styling to <table>
    # return df


# In[104]:


def hemispheres(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    hemisphere_image_urls = []
    results = soup.find('div', class_='result-list')
    items = results.find_all('div', class_='item')
    for item in items:
        title=[]
        result = item.find('div', class_='description')
        text = result.a.text
        title.append(text)
        
        url=[]
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
        
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        
    images1 = soup.find('div', class_='downloads').find('ul').find('li')
    image1 = images1.a['href']
    url.append(image1)
    browser.click_link_by_partial_text('Back')
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
        
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        
    images2 = soup.find('div', class_='downloads').find('ul').find('li')
    image2 = images2.a['href']
    url.append(image2)
    browser.click_link_by_partial_text('Back')
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
        
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        
    images3 = soup.find('div', class_='downloads').find('ul').find('li')
    image3 = images3.a['href']
    url.append(image3)
        
    browser.click_link_by_partial_text('Back')
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
        
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        
    images4 = soup.find('div', class_='downloads').find('ul').find('li')
    image4 = images4.a['href']
    url.append(image4)
        
    hemisphere_image_urls.append({'title': title[0], 'img_url': url[0]})
    #print(hemisphere_image_urls)  
    listings["hemispheres_info"] = hemisphere_image_urls 

# hemispheres(browser)


# In[89]:


# hemispheres_info.append([{'title': title[0], 'img_url': url[0]},{'title': title[1], 'img_url': url[1]},{'title': title[2], 'img_url': url[2]},{'title': title[3], 'img_url': url[3]}])
# print(hemispheres_info)

scrape_all()