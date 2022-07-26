import requests
from bs4 import BeautifulSoup


def get_wwr(word):
    job_result = []
    job_request = requests.get(
        f"https://weworkremotely.com/remote-jobs/search?term={word}")
    job_soup = BeautifulSoup(job_request.text, "html.parser")
    main = job_soup.find("div", {"id": "job_list"})
    sections = main.find_all("section", {"class": "jobs"})
    for section in sections:
        categorys = main.find_all("li", {"class": "feature"})
        for category in categorys:
            name = category.find("span", {"class": "company"}).text
            title = category.find("span", {"class": "title"}).text
            local = category.find("span", {"class": "region company"}).text
            pre_time = category.find_all("span", {"class": "company"})
            time = pre_time[1].text
            pay = "Negotiation"
            date = category.find("span", {"class": "date"})
            pre_link = category.find_all("a")
            link = pre_link[1].attrs["href"]
            if date:
                date = date.text
            else:
                date = "Limitless"
            jobs = {
                "name": name,
                "place": local,
                "title": title,
                "time": time,
                "pay": pay,
                "date": date,
                "link": f"https://weworkremotely.com/{link}"
            }
            job_result.append(jobs)
    print(job_result)
    return job_result


def get_sof(word):
    job_result = []
    job_request = requests.get(
        f"https://stackoverflow.com/jobs/companies?q={word}")
    job_soup = BeautifulSoup(job_request.text, "html.parser")
    pages = job_soup.find("div", {"class": "s-pagination"}).find_all("a")
    for page in pages[:-1]:
        pag = page.attrs['href']
        pag = f"https://stackoveflow.com{pag}"
        for page in pag:
            page_request = requests.get(page)
            page_soup = BeautifulSoup(page_request.text, "html.parser")
            page_main = page_soup.find("company", {"id": "job_list"})
            sections = page_main.find_all(
                "section", {"class": "flex--item fl1 text mb0"})
            for section in sections:
                print(section)
    return job_result
