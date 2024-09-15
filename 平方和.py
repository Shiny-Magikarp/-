import random

# 1. 生成一个随机整数列表
def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# 2. 计算偶数的平方和
def calculate_even_squares_sum(numbers):
    # 使用 filter 过滤出偶数
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    # 使用 map 计算偶数的平方
    squares = list(map(lambda x: x ** 2, evens))
    # 使用 sum 计算平方和
    return sum(squares)

# 主程序
if __name__ == "__main__":
    size = 10  # 列表大小
    lower_bound = 1  # 下界
    upper_bound = 20  # 上界

    random_list = generate_random_list(size, lower_bound, upper_bound)
    print("随机生成的整数列表:", random_list)
    print("列表长度:", len(random_list))  # 使用 len 函数

    even_squares_sum = calculate_even_squares_sum(random_list)
    print("偶数的平方和:", even_squares_sum)