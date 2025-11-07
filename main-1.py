import threading
import multiprocessing

#   Function 1: Check if a number is positive, negative, or zero 
def check_number(num):
    """Check if a number is positive, negative, or zero."""
    if num > 0:
        print(f"{num} is a Positive number")
    elif num == 0:
        print(f"{num} is Zero")
    else:
        print(f"{num} is a Negative number")


#   Function 2: Find the sum of all numbers in a list 
def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    total = sum(numbers)
    print(f"The sum of the list is: {total}")


#  Threading Implementation 
def run_with_threads():
    """Run both functions using threading."""
    print("\n--- Running with Threads ---")
    t1 = threading.Thread(target=check_number, args=(1,))
    t2 = threading.Thread(target=calculate_sum, args=([6, 6, 7, 8, -3, 2, 5, 44, 22],))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()


#  Multiprocessing Implementation
def run_with_processes():
    """Run both functions using multiprocessing."""
    print("\n--- Running with Processes ---")
    p1 = multiprocessing.Process(target=check_number, args=(-4.5,))
    p2 = multiprocessing.Process(target=calculate_sum, args=([6, 6, 7, 8, -3, 2, 5, 44, 22],))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()


#  Main Execution 
if __name__ == "__main__":
    print("Starting Program Execution...")
    
    # Run functions using threads
    run_with_threads()

    # Run functions using separate processes
    run_with_processes()

    print("\nProgram Completed.")
