from requests_html import HTMLSession

class Scraper():
    def scrapdata(self, tag):
        url =f'https://quotes.toscrape.com/tag/{tag}'
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

        qlist = []
        quotes = r.html.find('div.quote')

        for q in quotes:
            item ={
            'text':q.find('span.text', first = True).text.strip(),
            'author': q.find('small.author',first = True).text.strip()
            }
            print(item)
            qlist.append(item)

        return qlist


quotes = Scraper()
quotes.scrapdata('life')