import pandas as pd
import requests

# Replace this with your SerpApi key
SERPAPI_API_KEY = '14a481815f091a01e60215a1a6c049c71f563a5e52d4914653a94eec4bf77bce'

# Function to search LinkedIn URLs on Google
def get_linkedin_url(company_name):
    search_query = f"{company_name} LinkedIn"
    params = {
        "q": search_query,
        "api_key": SERPAPI_API_KEY,
        "engine": "google"
    }

    response = requests.get('https://serpapi.com/search', params=params)
    search_results = response.json()

    # Extract LinkedIn URL from search results (if available)
    for result in search_results.get("organic_results", []):
        if 'linkedin.com/company' in result['link']:
            return result['link']

    return None

companies = [
    "Apple", "Microsoft", "Samsung Electronics", "Alphabet", "AT&T", "Amazon", 
    "Verizon Communications", "China Mobile", "Walt Disney", "Facebook", "Alibaba", 
    "Intel", "Softbank", "IBM", "Tencent Holdings", "Nippon Telegraph & Tel", 
    "Cisco Systems", "Oracle", "Deutsche Telekom", "Taiwan Semiconductor", "KDDI", 
    "SAP", "Telefónica", "América Móvil", "Hon Hai Precision", "Dell", "Orange", 
    "China Telecom", "SK Hynix", "Accenture", "Broadcom", "Micron Technology", 
    "Qualcomm", "PayPal", "China Unicom", "HP", "BCE", "Tata Consultancy Services", 
    "Automatic Data Processing", "BT Group", "Mitsubishi Electric", "Canon", 
    "Booking Holdings", "Saudi Telecom", "JD.com", "Texas Instruments", "Netflix", 
    "Philips", "Etisalat", "Baidu", "ASML Holding", "Salesforce.com", "Applied Materials", 
    "Recruit Holdings", "SingTel", "Adobe", "Xiaomi", "Telstra", "VMware", 
    "TE Connectivity", "SK Holdings", "Murata Manufacturing", "Cognizant", "NVIDIA", 
    "eBay", "Telenor", "Vodafone", "SK Telecom", "Vivendi", "Naspers", "Infosys", 
    "China Tower Corp.", "Swisscom", "Corning", "Fidelity National Information", 
    "Rogers Communications", "Nintendo", "Kyocera", "NXP Semiconductors", "DISH Network", 
    "Rakuten", "Altice Europe", "TELUS", "Capgemini", "Activision Blizzard", 
    "Analog Devices", "Lam Research", "DXC Technology", "Legend Holding", 
    "Lenovo Group", "NetEase", "Tokyo Electron", "Keyence", "Telkom Indonesia", 
    "Nokia", "Fortive", "Ericsson", "Fiserv", "Fujitsu", "Hewlett Packard Enterprise"
]


# Prepare a list for storing the data
data = []

# Loop through the companies and fetch LinkedIn URLs
for company in companies:
    linkedin_url = get_linkedin_url(company)
    data.append({
        'Company': company,
        'LinkedIn URL': linkedin_url
    })

# Save the data into a CSV file
df = pd.DataFrame(data)
df.to_csv('companies_linkedin.csv', index=False)

print("CSV file created successfully!")
