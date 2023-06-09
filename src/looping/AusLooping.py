#mgs - 2023 looping

#print(any(x % 2 == 0 for x in range(40,100,2) ))
#print(not any(x % 2 == 0 for x in range(40,100,2) ))
#print(all(x % 2 != 0 for x in range(40,100,2) ))

#print(all(x % 2 == 0 for x in range(40,100,2) ))
#print(not all(x % 2 == 0 for x in range(40,100,2) ))
#print(any(x % 2 != 0 for x in range(40,100,2) ))

#print(any(all(y % 2 == 0 
# for y in range(x))
# for x in range(10)))

#print([x * x for x in range(10) if x % 2 == 0])
#print([x * x for x in range(0, 10, 2)])
#print([(x, y, x**2 + y**2)
# for x in range(100)
# for y in range(100)
# if (x**2 + y**2) % 3 == 0 and x**2 % 2 == 0 and y**2 %2 ==0])

print({x * y
        for x in range(10)
        for y in range(10)
        if x * y % 2 == 0})
