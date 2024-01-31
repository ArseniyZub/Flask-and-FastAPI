import asyncio
import random
import time

async def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

async def calculate_sum_partial(arr, start, end):
    return sum(arr[start:end])

async def main():
    array_size = 1000000
    num_tasks = 4

    arr = await generate_random_array(array_size)

    start_time = time.time()

    tasks = []

    for i in range(num_tasks):
        start_index = i * (array_size // num_tasks)
        end_index = (i + 1) * (array_size // num_tasks) if i != num_tasks - 1 else array_size

        task = calculate_sum_partial(arr, start_index, end_index)
        tasks.append(task)

    partial_sums = await asyncio.gather(*tasks)
    total_sum = sum(partial_sums)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Сумма элементов массива: {total_sum}")
    print(f"Время выполнения: {elapsed_time} секунд")

if __name__ == "__main__":
    asyncio.run(main())
