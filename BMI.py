def BMI(weight, height):  
    bmi = weight / (height ** 2)  
    print("BMI指数：" + str(bmi))  
    if bmi < 18.5:  
        print("偏瘦")  
    elif 18.5 <= bmi < 25:  
        print("正常")  
    elif 25 <= bmi < 30:  
        print("偏胖")  
    else:  
        print("肥胖")  
    return bmi  

try:  
    input_weight = float(input("请输入体重(kg):"))  
    input_height = float(input("请输入身高(m):"))  
    result = BMI(input_weight, input_height)  
except ValueError:  
    print("请输入有效的数字。")  