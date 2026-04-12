def read_log(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File " + filename + " does not exist")
    except PermissionError:
        print("Error: No permission to read " + filename)

read_log("server_log.txt")
read_log("missing_file.txt")
