from csv import DictReader
import csv

neg_review = []
pos_review = []

def gen_output():
    place = ['patong_google','patong_trip','promthep_google','promthep_trip','wat_google','wat_trip']
    for data in place:
        sort(data)

def sort(place):
    path = f'./data/{place}_clean_translated_add_rating.csv'
    with open(path, mode='r', encoding='utf-8') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:

            if row['rating'] in (None,'',""): rate = 0
            else: rate = row['rating']

            rating = int(rate)

            Review = row['th']

            if rating >= 0.0 and rating <= 2.5:
                neg_review.append(Review)

            elif rating >= 2.6 and rating <= 5:
                pos_review.append(Review)         

    fieldnames = ['Review']
    with open(f'./output/{place}_negative.csv', mode ='w', newline='', encoding='utf-8') as csvfile:
                    
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()

                    for data in neg_review:
                        writer.writerow({'Review' : data})

    with open(f'./output/{place}_positive.csv', mode='w', newline='', encoding='utf-8') as csvfile:

                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()

                    for data in pos_review:
                        writer.writerow({'Review' : data})
                        
gen_output()