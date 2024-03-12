import json
from datetime import datetime
import urllib.parse
import csv
def csv_to_json(csv_file_path, json_file_path):
    rows = []

    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            rows.append(row)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4)

    print(f"CSV data has been successfully converted to JSON and saved to {json_file_path}.")

csv_file_path = 'internship_listings.csv'
json_file_path = 'internship_listings.json'


csv_to_json(csv_file_path, json_file_path)



with open('header.md', 'r', encoding='utf-8') as header_file:
    header_content = header_file.read()

with open('internship_listings.json', 'r', encoding='utf-8') as file:
    listings = json.load(file)


markdown_content = header_content + "\n\n# Internship Listings for Summer 2024\n\n"
markdown_content += "| Company | Role | Location(s) | Apply/Link | Date Posted |\n"
markdown_content += "|---------|------|-------------|-------|-------------|\n"

sorted_listings = sorted(listings, key=lambda x: x.get('date_posted', 0), reverse=True)

for listing in listings[:500]:
    company_name = listing.get('Company', 'N/A')
    role = listing.get('Role', 'N/A')
    locations = listing.get('Location(s)', 'N/A')
    date_posted = listing.get('Date Posted', 'N/A') 
    apply_url = listing.get('Apply', '')
    apply_url_encoded = urllib.parse.quote(apply_url, safe=':/')
    link_button = (f'<a href="{apply_url_encoded}"><img src="data/images/applybutton.png" alt="Apply Button" style="width:85px;"></a>'
                    f'<a href="https://www.interninsider.me/subscribe?utm_source=git"><img src="data/images/interninsidersmall.png" alt="Intern Insider" style="width:40px;"></a>'
                    f'<a href="https://www.ribbon.ai/install"><img src="data/images/ribbonsmall.png" alt="Ribbon" style="width:40px;"></a>')

    markdown_content += f"| {company_name} | {role} | {locations} | {link_button} | {date_posted} |\n"

with open('footer.md', 'r', encoding='utf-8') as footer_file:
    footer_content = footer_file.read()

markdown_content += footer_content


with open('../README.md', 'w', encoding='utf-8') as readme_file:
    readme_file.write(markdown_content)

print("README.md has been created successfully.")
