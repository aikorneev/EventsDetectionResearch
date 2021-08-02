import json
import requests as req
import csv
import math

if __name__ == '__main__':
    page_start = 497
    page = page_start
    events_on_page = 100  # max = 100
    page_count = page + 1 #to go into "while"

    f = csv.writer(open("test.csv", "w+", newline='', encoding='utf-8'), delimiter=';')
    f.writerow(["Short name","Name", "Description", "Body text", "Dates", "City", "Place","Coordinates","Category", "Event tag"])

    while page_count > page:
        par = {"lang": "ru", "fields": "short_title,title,description,body_text,dates,location,place,categories,tags", "page_size":events_on_page, "page":page}
        r = req.get("https://kudago.com/public-api/v1.4/events/", params=par)
        parsed = json.loads(r.text)

        if page == page_start:
            page_count = math.ceil(parsed["count"]/events_on_page)
            print('events number', parsed["count"])
            print('page number', page_count)

        for event in parsed["results"]:
            if not event["place"]:
                place = "None"
                coordinates = "None"
            else:
                placeid = event["place"]["id"]
                place_par = {"lang": "ru", "fields": "address,coords"}
                place_r = req.get("https://kudago.com/public-api/v1.4/places/" + str(placeid) + "/", params=place_par)
                parsed = json.loads(place_r.text)
                if "address" in parsed:
                    place = parsed["address"]
                else:
                    place = "None"
                if "coords" in parsed:
                    coordinates = parsed["coords"]
                else:
                    place = "None"

            f.writerow([event["short_title"],
                        event["title"],
                        event["description"],
                        event["body_text"],
                        event["dates"],
                        event["location"]["slug"],
                        place,
                        coordinates,
                        ','.join(event["categories"]),
                        ','.join(event["tags"])])
        print("Page",page,"finished")
        page +=1

    print("done")