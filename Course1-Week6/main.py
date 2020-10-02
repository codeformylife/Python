def computepay(h,r):
    result=0
    if(h>40):
        result = 40*r +(h-40)*(r*1.5)
    return result

hrs = input("Enter Hours:")
rate = input("Enter rate:")
hrs= float(hrs)
rate= float(rate)
p = computepay(hrs,rate)
print("Pay",p)