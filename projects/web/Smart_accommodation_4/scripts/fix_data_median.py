import gzip
import csv
import os
import shutil
import random

def parse_price(val):
    if not val:
        return None
    val_str = val.strip().replace('$', '').replace(',', '')
    if not val_str:
        return None
    try:
        return float(val_str)
    except ValueError:
        return None

def compute_medians(in_path):
    print("Computing medians...")
    prices_by_group = {}
    with gzip.open(in_path, 'rt', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nb = row.get('neighbourhood_cleansed', 'Unknown')
            rt = row.get('room_type', 'Unknown')
            price = parse_price(row.get('price'))
            
            if price is not None:
                group = (nb, rt)
                if group not in prices_by_group:
                    prices_by_group[group] = []
                prices_by_group[group].append(price)
                
    medians = {}
    for group, prices in prices_by_group.items():
        sorted_prices = sorted(prices)
        n = len(sorted_prices)
        if n == 0:
            medians[group] = 1200.0
        elif n % 2 == 1:
            medians[group] = sorted_prices[n//2]
        else:
            medians[group] = (sorted_prices[n//2 - 1] + sorted_prices[n//2]) / 2.0
            
    return medians

def generate_price(nb, rt, medians):
    med = medians.get((nb, rt), 1200.0)
    # random between 0.8 and 1.2 of median, rounded to nearest 10
    new_price = med * random.uniform(0.8, 1.2)
    return round(new_price / 10) * 10

def process_file(in_path, out_path, is_gz, medians):
    print(f"Processing {in_path}...")
    open_func = lambda p, m, enc: gzip.open(p, m, encoding=enc) if is_gz else open(p, m, encoding=enc)
        
    with open_func(in_path, 'rt', 'utf-8-sig') as f_in, \
         open_func(out_path, 'wt', 'utf-8') as f_out:
        
        reader = csv.DictReader(f_in)
        fieldnames = list(reader.fieldnames)
        if fieldnames and fieldnames[0] == '\ufeffid':
            fieldnames[0] = 'id'
            
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        
        fixed_count = 0
        for row in reader:
            needs_fix = False
            if '\ufeffid' in row:
                row['id'] = row.pop('\ufeffid')
                
            if 'name' in row and not row['name'].strip():
                row['name'] = f"未命名房源 #{row.get('id', '')}"
                needs_fix = True
                
            if 'price' in row:
                if parse_price(row['price']) is None:
                    nb = row.get('neighbourhood_cleansed', 'Unknown')
                    rt = row.get('room_type', 'Unknown')
                    row['price'] = str(generate_price(nb, rt, medians))
                    needs_fix = True
                        
            if needs_fix:
                fixed_count += 1
                
            writer.writerow(row)
            
    print(f"Fixed {fixed_count} rows in {in_path}.")
    shutil.move(out_path, in_path)

if __name__ == '__main__':
    random.seed(42) # For reproducible random prices
    listings_path = os.path.join('data', 'listings_cleaned.csv.gz')
    if os.path.exists(listings_path):
        medians = compute_medians(listings_path)
        process_file(listings_path, listings_path + '.tmp', True, medians)
        
    preds_path = os.path.join('data', '_predictions.csv')
    if os.path.exists(preds_path):
        process_file(preds_path, preds_path + '.tmp', False, medians)
        
    print("Done!")
