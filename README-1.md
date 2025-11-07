# Multi-threaded and Multi-processed Python Program

## Overview
This project showcases the use of **threads** and **processes** in Python to execute two tasks simultaneously:

1. Determine whether a number is positive, negative, or zero.  
2. Compute the sum of all elements in a list.

Both tasks are executed using:
- **Threading** – lightweight concurrency within a single process.  
- **Multiprocessing** – true parallel execution using multiple processes.

---

## Core Concepts

### Threading
Threading enables multiple tasks to run concurrently within the same process.  
Since all threads share the same memory space, this approach is ideal for **I/O-bound operations**.

**Example:**
```python
t1 = threading.Thread(target=check_number, args=(1,))
t2 = threading.Thread(target=calculate_sum, args=(numbers,))
```

### Multiprocessing
Multiprocessing runs tasks in **separate processes**, each with its own memory space.  
This makes it a great choice for **CPU-bound operations** that benefit from parallelism.

**Example:**
```python
p1 = multiprocessing.Process(target=check_number, args=(-4.5,))
p2 = multiprocessing.Process(target=calculate_sum, args=(numbers,))
```

---

## Functions

**check_number(num)**  
Determines whether a given number is positive, negative, or zero.

**calculate_sum(numbers)**  
Calculates and prints the total sum of a list of numbers.

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Execute the script**
   ```bash
   python main.py
   ```

3. Observe results from both the **threading** and **multiprocessing** executions.

---

## Example Output
```
Starting Program Execution...

--- Running with Threads ---
1 is a Positive number
The sum of the list is: 83

--- Running with Processes ---
-4.5 is a Negative number
The sum of the list is: 83

Program Completed.
```

---

## Project Structure
```
.
├── main.py        # Python script implementing threading and multiprocessing
└── README.md      # Project documentation
```

---

## Technologies Used
- Python 3.x  
- threading module  
- multiprocessing module  

---

## License
This project is open source and distributed under the **MIT License**.
