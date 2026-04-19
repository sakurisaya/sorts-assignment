from insertion_sort import insertion_sort
from merge_sort import merge_sort
import random

def main():
    test_data = random.sample(range(20), k=10)
    print("=== テストデータ ===")
    print(test_data)

    print("\n=== 挿入ソート ===")
    print(insertion_sort(test_data.copy()))

    print("\n=== マージソート ===")
    print(merge_sort(test_data.copy()))

if __name__ == "__main__":
    main()