import requests
import random
import threading
from queue import Queue

# Function to generate a random phone number for a specific operator series
def generate_numbers(operator, count):
    numbers = []
    for _ in range(count):
        number = operator
        for _ in range(9):  # Generate random 9-digit number
            number += str(random.randint(0, 9))
        numbers.append(number)
    return numbers

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
    # User input for amount and number of threads
    amount = int(input("Enter the number of messages to send: "))
    num_threads = int(input("Enter the number of threads: "))
    num_count = int(input("Enter the number of phone numbers to generate for each operator: "))

    # Generate numbers for 018 and 016 operators
    operator_016 = generate_numbers("016", num_count)
    operator_018 = generate_numbers("018", num_count)

    # Fill the queue with random phone numbers from 018 and 016 operators
    for num_list in [operator_016, operator_018]:
        for number in num_list:
            number_queue.put(number)

    # Create worker threads
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    # Wait for all tasks in the queue to be processed
    number_queue.join()

if __name__ == "__main__":
    number_queue = Queue()
    message = """18+ sex HOT MEHJABIN CHOWDHURY SEX VIDEO LINK: https://t.me/+U-6EWcmE_9Y4NzRl 💔https://t.me/+U-6EWcmE_9Y4NzRl🫣 
    এখুনি"""
    main()
