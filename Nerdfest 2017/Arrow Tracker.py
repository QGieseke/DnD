x = 80
delta = 0
cont = True
print("Welcome to Quinn's Arrow tracker software: version 1.0.0.0")

while (cont):
	print("\nCurrent arrows:" + str(x))
	delta = input("Enter arrows spent: ")
	if (len(delta) == 0):
		delta = 1
	
	if (int(delta) == 0):
		cont = False
	
	x -= int(delta)