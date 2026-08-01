import gzip
import csv

def check_data():
    id_to_check = '1384029173741834977'
    found_in_listings = False
    
    with gzip.open('data/listings_cleaned.csv.gz', 'rt', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['id'] == id_to_check:
                found_in_listings = True
                print("Found in listings_cleaned.csv.gz!")
                print(f"Name: {row.get('name')}")
                print(f"Price: {row.get('price')}")
                break
                
    if not found_in_listings:
        print("NOT found in listings_cleaned.csv.gz!")

check_data()
