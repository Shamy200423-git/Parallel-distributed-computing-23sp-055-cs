# Restaurant Kitchen Simulation 🍽️

## Overview
This project demonstrates the use of **advanced threading concepts in Python** to simulate a real-world restaurant kitchen scenario.  
It models concurrent activities such as cooking multiple dishes with limited stoves, waiting for all dishes to be completed, and notifying the waiter when everything is ready.

### Repository
[GitHub Repository Link](https://github.com/Shamy200423-git/Parallel-distributed-computing-23sp-055-cs)

---

## Key Features
- **Semaphore:** Limits the number of stoves available for chefs (only 2 at a time).  
- **Barrier:** Ensures all dishes are cooked before moving on.  
- **Condition:** Waiter gets notified once all dishes are ready to serve.  
- **RLock:** Provides thread-safe logging for clean console output.

---

## Real-Life Analogy
| Concept | Python Mechanism | Real-World Meaning |
|----------|------------------|--------------------|
| Limited stoves | `Semaphore` | Only two chefs can cook at a time |
| All dishes must finish before serving | `Barrier` | Wait until all meals are ready |
| Waiter serves when all done | `Condition` | Waiter waits for chefs’ signal |
| Safe console printing | `RLock` | Prevents messy or overlapping log outputs |

---

## Code Example
```python
import threading
import time
import random

stoves = threading.Semaphore(2)
num_dishes = 4
cook_barrier = threading.Barrier(num_dishes)
waiter_condition = threading.Condition()
log_lock = threading.RLock()
ready_dishes = []

def log(msg):
    with log_lock:
        print(msg)

def chef(dish_id):
    log(f"Chef started preparing Dish {{dish_id}}.")
    with stoves:
        log(f"Dish {{dish_id}} is cooking...")
        time.sleep(random.uniform(1, 3))
        log(f"Dish {{dish_id}} is ready!")

    cook_barrier.wait()
    log(f"Chef finished Dish {{dish_id}}.")

    with waiter_condition:
        ready_dishes.append(dish_id)
        waiter_condition.notify()

def waiter():
    with waiter_condition:
        while len(ready_dishes) < num_dishes:
            waiter_condition.wait()
        log("Waiter: All dishes are ready! Serving now.")

def main():
    log("Restaurant opens. Chefs start cooking!")
    t_waiter = threading.Thread(target=waiter)
    t_waiter.start()

    chefs = []
    for i in range(1, num_dishes + 1):
        t = threading.Thread(target=chef, args=(i,))
        chefs.append(t)
        t.start()

    for t in chefs:
        t.join()

    t_waiter.join()
    log("Restaurant closed for the night.")

if __name__ == "__main__":
    main()
```

---

## Example Output
```
Restaurant opens. Chefs start cooking!
Chef started preparing Dish 1.
Chef started preparing Dish 2.
Dish 1 is cooking...
Dish 2 is cooking...
Dish 1 is ready!
Dish 2 is ready!
Chef started preparing Dish 3.
Chef started preparing Dish 4.
Dish 3 is cooking...
Dish 4 is cooking...
Dish 3 is ready!
Dish 4 is ready!
Waiter: All dishes are ready! Serving now.
Restaurant closed for the night.
```

---

## How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shamy200423-git/Parallel-distributed-computing-23sp-055-cs.git
   cd Parallel-distributed-computing-23sp-055-cs
   ```

2. **Run the Python script:**
   ```bash
   python restaurant_simulation.py
   ```

3. Observe the synchronized execution and notifications.

---

## Technologies Used
- Python 3.x  
- threading module (Semaphore, Barrier, Condition, RLock)

---

## License
This project is open source and available under the **MIT License**.
