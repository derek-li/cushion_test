import requests
from bs4 import BeautifulSoup
from collections import Counter

class Capture:

	def capture_text(url):

		url_data = requests.get(url)
		parsed_content = BeautifulSoup(url_data.content, 'html.parser')

		for script in parsed_content(["script", "style", "link"]):
			script.extract()

		text = parsed_content.get_text()
		return text

	def get_most_frequent_words(text):
       
		words = Counter()
		
		words.update(text.lower().split())
		mostFrequentWords = words.most_common()
		return mostFrequentWords[:10]
        