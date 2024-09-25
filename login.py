import warnings
warnings.filterwarnings('ignore')

import requests
from bs4 import BeautifulSoup
from getpass import getpass

# Create a session object
s = requests.Session()

# Define the headers
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-US,en;q=0.9',
    'connection': 'keep-alive',
    'host': 'login.usna.edu',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}

# The login page URL where we will scrape the request_id from
login_page_url = 'https://login.usna.edu'

# Get the login page to scrape the request_id
login_page_response = s.get(login_page_url, headers=headers, verify=False)

# Check if the login page loaded successfully
if login_page_response.ok:
    # Parse the HTML content of the page
    soup = BeautifulSoup(login_page_response.text, 'html.parser')

    # Scrape the request_id (replace 'input_name' with the actual name attribute if it's in an input field)
    request_id_input = soup.find('input', {'name': 'request_id'})
    
    if request_id_input:
        request_id = request_id_input['value']
        print(f'Found request_id: {request_id}')
    else:
        print("Failed to find request_id")
        request_id = None
else:
    print(f"Failed to load login page: Status Code {login_page_response.status_code}")
    request_id = None

# If request_id is found, proceed with login
if request_id:
    # Login URL (form submission URL)
    login_url = 'https://login.usna.edu/oam/server/auth_cred_submit'

    # Ask the user for credentials
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")  # Hides input for security

    # Define the login data, using the scraped request_id
    login_data = {
        'username': username,
        'password': password,
        'request_id': request_id,  # Use the scraped request_id
        'displayLangSelection': 'false',
        'Languages': ''
    }

    # Post the login data
    response = s.post(login_url, headers=headers, data=login_data, verify=False)

    # Check if the login was successful
    if response.ok:
        print(f'Successfully logged in! Status Code: {response.status_code}')
        
        # Now prompt user for input
        P_ALPHA = input("Enter midshipman alpha: ")
        P_LAST_NAME = input("Enter midshipman's last name: ")
        P_MICO_CO_NBR = input("Enter midshipman company number (e.g., 8): ")
        P_SECOF_COOF_SEBLDA_AC_YR = input("Enter academic year (e.g., 2025): ")
        P_SECOF_COOF_SEBLDA_SEM = input("Enter semester (e.g., FALL): ")

        # Define the payload
        payload = {
            'P_ALPHA': P_ALPHA,
            'P_LAST_NAME': P_LAST_NAME,
            'P_MICO_CO_NBR': P_MICO_CO_NBR,
            'P_SECOF_COOF_SEBLDA_AC_YR': P_SECOF_COOF_SEBLDA_AC_YR,
            'P_SECOF_COOF_SEBLDA_SEM': P_SECOF_COOF_SEBLDA_SEM,
            'P_SECOF_COOF_SEBLDA_BLK_NBR': '1',
            'P_MAJOR_CODE': '',
            'P_NOMI_FORMATTED_NAME': '',
            'Z_ACTION': 'QUERY',
            'Z_CHK': '0'
        }

        # The URL where the form is submitted
        action_query_url = 'https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery'

        # Make a POST request to submit the form
        response_query = s.post(action_query_url, headers=headers, data=payload, verify=False)

        # Check if the request was successful
        if response_query.ok:
            print(f'Query successful! Status Code: {response_query.status_code}')
            #print(response_query.text)  # Print the response content (HTML or other output)
        else:
            print(f'Query failed! Status Code: {response_query.status_code}')
    else:
        print(f'Login failed! Status Code: {response.status_code}')

def extract_table_from_html(response_text):
    # Parse the HTML content
    soup = BeautifulSoup(response_text, 'html.parser')

    # Find the table
    table = soup.find('table', {'border': True})

    if table:
        # Extract the headers
        headers = [header.get_text(strip=True) for header in table.find_all('th')]

        # Extract the rows
        rows = []
        for row in table.find_all('tr', {'class': 'cgrldatarow'}):
            cells = row.find_all('td')
            row_data = [cell.get_text(strip=True) for cell in cells]
            rows.append(row_data)

        # Format the table output nicely
        formatted_table = format_table(headers, rows)
        return formatted_table
    else:
        return "No table found in the response."

def format_table(headers, rows):
    # Calculate column widths based on the longest text in each column
    column_widths = [len(header) for header in headers]

    for row in rows:
        for i, cell in enumerate(row):
            column_widths[i] = max(column_widths[i], len(cell))

    # Create the table string
    formatted_output = []

    # Format the header row
    header_row = " | ".join(f"{header:<{column_widths[i]}}" for i, header in enumerate(headers))
    formatted_output.append(header_row)
    formatted_output.append("-" * len(header_row))  # Separator line

    # Format each data row
    for row in rows:
        data_row = " | ".join(f"{cell:<{column_widths[i]}}" for i, cell in enumerate(row))
        formatted_output.append(data_row)

    return "\n".join(formatted_output)

print(extract_table_from_html(response_query.text))