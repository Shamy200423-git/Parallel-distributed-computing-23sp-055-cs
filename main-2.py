import threading
import time
import random

# -------------------------------
# Example: Restaurant Kitchen Simulation
# -------------------------------
# - Only 2 stoves available (Semaphore)
# - Wait until all dishes are cooked (Barrier)
# - Notify waiter when all dishes are ready (Condition)
# - Safe logging using RLock
# -------------------------------

stoves = threading.Semaphore(2)        # Only 2 chefs can cook at once
num_dishes = 4                         # Total dishes to prepare
cook_barrier = threading.Barrier(num_dishes)  # Wait until all dishes are ready
waiter_condition = threading.Condition()      # Waiter waits for notification
log_lock = threading.RLock()                  # Safe logging

ready_dishes = []


def log(msg):
    """Thread-safe print using RLock"""
    with log_lock:
        print(msg)


def chef(dish_id):
    """Each chef prepares one dish."""
    log(f"Chef started preparing Dish {dish_id}.")
    with stoves:
        log(f"Dish {dish_id} is cooking on the stove...")
        time.sleep(random.uniform(1, 3))
        log(f"Dish {dish_id} is cooked and ready to serve!")

    # Wait for all dishes to be ready
    cook_barrier.wait()
    log(f"Chef finished Dish {dish_id} and is cleaning up.")

    # Notify waiter
    with waiter_condition:
        ready_dishes.append(dish_id)
        waiter_condition.notify()


def waiter():
    """Waiter waits until all dishes are ready before serving."""
    with waiter_condition:
        while len(ready_dishes) < num_dishes:
            waiter_condition.wait()
        log("Waiter: All dishes are ready! Serving customers now.")


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
