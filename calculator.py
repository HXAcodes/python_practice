#الة حاسبة بسيطة 
print("مرحباً بك في الآلة الحاسبة!") 
num1 = float(input("أدخل الرقم الأول: ")) 
num2 = float(input("أدخل الرقم الثاني: ")) 
operation = input("اختر العملية (+, -, *, /): ") 
if operation == "+": 
    print("النتيجة:", num1 + num2) 
elif operation == "-": 
    print("النتيجة:", num1 - num2) 
elif operation == "*": 
    print("النتيجة:", num1 * num2) 
elif operation == "/": 
    if num2 != 0: 
     print("النتيجة:", num1 / num2) 
    else: 
     print("لا يمكن القسمة على صفر") 
else: 
    print("عملية غير صحيحة")