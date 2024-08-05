#!/user/bin/env python3
# -*- coding: utf-8 -*-
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number = int(input("请输入一个非负整数："))
    if number < 0:
        print("负数没有阶乘。")
    else:
        print(f"{number} 的阶乘是 {factorial(number)}")

if __name__ == "__main__":
    main()