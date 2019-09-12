# Web-Scraping Hackmageddon

## From gathering data to machine learning - Insights into the world of Cyber Attacks by Scraping Hackmageddon

## Blog Post: https://nycdatascience.com/blog/student-works/web-scraping-hackmageddon/

The global cost of cyber crime for 2015 was $500 billion (BOLD NUMBER).
That’s more than 5 times Google’s yearly cash flow of 90 billion dollars.
And that number is set to grow tremendously, to around 2 trillion dollars by 2019.

The purpose of this excercise was to successfully scrape Hackmageddon's website to explore the types of attacks used by cybercriminals to drive up such a huge figure and help you understand how they work and affect you.Hackmageddon is a website that has massive data on list of events of cyber attacks dating back to 2011

* Folder Hackmageddon - contains the spyder to scrape Hackmageddon website. Copy this folder and paste it in your directory. 
    * How to deploy spyder
         * first you have to download scrapy tool with this command `pip install scrapy==1.5.0`.
         * Type this command in your command prompt to deploy spyder `scrapy crawl hackmageddon`. Make sure you're                    in the top level of the project's directory, the one contains scrapy.cfg file.
* Hackmageddon.ipynb - IPython notebook contains code to visualize the scraped data and to conduct a text mining using     natural language processing and unsupervised learning.
* cluster.html - contains interactive d3.js visualization cluster map 
* cyber_attacks.pdf - contains a presentation outlining the process and findings.
