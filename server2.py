from fastapi import FastAPI
from scrape import run as scrape_runner
from logger import trigger_log_save

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/abc")
def read_root():
    return {"data": [1,2,3]}


@app.post("/box-office-mojo-scraper")
def scrape_runner_view():
    trigger_log_save()
    scrape_runner()
    return {"data": [1,2,3]}
