import json
from collections import Counter

def load_countries_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_all_languages(countries_data):
    all_languages = []
    for country in countries_data:
        all_languages.extend(country['languages'])
    return all_languages

def most_spoken_languages(countries_data, n=10):
    # Get all languages from the countries data
    all_languages = get_all_languages(countries_data)
    
    # Count the occurrences of each language
    language_counts = Counter(all_languages)
    
    # Sort languages by count in descending order and get the top n
    top_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:n]
    
    # Format the result as a list of dictionaries
    result = []
    for lang, count in top_languages:
        result.append({'language': lang, 'count': count})
    
    return result

# Load the data
file_path = 'data/countries-data.py'  # Adjust this path as necessary
countries_data = load_countries_data(file_path)

# Get top 10 languages
top_10_languages = most_spoken_languages(countries_data, 10)

# Print results
print("Top 10 most spoken languages:")
for lang in top_10_languages:
    print(f"{lang['language']}: {lang['count']} countries")

print("\nTop 20 most spoken languages:")
top_20_languages = most_spoken_languages(countries_data, 20)
for lang in top_20_languages:
    print(f"{lang['language']}: {lang['count']} countries")