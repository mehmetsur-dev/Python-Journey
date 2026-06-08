# URL Shortener Simulator

url_database = {"goog": {"long_url": "https://www.google.com", "click_count": 12},
                "git": {"long_url": "https://www.github.com", "click_count": 45}
}

url_database. update({"py": {"long_url": "https://www.python.org", "click_count": 0}})


user_input = input("Enter a short code to visit: ").strip().lower()


link_data = url_database.get(user_input)

if link_data is not None:
    print(f"Redirecting to: {link_data['long_url']}")

    url_database[user_input]["click_count"] += 1
else:
    print("Error: Short code not found.")


print("\n------------------\n")

if "goog" in url_database:
    del url_database["goog"]
    print("Successfully deleted 'goog' from the database.")


print("\n--- Final Analytics Report ---")

for short_code, data in url_database.items():
    destination = data["long_url"]
    clicks = data["click_count"]

    print(f"Short Code: {short_code:<5} | Destination: {destination:<28} | Clicks: {clicks}")