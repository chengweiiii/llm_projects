import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the CVPR 2024 website
base_url = "https://openaccess.thecvf.com"
url = "https://openaccess.thecvf.com/CVPR2024?day=all"

# Fetch the HTML content
response = requests.get(url)
response.raise_for_status()  # Raise an exception for bad status codes

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all paper elements, limiting to the top 10
paper_elements = soup.find_all('dt', class_='ptitle')[:10]

# Extract data and store in a list of dictionaries
data = []
for paper_element in paper_elements:
    title_element = paper_element.find('a')
    title = title_element.text.strip()
    pdf_link = base_url + title_element['href']  # Add back the domain

    abstract_element = paper_element.find_next_sibling('dd')
    abstract = abstract_element.text.strip() if abstract_element else "Abstract not found" 

    data.append({
        'Title': title,
        'Abstract': abstract,
        'PDF Link': pdf_link
    })

# Create a DataFrame from the extracted data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("cvpr_2024_papers_top10.csv", index=False)

print("Data extraction and saving complete!")