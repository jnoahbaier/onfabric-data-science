import json
import pandas as pd
from collections import Counter

# Load the fashion catalog
print("Loading fashion catalog JSON...")
with open('fashion_catalog.json', 'r') as f:
    fashion_data = json.load(f)

# Function to extract categories
def extract_categories(data):
    categories = []
    
    # Check if data is a list of items
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and 'CATEGORY' in item:
                categories.append(item['CATEGORY'])
    # Check if data is a dictionary with items
    elif isinstance(data, dict):
        # Check if the data itself has a category field
        if 'CATEGORY' in data:
            categories.append(data['CATEGORY'])
            
        # Look for arrays or objects that might contain items
        for key, value in data.items():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict) and 'CATEGORY' in item:
                        categories.append(item['CATEGORY'])
            elif isinstance(value, dict) and 'CATEGORY' in value:
                categories.append(value['CATEGORY'])
    
    return categories

# Extract categories
print("Extracting categories...")
categories = extract_categories(fashion_data)

# Count occurrences of each category
category_counts = Counter(categories)

# Print the results
print(f"\nFound {len(category_counts)} unique categories:")
for category, count in category_counts.most_common():
    print(f"- {category}: {count} items")

# Save to CSV
pd.DataFrame(category_counts.most_common(), columns=['Category', 'Count']).to_csv('fashion_categories.csv', index=False)
print("\nSaved categories to fashion_categories.csv") 