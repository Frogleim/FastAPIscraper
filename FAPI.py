from scraper import Scraper
from fastapi import FastAPI


app = FastAPI()
quotes = Scraper()
quotes.scrapdata('life')

@app.get('/{cat}')
async def read_item(cat):
    return quotes.scrapdata(cat)

