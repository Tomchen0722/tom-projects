import gzip
import csv
import os
import shutil

def process_file(in_path, out_path, is_gz):
    print(f"Processing {in_path}...")
    if is_gz:
        open_func = lambda p, m, enc: gzip.open(p, m, encoding=enc)
    else:
        open_func = lambda p, m, enc: open(p, m, encoding=enc)
        
    with open_func(in_path, 'rt', 'utf-8-sig') as f_in, \
         open_func(out_path, 'wt', 'utf-8') as f_out:
        
        reader = csv.DictReader(f_in)
        # Handle fieldnames if there was a BOM on 'id'
        fieldnames = list(reader.fieldnames)
        if fieldnames and fieldnames[0] == '\ufeffid':
            fieldnames[0] = 'id'
            
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        
        fixed_count = 0
        for row in reader:
            needs_fix = False
            
            # fix id key if BOM was present
            if '\ufeffid' in row:
                row['id'] = row.pop('\ufeffid')
                
            # Check name
            if 'name' in row and not row['name'].strip():
                row['name'] = f"未命名房源 #{row['id']}"
                needs_fix = True
                
            # Check price
            if 'price' in row:
                price_str = row['price'].strip().replace('$', '').replace(',', '')
                if not price_str:
                    row['price'] = '1200'
                    needs_fix = True
                else:
                    try:
                        float(price_str)
                    except ValueError:
                        row['price'] = '1200'
                        needs_fix = True
                        
            if needs_fix:
                fixed_count += 1
                
            writer.writerow(row)
            
    print(f"Fixed {fixed_count} rows in {in_path}.")
    shutil.move(out_path, in_path)

if __name__ == '__main__':
    # Fix listings_cleaned.csv.gz
    listings_path = os.path.join('data', 'listings_cleaned.csv.gz')
    if os.path.exists(listings_path):
        process_file(listings_path, listings_path + '.tmp', True)
        
    # Fix _predictions.csv
    preds_path = os.path.join('data', '_predictions.csv')
    if os.path.exists(preds_path):
        process_file(preds_path, preds_path + '.tmp', False)
        
    print("Done!")
