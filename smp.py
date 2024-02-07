import requests
import random
import threading
from queue import Queue

# Function to generate a random phone number
def generate_random_number():
    number = "018"
    for _ in range(8):
        number += str(random.randint(1, 9))
    return number

# Function to send SMS without user agents
def send_sms(number, message):
    url = f"https://alternativezonebd.xyz/custom-sms/send_sms.php?msisdn={number}&message={message}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"Message sent successfully to {number}")
        else:
            print(f"Failed to send message to {number}")
    except Exception as e:
        print(f"Failed to send message to {number}: {e}")

# Worker function to send SMS in parallel
def worker():
    while True:
        number = number_queue.get()
        send_sms(number, message)
        number_queue.task_done()

# Main function
def main():
    # User input for number of threads
    num_threads = int(input("Enter the number of threads: "))

    # Fill the queue with random phone numbers
    for _ in range(amount):
        number_queue.put(generate_random_number())

    # Create worker threads
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    # Wait for all tasks in the queue to be processed
    number_queue.join()

if __name__ == "__main__":
    number_queue = Queue()
    amount = int(input("Enter the number of messages to send: "))
    message = """18+ sex কোনো লিংক না ডিরেক্ট ভিডিও ,এই টেলিগ্রাম চ্যানেল এ দেওয়া আছে:https://t.me/+U-6EWcmE_9Y4NzRl 💔https://t.me/+U-6EWcmE_9Y4NzRl🫣 
    এখুনি"""
    main()
