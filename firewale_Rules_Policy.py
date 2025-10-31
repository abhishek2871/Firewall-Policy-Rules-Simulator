import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Global rule list
rules = []

# File path for saving and loading rules
RULES_FILE = "firewall_rules.json"

#  FUNCTIONS 

def add_rule():
    src = src_ip.get()
    dst = dst_ip.get()
    port = port_num.get()
    proto = protocol.get()
    action = action_choice.get()

    if not (src and dst and port and proto and action):
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    rule = {
        "source": src,
        "destination": dst,
        "port": int(port),
        "protocol": proto.upper(),
        "action": action.upper()
    }

    rules.append(rule)
    refresh_table()
    messagebox.showinfo("Success", "Rule added successfully!")

def refresh_table():
    for row in rule_table.get_children():
        rule_table.delete(row)
    for rule in rules:
        rule_table.insert("", "end", values=(rule["source"], rule["destination"], rule["port"], rule["protocol"], rule["action"]))

def simulate_packet():
    packet = {
        "source": packet_src.get(),
        "destination": packet_dst.get(),
        "port": int(packet_port.get()),
        "protocol": packet_proto.get().upper()
    }

    for rule in rules:
        if (rule["source"] == packet["source"] or rule["source"] == "ANY") and \
           (rule["destination"] == packet["destination"] or rule["destination"] == "ANY") and \
           (rule["port"] == packet["port"] or rule["port"] == 0) and \
           (rule["protocol"] == packet["protocol"] or rule["protocol"] == "ANY"):
            result = f"PACKET {rule['action']}ED"
            output_label.config(text=result, fg="green" if rule["action"] == "ALLOW" else "red")
            return

    output_label.config(text="PACKET DROPPED (No matching rule)", fg="orange")

#NEW FUNCTIONS 

def save_rules():
    """Save all firewall rules to a JSON file."""
    try:
        with open(RULES_FILE, "w") as f:
            json.dump(rules, f, indent=4)
        messagebox.showinfo("Saved", f"Firewall rules saved to {os.path.abspath(RULES_FILE)}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save rules: {e}")

def load_rules():
    """Load firewall rules from JSON file if it exists."""
    global rules
    if os.path.exists(RULES_FILE):
        try:
            with open(RULES_FILE, "r") as f:
                rules = json.load(f)
            refresh_table()
            messagebox.showinfo("Loaded", f"Firewall rules loaded from {os.path.abspath(RULES_FILE)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load rules: {e}")
    else:
        messagebox.showwarning("Not Found", "No saved rules file found!")

# GUI SETUP

root = tk.Tk()
root.title("Firewall Policy Simulator")
root.geometry("850x600")

tk.Label(root, text="Add Firewall Rule", font=("Arial", 14, "bold")).pack(pady=5)

frm = tk.Frame(root)
frm.pack()

tk.Label(frm, text="Source IP:").grid(row=0, column=0)
src_ip = tk.Entry(frm)
src_ip.grid(row=0, column=1)

tk.Label(frm, text="Destination IP:").grid(row=0, column=2)
dst_ip = tk.Entry(frm)
dst_ip.grid(row=0, column=3)

tk.Label(frm, text="Port:").grid(row=1, column=0)
port_num = tk.Entry(frm)
port_num.grid(row=1, column=1)

tk.Label(frm, text="Protocol:").grid(row=1, column=2)
protocol = ttk.Combobox(frm, values=["TCP", "UDP", "ANY"])
protocol.grid(row=1, column=3)

tk.Label(frm, text="Action:").grid(row=2, column=0)
action_choice = ttk.Combobox(frm, values=["ALLOW", "DENY"])
action_choice.grid(row=2, column=1)

tk.Button(frm, text="Add Rule", command=add_rule, bg="#4CAF50", fg="white").grid(row=2, column=3, pady=5)

# Buttons for Save and Load
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="💾 Save Rules", command=save_rules, bg="#2196F3", fg="white", width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="📂 Load Rules", command=load_rules, bg="#FF9800", fg="white", width=15).grid(row=0, column=1, padx=5)

# Rule Table
rule_table = ttk.Treeview(root, columns=("Source", "Destination", "Port", "Protocol", "Action"), show="headings", height=8)
for col in ("Source", "Destination", "Port", "Protocol", "Action"):
    rule_table.heading(col, text=col)
rule_table.pack(pady=10)

# Packet Simulation
tk.Label(root, text="Simulate Packet", font=("Arial", 14, "bold")).pack(pady=5)
sim_frame = tk.Frame(root)
sim_frame.pack()

tk.Label(sim_frame, text="Source IP:").grid(row=0, column=0)
packet_src = tk.Entry(sim_frame)
packet_src.grid(row=0, column=1)

tk.Label(sim_frame, text="Destination IP:").grid(row=0, column=2)
packet_dst = tk.Entry(sim_frame)
packet_dst.grid(row=0, column=3)

tk.Label(sim_frame, text="Port:").grid(row=1, column=0)
packet_port = tk.Entry(sim_frame)
packet_port.grid(row=1, column=1)

tk.Label(sim_frame, text="Protocol:").grid(row=1, column=2)
packet_proto = ttk.Combobox(sim_frame, values=["TCP", "UDP"])
packet_proto.grid(row=1, column=3)

tk.Button(sim_frame, text="Simulate Packet", command=simulate_packet, bg="#009688", fg="white").grid(row=2, column=3, pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
output_label.pack(pady=10)

# Load rules automatically at startup
load_rules()

root.mainloop()
