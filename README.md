🧱 Firewall Policy Simulator
🧰 Tool Overview

Firewall Policy Simulator is a Python-based GUI tool built with Tkinter that allows users to create, save, load, and simulate firewall rules in an easy-to-use graphical interface.
It helps cybersecurity learners and professionals understand how firewalls filter packets based on defined policies such as source IP, destination IP, port, protocol, and action (ALLOW/DENY).

⚙️ Key Features

🧩 Add Firewall Rules – Create custom rules with Source IP, Destination IP, Port, Protocol (TCP/UDP/ANY), and Action (ALLOW/DENY).

💾 Save Rules – Save all created rules to a JSON file (firewall_rules.json) for future use.

📂 Load Rules – Load previously saved rules automatically at startup or manually.

🧮 Simulate Packets – Test packets against all rules to see if they’re ALLOWED, DENIED, or DROPPED.

🧱 Rule Matching Logic – Supports ANY for wildcards and Port 0 to represent any port.

🪟 User-Friendly GUI – Built using Tkinter with clear labels, input fields, and rule table.

🗂️ Persistent Storage – Rules are stored in a local JSON file—no database needed.

🚀 Cross-Platform Support – Runs on Windows, macOS, and Linux (Python 3+).

How to Run the Tool


1️⃣ Clone the repository
git clone https://github.com/abhishek2871/Firewall-Policy-Rules-Simulator
cd firewall-policy-simulator

2️⃣ (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate  # for Windows
source venv/bin/activate  # for Linux/macOS

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the simulator
python firewall_simulator.py
