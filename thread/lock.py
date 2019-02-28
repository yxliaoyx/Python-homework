import threading


def my_proc(data, lock):
    for _ in range(100000):
        for i in range(len(data)):
            with lock:
                data[i] = data[i] + 1


data = [1, 2, 3, 4]

lock = threading.Lock()
thread1 = threading.Thread(target=my_proc, args=(data, lock))
thread2 = threading.Thread(target=my_proc, args=(data, lock))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(data)
