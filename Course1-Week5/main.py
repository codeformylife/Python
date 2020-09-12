hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
result = 0
if h >40 :
	result = 40 * float(rate)+ ((float(hrs)-40)*(float(rate)*1.5))
print(result)