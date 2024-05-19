#imports needed, bs4, requests and lxml
import pandas as pd
from bs4 import BeautifulSoup
import requests

#Url used to test the function below
#url = ("https://webscraper.io/test-sites/tables/tables-without-thead")

#A function that performs the web scraping called 'web_scraper'
def web_scraper(url):

    #scraped_text is the entired scraped webpage
    scraped_text = requests.get(url).text
    #beautiful soup instance 
    soup = BeautifulSoup(scraped_text, 'html.parser')
    #from soup find all the tr elements 
    tr_raw = soup.find_all('tr')

    table_headers = []
    #extracting th text from the th element tags and removing whitespace and delimiters
    for th in tr_raw:
        th_text = [th.get_text().strip() for th in th.find_all('th')]
        if any(th_text):
            table_headers.append(th_text)
    #new list created for storing table_rows
    table_rows = []
    #going through each tr element and appending text from td elememts nested inside of them to the table_rows list  
    for tr in tr_raw:
        row_data = [td.get_text().strip() for td in tr.find_all('td')]
        if any(row_data):
            table_rows.append(row_data)

    df = pd.DataFrame(table_rows, columns=table_headers)
    
    html_table = df.to_html(index=False)
    
    return html_table

        #To test the function
        #Prints out each of the lists containing the newly clean and structured data 
    
    #print('Table Headers:\n', table_headers)
    #print('Table Rows:\n', table_rows)

#web_scraper("https://webscraper.io/test-sites/tables/tables-without-thead")
