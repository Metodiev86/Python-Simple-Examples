#Използване на оператора "For" за цикъл.
import time
for i in range(5):
    print(i)

print("*"*80)
for i in range(5,10): #С два параметъра на матода "range()" се подава диапазона в който да брои
    print(i)

print("*"*80)
for i in range(0,10+1,2): #Третият параметър е през каква стъпка да брои
    print(i)

print("*"*80)
for second in range(10,0,-1):
    print(second)
    time.sleep(1) #Метода "sleep()", на класът time, забавя с определен брой секунди, подадени му като параметър
print("Честита нова година")