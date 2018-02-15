from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def amazonScraper(amazon_id):

	full_url = "https://www.amazon.com/dp/"+amazon_id

	url = Request(full_url)

	html = urlopen(url)

	bsobj = BeautifulSoup(html, "html.parser" )

	title = bsobj.find("span", {"id":"productTitle"})

	print( title.get_text().replace("\n","") )

	price = bsobj.find("span",{"id":"priceblock_ourprice"})

	print(price.get_text())

	description = bsobj.find("div", {"id":"productDescription"}).find("p")

	print( description.get_text().replace("\n","") )



	
amazonScraper("B016S5PYIS")