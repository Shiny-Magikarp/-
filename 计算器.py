def Calculator(num1, num2, operator):
    if operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    elif operator == '*':
        ans = num1 * num2
    elif operator == '/':
        ans = num1 / num2
    return ans

try:
    m = float(input("请输入参与运算的第一个数:"))
    n = float(input("请输入参与运算的第二个数:"))
    o = str(input("请输入运算符:"))
    a = Calculator(m,n,o)
    print("运算的结果为:",a)
except ValueError:
    print("请输入有效的数字。")