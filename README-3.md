# Parallel and Distributed Computing Project

## Overview

This repository contains a set of Python programs demonstrating the
principles of **parallel** and **distributed computing** using various
techniques such as **threading**, **multiprocessing**, and
**inter-process communication**.\
The goal is to understand how concurrent and parallel tasks can be
executed efficiently using Python.

------------------------------------------------------------------------

## Core Concepts

### Threading

Threading allows multiple tasks to execute concurrently within the same
process.\
It is best suited for **I/O-bound operations** where tasks spend time
waiting for input/output events.

### Multiprocessing

Multiprocessing enables the execution of multiple processes in parallel,
each with its own memory space.\
It is ideal for **CPU-bound operations**, allowing full utilization of
multiple CPU cores.

### Inter-Process Communication (IPC)

IPC is used for data sharing between processes through mechanisms such
as **queues**, **pipes**, or **shared memory**.

------------------------------------------------------------------------

## Key Features

-   Demonstrates both **thread-based** and **process-based**
    parallelism.\
-   Showcases Python's built-in modules: `threading`, `multiprocessing`,
    and `queue`.\
-   Illustrates synchronization, communication, and data sharing between
    concurrent tasks.\
-   Emphasizes real-world computing concepts such as scalability and
    efficiency.

------------------------------------------------------------------------

## How to Run

1.  **Clone the Repository**

    ``` bash
    git clone https://github.com/Shamy200423-git/Parallel-distributed-computing-23sp-055-cs.git
    cd Parallel-distributed-computing-23sp-055-cs
    ```

2.  **Run the Program**

    ``` bash
    python main.py
    ```

    or, if there are multiple scripts:

    ``` bash
    python filename.py
    ```

3.  Observe how threading and multiprocessing behave differently in
    terms of performance and resource usage.

------------------------------------------------------------------------

## Example Output

    Starting Parallel Execution...

    --- Running with Threads ---
    Task 1: Completed
    Task 2: Completed
    Elapsed Time: 1.23 seconds

    --- Running with Processes ---
    Task 1: Completed
    Task 2: Completed
    Elapsed Time: 0.87 seconds

    Program Execution Finished.

------------------------------------------------------------------------

## Project Structure

    .
    ├── main.py               # Primary script demonstrating parallel execution
    ├── utils/                # Helper modules and functions
    ├── examples/             # Additional code samples for experimentation
    └── README.md             # Project documentation

------------------------------------------------------------------------

## Technologies Used

-   Python 3.x\
-   Threading Module\
-   Multiprocessing Module\
-   Queue and IPC Concepts

------------------------------------------------------------------------

## Repository

[GitHub Repository -- Parallel Distributed Computing
Project](https://github.com/Shamy200423-git/Parallel-distributed-computing-23sp-055-cs)

------------------------------------------------------------------------

## License

This project is open source and distributed under the **MIT License**.
