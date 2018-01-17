from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

def main():
	# Fill in with url of page which is to be scraped
	url = "https://cryptoweekly.co/100/"

	# Retreives and parses page html
	client = urlopen(url)
	pageHtml = client.read()
	pageSoup = soup(pageHtml, "html.parser")

	# Parsed html
	print(pageSoup)
	
	client.close()


if __name__ == '__main__':
	main()