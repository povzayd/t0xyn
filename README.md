🔍 t0xyn Tellonym Scrapping Tool!

This is a simple Python script to search for users on Tellonym.me by keywords or usernames. It interacts with Tellonym's backend API and extracts publicly available user data into a results.txt file.

---

📌 Features

🔎 Search Tellonym users by keyword or exact username.

📁 Option to load search terms from a .txt file.

📝 Saves detailed user info (display name, bio, social links, etc.) into results.txt.

🚫 Gracefully handles errors like failed API responses or empty results.

---

⚙️ Requirements

`Python 3.x`

`requests module`


Install dependencies using:

`pip install requests`


---

🧠 How It Works

1. You provide search terms (either manually or via a .txt file).


2. The script queries Tellonym's search API with each term.


3. It collects and prints:
```
Display name

Username

About Me

Instagram link

Snapchat link

Verification and activity status
```
4. All results are saved in results.txt.




---

🚀 Usage

Option 1: Manual Input

Run the script:
```
python t0xyn.py

Choose option 1 and enter comma-separated keywords:

Enter search terms (comma separated): hacker, programmer, xbee9
```

---

Option 2: File Input

Prepare a .txt file (e.g., names.txt) like this:
```
Jones Mill
pro max 
Random Name
```
Then run the script:
```
python t0xyn.py

Choose option 2 and enter the full file path:

Enter full path to .txt file: /path/to/names.txt
```

---

📂 Output Example (results.txt)
```
=== Results for 'hacker' ===

Display Name : John Doe  
Username     : hacker_123  
About Me     : Cybersecurity enthusiast.  
Instagram    : https://instagram.com/johndoe  
Snapchat     : https://snapchat.com/add/johndoe  
Verified     : No  
Active       : Yes  
----------------------------------------

```
---

🧪 Performance Note

✅ This tool was tested with a names.txt file containing 14k search terms[Region specific!!].                                                                                        
⛔ After that point, the API rate-limited further requests. [After 917333 lines. Means approx. 91733 users were scrapped]                                                      
👉 Suggestion: Add delays or rotate proxies if you plan on scraping at scale.


---

⚠️ Disclaimer

This script scrapes publicly available data from Tellonym’s web client API.

It is intended for educational, ethical, and research purposes only.

Do not use this for stalking, harassment, or any malicious activity.

Respect platform terms and rate limits.

---

📄 License

This project is open-source and provided as-is, without warranty or liability.
Use responsibly under the MIT License.
