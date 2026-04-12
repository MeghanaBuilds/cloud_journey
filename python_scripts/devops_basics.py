servers = {
    "web-server-1": "192.168.1.1",
    "web-server-2": "192.168.1.2",
    "db-server-1": "192.168.1.3",
    "app-server-1": "192.168.1.4"
}

active_servers = ["web-server-1", "web-server-2", "app-server-1"]

def check_status(server_name):
    if server_name in active_servers:
        print(server_name + " is ACTIVE")
    else:
        print(server_name + " is OFFLINE")

def get_ip(server_name):
    if server_name in servers:
        print("IP address of " + server_name + " is: " + servers[server_name])
    else:
        print("Server not found in inventory")

print("===== Server Inventory Check =====")
print("")

print("--- Checking Server Status ---")
for server in servers:
    check_status(server)

print("")
print("--- Looking Up IP Addresses ---")
get_ip("web-server-1")
get_ip("db-server-1")

print("")
print("--- All Servers In Inventory ---")
for server in servers:
    print(server + " --> " + servers[server])

print("")
print("===== Check Complete =====")
