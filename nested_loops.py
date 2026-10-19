#Nested loop is a loop inside annother loop and does the inner lop then repeats it for a sepspific amount of time
print("Nested loop for each number in difernt lines")
#outer loop does a number of times for waht the inner loop is doing
for i in range(2):
    #the innner loop does the repition of what is is printing
    for j in range(1,6):
        print(j)
print("Nested loop for  each number in the same line")
for i in range(2):
    for j in range(1,6):
        print(j,end="")
print()
print("Nested loop for every 5 numbers in difernt lines")
for i in range(2):
    for j in range(1,6):
        print(j,end=" ")
    print()
