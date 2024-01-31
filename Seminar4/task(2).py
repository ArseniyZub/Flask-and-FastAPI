import multiprocessing
import random
import time

def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def calculate_sum_partial(arr, start, end, result_queue):
    partial_sum = sum(arr[start:end])
    result_queue.put(partial_sum)

def main():
    array_size = 1000000
    num_processes = 4

    arr = generate_random_array(array_size)

    result_queue = multiprocessing.Queue()

    processes = []

    start_time = time.time()

    for i in range(num_processes):
        start_index = i * (array_size // num_processes)
        end_index = (i + 1) * (array_size // num_processes) if i != num_processes - 1 else array_size

        process = multiprocessing.Process(target=calculate_sum_partial, args=(arr, start_index, end_index, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = 0
    while not result_queue.empty():
        total_sum += result_queue.get()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Сумма элементов массива: {total_sum}")
    print(f"Время выполнения: {elapsed_time} секунд")

if __name__ == "__main__":
    main()
