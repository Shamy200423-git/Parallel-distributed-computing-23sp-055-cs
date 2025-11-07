import multiprocessing
import time
import random
import os


# ---------------------- Worker Process ----------------------
def delivery_worker(task_queue, pipe_conn):
    """
    Worker takes parcels from the queue and sends status through a pipe.
    """
    while True:
        try:
            parcel = task_queue.get(timeout=3)
        except:
            break  # No more parcels

        if parcel == "STOP":
            break

        # Simulate delivery time
        deliver_time = random.randint(2, 6)
        print(f"[Worker-{os.getpid()}] Delivering {parcel}...")
        time.sleep(deliver_time)

        # Notify supervisor via pipe
        pipe_conn.send(f"{parcel} delivered by Worker-{os.getpid()} in {deliver_time}s")

    pipe_conn.send(f"Worker-{os.getpid()} finished.")
    pipe_conn.close()


# ---------------------- Supervisor Process ----------------------
def supervisor(pipe_conn):
    """
    Supervisor receives updates from workers through a pipe.
    """
    while True:
        msg = pipe_conn.recv()
        if msg == "CLOSE":
            print("[Supervisor] Shutting down.")
            break
        print(f"[Supervisor] Update: {msg}")


# ---------------------- Main Program ----------------------
if __name__ == "__main__":
    print("\n=== Parcel Delivery Simulation ===\n")

    # Shared queue for assigning parcels
    parcel_queue = multiprocessing.Queue()

    # Pipe for worker → supervisor messages
    parent_conn, child_conn = multiprocessing.Pipe()

    # Spawn 3 worker processes
    workers = [
        multiprocessing.Process(target=delivery_worker, args=(parcel_queue, child_conn))
        for _ in range(3)
    ]

    for w in workers:
        w.start()

    # Spawn supervisor process
    supervisor_process = multiprocessing.Process(target=supervisor, args=(parent_conn,))
    supervisor_process.start()

    # Add parcels to queue
    parcels = ["Laptop", "Mobile", "Shoes", "Book", "Camera", "Watch"]
    for p in parcels:
        parcel_queue.put(p)

    # Timeout monitoring (manager)
    start = time.time()
    TIME_LIMIT = 10  # seconds

    while time.time() - start < TIME_LIMIT:
        time.sleep(1)

    # Kill slow workers after timeout
    print("\n[Manager] Time's up! Checking worker speed...")
    for w in workers:
        if w.is_alive():
            print(f"[Manager] Worker-{w.pid} too slow → Terminating.")
            w.terminate()
            w.join()

    # Send stop signals for any remaining worker
    for _ in workers:
        parcel_queue.put("STOP")

    # Close supervisor
    parent_conn.send("CLOSE")
    supervisor_process.join()

    print("\n=== Simulation Ended ===\n")
