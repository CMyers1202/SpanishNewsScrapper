from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

# I have it set up for the technology section; however, it can be set up for the home or any other section.
technology = 'https://elpais.com/tecnologia'
newspaper = 'https://elpais.com'

# Opens up the connection and grabs the requested webpage.
news_connection = uReq(technology)
pais_html = news_connection.read()
news_connection.close()

news_soup = soup(pais_html, "html.parser")

# Finds the articles on the main page.
containers = news_soup.find_all("article")

# Creates a .csv file of the articles.
news_articles = "newsLinks.csv"
f = open(news_articles, "w")

headers = "article, author, location, description, auther_link, article_link\n"

f.write(headers)

# Loops through all the articles on the technology page.
for container in containers:
	
	# Pulls the script from the associated article.
	script_data = json.loads(container.script.string)

	# Gets the data from the website.
	article_title = str(container.h2.text)
	writer_location = str(script_data['contentLocation'])
	description = str(script_data['description'])
	article_link = str(newspaper + container.a['href'])
	article_writer = str(script_data['author'][0]['name'])
	writer_link = str(script_data['author'][0]['sameAs'])

	if writer_location == "":
		writer_location = "None"

	# Writes all of the gathered data to the .csv file.
	f.write(article_title.replace(",", " ") + "," + article_writer + "," + writer_location + "," + description.replace(",", " ") + "," + writer_link + "," + article_link + "\n")

f.close
