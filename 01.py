import queue
import time

def parse_cmd(cmd):
    cmd = cmd.strip()
    cmd = cmd.split(' ')
    cmd[0] = cmd[0].lower()  
    return cmd

request_queue = queue.Queue()

def generate_request():
    global request_counter
    request_counter += 1
    request = f"Request {request_counter}"  
    request_queue.put(request) 
    print(f"New request added to queue: {request}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing request: {request}")
        time.sleep(2)
        print(f"{request} processed successfully")
    else:
        print("No new requests to process")

request_counter = 0

def main():
    while True:
        user_input = input("Enter 'add' to create a new request, 'process' to handle requests, or 'exit' to finish: ")

        cmd = parse_cmd(user_input)

        if cmd[0] == "add":
            if len(cmd) > 1:
                request = " ".join(cmd[1:])  
                generate_request()
            else:
                print("No request specified. Please try again.")
        elif cmd[0] == "process":
            process_request()
        elif cmd[0] == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
