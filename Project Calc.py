def calc():
 try:
    number1 = float(input("Please input the first number:"))
 except ValueError:
    print("❌ Invalid number!")

 answer = number1
 print("Your answer is ", answer)


 try:
  while True:
     operation = input("Please choose any of this functions: +, -, x, / or input q to quit")

     if operation == "+":
         try:
            number2 = float(input("Please input the next number:"))
         except ValueError:
             print("❌ Invalid number!")
             break
         answer += number2

     elif operation == "-":
         try:
            number2 = float(input("Please input the next number:"))
         except ValueError:
             print("❌ Invalid number!")
             break
         answer = answer - number2

     elif operation == "x":
         try:
            number2 = float(input("Please input the next number:"))
         except ValueError:
             print("❌ Invalid number!")
             break
         answer = answer * number2

     elif operation == "/":
         try:
            number2 = float(input("Please input the next number:"))
         except ValueError:
             print("❌ Invalid number!")
             break
         try:
             answer = answer / number2
         except ZeroDivisionError:
             print("No number can be divided by 0")
             continue

     elif operation == "q":
         break
    
     else:
         print("This is not an operation")

 except ValueError:
    print("This is not an integer")

 print("Your answer is ", answer)



while True:
       calc()
       per = str(input("Do you want to perform another calculation: Yes/No"))
         
       if per == "Yes":
          calc
       elif per == "No":
          break
       else:
          print("❌ The input is not valid!")
