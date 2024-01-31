import threading
import random
import time

def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def calculate_sum_partial(arr, start, end, result_lock, result_list):
    partial_sum = sum(arr[start:end])
    with result_lock:
        result_list.append(partial_sum)

def main():
    array_size = 1000000
    num_threads = 4

    arr = generate_random_array(array_size)

    result_list = []
    result_lock = threading.Lock()

    threads = []

    start_time = time.time()

    for i in range(num_threads):
        start_index = i * (array_size // num_threads)
        end_index = (i + 1) * (array_size // num_threads) if i != num_threads - 1 else array_size

        thread = threading.Thread(target=calculate_sum_partial, args=(arr, start_index, end_index, result_lock, result_list))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(result_list)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Сумма элементов массива: {total_sum}")
    print(f"Время выполнения: {elapsed_time} секунд")

if __name__ == "__main__":
    main()
