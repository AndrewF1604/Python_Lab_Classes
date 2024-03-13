import multiprocessing
import time
import matplotlib.pyplot as plt


def bubble_sort_chunk(chunk):
    n = len(chunk)
    for i in range(n):
        for j in range(0, n - i - 1):
            if chunk[j] > chunk[j + 1]:
                chunk[j], chunk[j + 1] = chunk[j + 1], chunk[j]
    return chunk


def parallel_bubble_sort(input_list, num_processes):
    chunk_size = len(input_list) // num_processes
    pool = multiprocessing.Pool(processes=num_processes)

    chunks = [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]
    sorted_chunks = pool.map(bubble_sort_chunk, chunks)

    sorted_list = []
    while sorted_chunks:
        min_values = [chunk[0] for chunk in sorted_chunks]
        min_index = min_values.index(min(min_values))
        sorted_list.append(sorted_chunks[min_index].pop(0))
        if not sorted_chunks[min_index]:
            del sorted_chunks[min_index]

    return sorted_list


def measure_sorting_time(input_size, num_processes):
    input_list = list(range(input_size, 0, -1))
    start_time = time.time()
    sorted_list = parallel_bubble_sort(input_list, num_processes)
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    input_sizes = [200, 1000, 10000, 15000]
    num_processes_list = [1,2, 4]
    results = []

    for num_processes in num_processes_list:
        process_times = []
        for input_size in input_sizes:
            sorting_time = measure_sorting_time(input_size, num_processes)
            process_times.append(sorting_time)
        results.append(process_times)

    # Wykres  mmis@student.agh.edu.pl
    plt.figure(figsize=(8, 6))
    for idx, num_processes in enumerate(num_processes_list):
        plt.plot(input_sizes, results[idx], marker='o', label=f'{num_processes} procesy')

    plt.xlabel('Rozmiar danych wejściowych')
    plt.ylabel('Czas sortowania (s)')
    plt.title('Czas sortowania bąbelkowego w zależności od liczby procesów i rozmiaru danych')
    plt.legend()
    plt.grid(True)
    plt.show()