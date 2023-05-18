from logo wordlist stages import logo_calc 

def addition (n1, n2):
  """add given two numbers"""
  return n1 + n2 

def subtraction (n1, n2):
  """subtracts given two numbers"""
  return n1 - n2 

def mutiply(n1, n2):
   """multiply given two numbers"""
  return n1 * n2 

def divide(n1, n2):
   """divide given two numbers"""
  return ni / n2

operations = {
  "+" : addition,
  "-" : subtraction,
  "*"  : mutiply,
  "/" : divide
}

def caculator():
  print(logo_calc)
  num1 = input("Enter the first number : ")
  for symbol in opertaions:
    print(symnol)
  should_continue = True
  while should_continue:
    operator = input("please select any operation : ")
    num2 = input("Please enter another number : ")
    caculation_function = operations[operator]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operator} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit : ").lower() == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
     
calculator()
