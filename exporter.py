import csv


def save_to_file(jobs):
    file = open("job.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["name", "place", "title", "time", "pay", "date", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
