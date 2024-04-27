import queue
import time

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

        if user_input == "add":
            generate_request()
        elif user_input == "process":
            process_request()
        elif user_input == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
