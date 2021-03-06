import pandas as pd
import urllib.request
from collections import Counter

from newtest import recent_post_links, insta_link_details, insta_url_to_img

#Change post count to change amount of post downloaded
example_username_urls = recent_post_links('lilmiquela', post_count=30)
print(example_username_urls)
example_username_details = [insta_link_details(url) for url in example_username_urls]
example_username = pd.DataFrame(example_username_details)
example_username.head()
csv = example_username.to_csv('/Users/Anton/Desktop/Python/Instagram Scraper/example_username.csv')
print(csv)