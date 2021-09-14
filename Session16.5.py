"""
  in this program,we take data from another website using user defined package
  requests and built-in package json
  we have installed requests .
  steps to install- 1. open google chrome,search pypi ,open the website
                    2. search requests
                    3. when the page opens, u see there are various versions of requests
                    4. click on the 1st one,u will see 'pip install requests' written on the top
                    5. then come to pycharm,open terminal,write 'pip install requests'
                    6. it will install you the requests
                    7. then u can import requests.otherwise it will give u an error,if u try to import that.


     When u see the data present in this url,it seems like dict but when u print the type,it will give u str
     that means it is JSON
"""

import requests
import json

api_key = "31c21508fad64116acd229c10ac11e84"
url = "https://newsapi.org/v2/top-headlines?country=in&apiKey={}".format(api_key)

print(url)

# response is a reference variable
response = requests.get(url)
# print(response)
# print(response.text)    # .text means it will print u the data in the url
# print(type(response.text)) # JSON (java Script Object Notation)

# converts the response.text data type(str) to dict
data = json.loads(response.text)
# print(data)
print(type(data))

print("TOTAL RESULTS:", data['totalResults'])
articles = data['articles']

for article in articles:
    print(article['author'])
    print(article['title'])
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print()