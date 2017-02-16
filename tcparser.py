from lxml import html
import requests
import csv

def writeToCsv(articleResults):
		"""Write articleResults to a CSV file.
		articleResults in an array containing information about an article's title, URL,
		and if applicable, the subject company's name and website URL.
    """
		with open('output.csv', 'wb') as csvfile:
				writer = csv.writer(csvfile, escapechar='"', quoting=csv.QUOTE_MINIMAL)

				for row in articleResults:
						writer.writerow([unicode(s).encode("utf-8") for s in row])

def getArticleInfo(articleUrl):
		"""Gets the article's title, URL, and if applicable, the subject company's name and
		website URL. Note that this function will only work for www.techcrunch.com as of 2/15/2017.
		Returns [title, articleUrl, companyName, website]
    """
		article = requests.get(articleUrl)
		articleTree = html.fromstring(article.content)
		title = articleTree.xpath('//h1/text()')
		if title:
				title = title[0].strip()
		website = "n/a"
		companyName = "n/a"

		websiteExists = False
		companyCard = articleTree.xpath('//li[@class="data-card crunchbase-card active"]')
		if companyCard:
				companyCard = companyCard[0]
				for element in companyCard.iter("strong"):
						if element.text == "Website":
								span = element.getnext()
								a = span[0]
								website = a.text
								websiteExists = True
								break
				
				if websiteExists:
						companyName = articleTree.xpath('//a[@class="cb-card-title-link"]/text()')
						if companyName:
								companyName = companyName[0].strip()
		
		return [title.encode('utf-8'), articleUrl, companyName, website]

def getArticleUrls(websiteUrl, xpathsToArticleLinks):
		"""Gets all article URLs from the websiteUrl's first page by using the list of XPaths 
		provided by xpathsToArticleLinks.
		Returns all of the article URLs found
    """
		page = requests.get(websiteUrl)
		tree = html.fromstring(page.content)

		urls = []
		for xpath in xpathsToArticleLinks:
				urls += tree.xpath(xpath)
		return urls

def main():
		articleResults = []
		urls = getArticleUrls("https://techcrunch.com", ['//h2[@class="post-title"]/node()/@href', '//li[@class="plain-item"]/node()/@href'])
		
		for url in urls:
				articleResults.append(getArticleInfo(url))

		writeToCsv(articleResults)

if __name__ == "__main__":
    main()