import datetime

servers = {
    "web-server-1": "192.168.1.1",
    "web-server-2": "192.168.1.2",
    "web-server-3": "192.168.1.3",
    "app-server-1": "192.168.1.4"
}

active_servers = ["web-server-1", "web-server-2", "app-server-1"]

def write_log(server_name, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = timestamp + " | " + server_name + " | " + status + "\n"

    with open("server_log.txt", "a") as log_file:
        log_file.write(log_entry)

    print("Logged: " + log_entry)

def check_and_log():
    print("===== Server Status Check =====")
    print("")
    
    for server in servers:
        if server in active_servers:
            status = "ACTIVE"
        else:
            status = "OFFLINE"
        
        write_log(server, status)
    
    print("")
    print("===== All statuses logged to server_log.txt =====")

check_and_log()
