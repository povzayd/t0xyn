import os
import time
from curl_cffi import requests

def search_tellonym(terms):
    url = "https://api.tellonym.me/search/users"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://tellonym.me/",
        "Origin": "https://tellonym.me",
        "Accept-Encoding": "gzip, deflate, br"
    }

    with open("results.txt", "w", encoding="utf-8") as f:
        for index, term in enumerate(terms):
            #bypass ratelimitttttt
            if index > 0:
                time.sleep(1.5)

            print(f"[+] Searching: {term}")
            params = {
                "searchString": term,
                "term": term,
                "limit": "100"
            }

            try:
    
                response = requests.get(url, headers=headers, params=params, impersonate="chrome")
                
                if response.status_code != 200:
                    print(f"[!] Failed for {term} (HTTP {response.status_code})")
                    continue

                data = response.json()
                users = data.get("results", [])

                f.write(f"\n=== Results for '{term}' ===\n")
                if not users:
                    f.write("No results found.\n")
                    continue

                for user in users:
                    f.write(f"\nDisplay Name : {user.get('displayName')}\n")
                    f.write(f"Username     : {user.get('username')}\n")
                    f.write(f"About Me     : {user.get('aboutMe', 'N/A')}\n")
                    f.write(f"Instagram    : {user.get('instagramLink', 'N/A')}\n")
                    f.write(f"Snapchat     : {user.get('snapchatLink', 'N/A')}\n")
                    f.write(f"Verified     : {'Yes' if user.get('isVerified') else 'No'}\n")
                    f.write(f"Active       : {'Yes' if user.get('isActive') else 'No'}\n")
                    f.write("-" * 40 + "\n")

            except Exception as e:
                print(f"[!] Error processing {term}: {e}")

    print("\n[✓] All results saved to results.txt")

def get_terms_from_file(filepath):
    if not os.path.isfile(filepath):
        print("[!] File not found.")
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

if __name__ == "__main__":
    print("Choose input method:")
    print("1. Enter comma-separated search terms")
    print("2. Provide path to a .txt file with terms")

    choice = input("Enter option (1 or 2): ").strip()

    if choice == "1":
        user_input = input("Enter search terms (comma separated): ")
        terms = [term.strip() for term in user_input.split(",") if term.strip()]
    elif choice == "2":
        filepath = input("Enter full path to .txt file: ").strip()
        terms = get_terms_from_file(filepath)
    else:
        print("[!] Invalid option selected.")
        exit()

    if not terms:
        print("[!] No terms to search.")
    else:
        search_tellonym(terms)
