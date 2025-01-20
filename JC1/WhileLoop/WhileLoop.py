#sum = 0
#count = 1
#while (count <= 10):
    #num = int(input("input number"))
    #sum = sum + num
    #count += 1 #+= means plus and assign 

#print (sum)

#Find the sum of all the input numbers until a rogue value (value to end program)  
#is included

sum = 0
num = int(input("input number"))
while (num != 999):
    if num > 0: #ensure that value is integer
        sum = sum + num
    num = int(input("input number")) 

print (f"total sum is {sum}")