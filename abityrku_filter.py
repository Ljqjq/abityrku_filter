from bs4 import BeautifulSoup
import requests
import urllib3

# Disable warnings about SSL verification being bypassed
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL of the webpage to scrape
link = 'https://abit-poisk.org.ua/rate2024/direction/1346377'

try:
    # Fetch the webpage with SSL verification disabled
    response = requests.get(link, verify=False, timeout=10)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    html_text = response.text
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Check if HTML is valid
if not html_text.strip():
    print("Error: Empty or invalid HTML content")
    exit()

# Parse HTML
try:
    soup = BeautifulSoup(html_text, 'lxml')
except Exception as e:
    print(f"Error parsing HTML with BeautifulSoup: {e}")
    exit()
print (link)
# Continue processing
print("HTML fetched and parsed successfully!")



# Initialize variables
garantu = 0
target_name = 'Яворський І. А.'  # Hardcoded for now; consider making it configurable

# Find all relevant rows
abityrku = soup.find_all('tr', class_='application-status application-status-14')
print (soup)
print("_______________________________________________________\n_______________________________________________________\n_______________________________________________________\n_______________________________________________________")

print(abityrku)
# Process each application row
for abityrka in abityrku:
    # Extract and clean name and priority
    abityrka_name = abityrka.find('a').text.strip()
    abityrka_prioritet = abityrka.find('td', class_='hidden-xs application-status-cell-priority-14').text.strip()

    # Check for the target name
    if abityrka_name == target_name:
        print('Target found: me')
        break

    # Count applications with priority 1
    if abityrka_prioritet == 'К':
        continue  # Skip 'К' entries
    try:
        if int(abityrka_prioritet) == 1:
            garantu += 1
    except ValueError:
        continue  # Skip invalid priority entries

    # Print applicant details
    print(f"Name: {abityrka_name}, Priority: {abityrka_prioritet}")

# Print the total count
print(f"Total guaranteed applications: {garantu}")
