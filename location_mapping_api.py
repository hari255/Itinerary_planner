import requests

# Your Google API Key
api_key = 'YOUR_GOOGLE_API_KEY'

# List of attractions
attractions = [
    "Statue of Liberty, New York, NY",
    "Golden Gate Bridge, San Francisco, CA",
    "Grand Canyon, AZ"
]

def get_reviews(place_name):
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": place_name,
        "inputtype": "textquery",
        "fields": "place_id",
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    place_data = response.json()
    
    if place_data['candidates']:
        place_id = place_data['candidates'][0]['place_id']
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        details_params = {
            "place_id": place_id,
            "fields": "name,rating,review",
            "key": api_key
        }
        details_response = requests.get(details_url, params=details_params)
        return details_response.json().get('result', {}).get('reviews', [])
    return []

# Fetch reviews for each attraction
for attraction in attractions:
    print(f"Reviews for {attraction}:")
    reviews = get_reviews(attraction)
    if reviews:
        for review in reviews:
            print(f"Rating: {review.get('rating', 'N/A')}, Review: {review.get('text', 'N/A')}")
    else:
        print("No reviews found.")
    print("-" * 40)
