for i in range(0, 151):
    print(i) #print all intergers 0 - 150

for i in range(5,1001, 5):
    print(i) #print all multiples of 5

for i in range(0, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i) #Counting the Dojo way

sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum) # Whoa that suckers huge!

for i in range(2018,0,-4):
    print(i) #countdown by fours

low = 2
high = 9
mult = 3

for i in range(low, high + 1):
    if i % mult == 0:
        print(i) #Flexible Counter