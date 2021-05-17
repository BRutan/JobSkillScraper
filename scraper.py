
import json
import requests
from nltk import stopwords

ip_address = ''

def glassdoor_query(keywords):
    """
    * Query glassdoor API.
    """
    # t.p: partner Id, 
    query = ['http://api.glassdoor.com/api/api.htm?v=1.1&format=json,']
    query.append['&t.p=%s&t.k=fz6JLNDfgVs&action=jobs&q=%s&userip=%s&useragent=Mozilla/%2F4.0'
    
    result = requests.get(query)

    
    

def scrape_descriptions(keywords):
    """
    * Scrape job descriptions from target website.
    """
    pass
    
