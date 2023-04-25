import math

num1 = float(input("Defina o prímeiro número: "))
num2 = float(input("Defina o segundo número: "))
num3 = float(input("Defina o terceiro número: "))
num4 = float(input("Defina o quarto número: "))

x1 = num1
y1 = num2
x2 = num3
y2 = num4

fun = math.sqrt(((x1 + x2)**2) + ((y1 - y2)**2))

if fun >=10:
    fun = math.sqrt(((x1 + x2)**2) + ((y1 - y2)**2))
    print("longe")
else:
    fun = math.sqrt(((x1 + x2)**2) + ((y1 - y2)**2))
    print("perto")

