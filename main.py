from insertion_sort.main import main as insertion_sort
from merge_sort.main import main as merge_sort
import timeit
import random
from tabulate import tabulate

test_lists = {
    "Small": [random.randint(0, 1000) for i in range(5000)],
    "Medium": [random.randint(0, 1000) for i in range(10000)],
    "Large": [random.randint(0, 1000) for i in range(30000)],
}


def timsort_sorted(array):
    return sorted(array)


def timsort_sort(array):
    array.sort()


def main():
    table = []
    for key in test_lists:
        table.append(
            [
                key,
                timeit.timeit(lambda: insertion_sort(test_lists[key]), number=10),
                timeit.timeit(lambda: merge_sort(test_lists[key]), number=10),
                timeit.timeit(lambda: timsort_sorted(test_lists[key]), number=10),
                timeit.timeit(lambda: timsort_sort(test_lists[key]), number=10),
            ]
        )

    print(
        tabulate(
            table,
            headers=[
                "List size",
                "Insertion sort",
                "Merge sort",
                "Timsort sorted",
                "Timsort sort",
            ],
        )
    )


if __name__ == "__main__":
    main()
