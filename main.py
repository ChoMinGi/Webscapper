import os
import csv
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_wwr, get_sof
from exporter import save_to_file


app = Flask("jobscrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingkJobs = db.get(word)
        if existingkJobs:
            jobs = existingkJobs
        else:
            jobs = get_wwr(word)
            db[word] = jobs
    else:
        return redirect("/")

    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           job_result=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("job.csv", download_name='SearchingResult.csv', as_attachment=True)
    except:
        return redirect("/")


app.run(host="0.0.0.0")
