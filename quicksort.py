#!/user/bin/env python3
# -*- coding: utf-8 -*-
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def main():
    try:
        arr = input("请输入一组数字，用空格分隔：").split()
        arr = [int(x) for x in arr]
        sorted_arr = quicksort(arr)
        print("排序后的数组：", sorted_arr)
    except ValueError:
        print("请输入有效的数字。")

if __name__ == "__main__":
    main()