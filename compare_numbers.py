#!/user/bin/env python3
# -*- coding: utf-8 -*-
def compare_numbers(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "两者相等"

def main():
    try:
        number1 = float(input("请输入第一个数字："))
        number2 = float(input("请输入第二个数字："))
        result = compare_numbers(number1, number2)
        if result == "两者相等":
            print("两个数字相等。")
        else:
            print(f"较大的数字是：{result}")
    except ValueError:
        print("请输入有效的数字。")

if __name__ == "__main__":
    main()

