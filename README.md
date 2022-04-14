# ScrapeOps Python Request SDK: For Scraping Monitoring, Statistics and Alerts.
The ScrapeOps Python Requests SDK is an extension for your python requests based scraping that gives you all the scraping monitoring, statistics, alerting and data validation you will need straight out of the box. 

Just import it into your python project, start using our requests wrapper and the SDK will automatically monitor your scrapers and send your logs to your scraping dashboard.

**Full documentation can be found here:** [ScrapeOps Documentation](https://scrapeops.io/docs/intro)


![ScrapeOps Dashboard Demo](https://github.com/ScrapeOps/scrapeops-docs/blob/main/assets/scrapeops-hero-demo.jpg)


## :computer: Demo
[:link: ScrapeOps Dashboard Demo](https://scrapeops.io/app/login/demo)

## :star: Features
<details>
<summary>View features</summary>

- ** Job Stats & Visualisation**
  - :chart_with_upwards_trend: Individual Job Progress Stats
  - :bar_chart: Compare Jobs versus Historical Jobs
  - :100: Job Stats Tracked
    - :white_check_mark: Pages Scraped & Missed
    - :white_check_mark: Items Parsed & Missed
    - :white_check_mark: Item Field Coverage
    - :white_check_mark: Runtimes
    - :white_check_mark: Response Status Codes
    - :white_check_mark: Success Rates & Average Latencies
    - :white_check_mark: Errors & Warnings
    - :white_check_mark: Bandwidth

- **Health Checks & Alerts**
  - :male_detective: Custom Spider & Job Health Checks 
  - :package: Out of the Box Alerts - Slack (More coming soon!)
  - :bookmark_tabs: Daily Scraping Reports

 - **Proxy Monitoring (Coming Soon)**
    - :chart_with_upwards_trend: Monitor Your Proxy Account Usage
    - :chart_with_downwards_trend: Track Your Proxy Providers Performance
    - :bar_chart: Compare Proxy Performance Verus Other Providers

</details>

## :rocket: Getting Started
You can get the ScrapeOps monitoring suite up and running in **3 easy steps**.

#### #1 - Install the ScrapeOps SDK:

`pip install scrapeops-python-requests`


#### #2 - Import & initialize the ScrapeOps logger</h3>
Import then initialize the Scrapeops logger and add your ``API key``.

```
  from scrapeops_python_requests.scrapeops_requests import ScrapeOpsRequests

  scrapeops_logger =  ScrapeOpsRequests(
                        scrapeops_api_key='API_KEY_HERE', 
                        spider_name='SPIDER_NAME_HERE',
                        job_name='JOB_NAME_HERE',
                      )
```


#### #3 -  Initialize the ScrapeOps Python Requests Wrapper
The last step is to just override the standard python requests with our requests wrapper.

Our wrapper uses the standard python request library but just provides a way for us to monitor the requests as they happen. 

Please only initialize the requests wrapper once near the top of your code. 

`requests = scrapeops_logger.RequestsWrapper()`



#### Simple Example:
We've added a simple example so you can see how you can add it to an existing project.

```
from scrapeops_python_requests.scrapeops_requests import ScrapeOpsRequests


## Initialize the ScrapeOps Logger
scrapeops_logger = ScrapeOpsRequests(
    scrapeops_api_key='API_KEY_HERE', 
    spider_name='DemoSpider',
    job_name='Test1',
    )


## Initialize the ScrapeOps Python Requests Wrapper
requests = scrapeops_logger.RequestsWrapper() 

urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        'http://quotes.toscrape.com/page/3/',
        'http://quotes.toscrape.com/page/4/',
        'http://quotes.toscrape.com/page/5/',
        ]


for url in urls:
    response = requests.get(url)

    item = {'test': 'hello'}

    ## Log Scraped Item
    scrapeops_logger.item_scraped(
        response=response,
        item=item
    )
    

```


#### Done!
That's all. From here, the ScrapeOps SDK will automatically monitor and collect statistics from your scraping jobs and display them in your [ScrapeOps dashboard](https://scrapeops.io/app/dashboard). 