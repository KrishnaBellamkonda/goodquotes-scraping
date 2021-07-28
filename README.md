# goodquotes-scraping
### Description
*This project scrapes data from good quotes website.* 

### Setup 
* Install Scrapy
* Clone the repository 
* You can run `scrapy crawl goodreads -o data/filename.[csv/json]` to scrape and download the data


### Functionality 
This spider obtains the goodreads website and scrapes the quote, author name and tags  from the website. A preprocessing pipeline processes the data and 
saves the data in the requried format. 

### Modules 
* scrapy 
* os
* json

### Data Sample
```
{
"text": "You know you're in love when you can't fall asleep because reality is finally better than your dreams.", 
"author": "Dr. Seuss", 
"tags": "attributed-no-source,dreams,love,reality,sleep"
},

```


### Sources
* Scrapy installation (https://docs.scrapy.org/en/latest/intro/install.html)
* GoodReads Quotes website (https://www.goodreads.com/quotes)

