****🚀 mass-curl-runner****
Bulk curl automation for recon, endpoint testing, and rapid HTTP analysis

A lightweight Python tool that lets you run curl across massive URL lists with custom headers, cookies, POST bodies, and more — all in one command.

✨ Key Features

📄 Process hundreds of URLs from a file

🧹 Ignores comments + empty lines

⚙️ Pass any additional flags directly to curl

⚡ Shows HTTP status + response time

🔇 Silent body output (faster, cleaner)

🛠️ Built for ethical hacking + recon workflows

**📁 URL File Example**

Your urls.txt should look like:

https://example.com/
https://example.com/login
https://example.com/api/users
# This is a comment

🏃‍♂️ How to Run
Basic run
- python3 mass_curl.py urls.txt

With curl flags
- python3 mass_curl.py urls.txt -k -L

Add cookies + headers
- python3 mass_curl.py urls.txt \
  -b "auth_session_hosted=xyz" \
  -H "X-Requested-With: XMLHttpRequest"

POST example
- python3 mass_curl.py urls.txt \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"test":1}'

**📤 Output Preview**
[*] Loaded 3 URLs

[*] Requesting: https://example.com/
HTTP 200 | time 0.152s

[*] Requesting: https://example.com/login
HTTP 302 | time 0.088s

🛠️ **Installation**
git clone https://github.com/<your-username>/mass-curl-runner
cd mass-curl-runner
chmod +x mass_curl.py

**📦 Requirements**

Python 3.8+

curl installed

URL list file

**🔒 Ethical Use**

This tool is for authorized testing only.
Do not use against systems without permission.

**📌 Future Features (Planned)**

Save responses to output directory

Only show certain status codes

Auto-parallelization for speed

JSON logging
