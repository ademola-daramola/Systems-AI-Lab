import random
import time
import os

#merge sort implementation in Python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        Left = arr[:mid]        # Dividing the array elements into 2 halves
        Right = arr[mid:]

        merge_sort(Left)        # Sorting the first half
        merge_sort(Right)        # Sorting the second half

        i = j = k = 0
        
        # Copy data to temp arrays Left[] and Right[]
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1


# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10,4, 37, 29, 12, 15, 20, 25, 30, 35, 80, 50, 60, 70, 90, 100]
    print("Given array is:", arr)
    merge_sort(arr)
    print("Sorted array is:", arr)
    
    def run_benchmarks():
        sizes = [1000, 10000, 50000]
        print("ALGORITHM BENCHMARK REPORT - WEEK 2")
        print("=========================================")
        print(f"{'Array Size':<15}{'Data Type':<20}{'Execution Time':<15}")
        print("-----------------------------------------")
       
        for size in sizes:
             #1. Random Case
            rand_array = [random.randint(1, 100000) for _ in range(size)]
            start = time.perf_counter()
            merge_sort(rand_array)
            end = time.perf_counter()
            print(f"{size:<15}{'Random Data':<20}{(end - start):.6f} sec")
        
            # 2. Sorted Case (Best Case Scenario)
            sorted_array = list(range(size))
            start = time.perf_counter()
            merge_sort(sorted_array)
            end = time.perf_counter()
            print(f"{size:<15}{'Already Sorted':<20}{(end - start):.6f} sec")
        
            # 3. Reversed Case (Worst Case Scenario)
            rev_array = list(range(size, 0, -1))
            start = time.perf_counter()
            merge_sort(rev_array)
            end = time.perf_counter()
            print(f"{size:<15}{'Reverse Sorted':<20}{(end - start):.6f} sec")
            print("-----------------------------------------")

if __name__ == "__main__":
    run_benchmarks()
    
    
        