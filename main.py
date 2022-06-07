import os


print("""
      Добро пожаловать в казино
      Испытай свою удачку :> 
""")

print("""
Во что хотите поиграть?))
1)Кубики
2)Сгенирировать пароль
3)
""")

Choose = int(input("Что вы выбираете?: "))
if Choose ==1:
      os.system("Clear")
      os.system("python3 cube.py")

elif Choose ==2:
      os.system("clear")
      os.system("python3 generate.py")      

else:
      print("Такого номера нету :/")
