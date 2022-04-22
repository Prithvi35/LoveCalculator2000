print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

comb_names = name1 + name2
lower_names = comb_names

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
digit_1 = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
digit_2 = l + o + v + e

digit_1 = str(digit_1)
digit_2 = str(digit_2)
percentage = digit_1 + digit_2
percentage = int(percentage)

if (percentage<10) or (percentage>90):
  percentage = str(percentage)
  print("Your score is " + percentage + ", you go together like coke and mentos.")
elif (percentage>40) and (percentage<50):
  percentage = str(percentage)
  print("Your score is " + percentage + " you are alright together.")
else:
  percentage = str(percentage)
  print("Your score is " + percentage)



