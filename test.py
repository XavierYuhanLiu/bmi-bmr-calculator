def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

def calculate_bmr(gender, weight, height, age):
    if gender.lower() == 'female':
        bmr = 655 + 9.6 * weight + 1.7 * height - 4.7 * age
    else:
        bmr = 66 + 13.7 * weight + 5.0 * height - 6.8 * age
    return bmr

def main():
    print("欢迎使用基础代谢率计算器！")
    gender = input("请输入您的性别（male/female）：").strip().lower()
    weight = float(input("请输入您的体重（Kg）：").strip())
    height = float(input("请输入您的身高（cm）：").strip())
    age = int(input("请输入您的年龄（岁）：").strip())

    bmr = calculate_bmr(gender, weight, height, age)
    print(f"您的基础消耗能量（千卡）是：{bmr:.2f}")

if __name__ == "__main__":
    main()