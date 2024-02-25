#Проверка за валидност на номера на кредитна карта:
#1. Премхаваме висчки '-' и празни места ' ', между цифрите.
#2. Събираме всички, числа намиращи се на нечетна позиция от дясо на ляво.
#3. Удвояваме всяка цифра намираща се на четна позиция от дясно наляво:
	#- Ако удвоенот число е двуцифрено разлагаме на две едноцифрени и ги събираме.
#4. След това сумираме новата редица от нечетни позиции.
#5. Събираме двете получени числа от (сумата на нечетните позици и сумата на четните позици).
#6. Извършваме целочислено делене на 10 и ако няма остатък (остатък е 0), номерът на картата е валиден.

sum_odd_digits = 0
sum_even_digits = 0
total = 0

#Step No 1
card_number = input("Въведете номера на своята карта: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]
print(card_number)

#Step 2
for x in card_number[::2]:
		sum_odd_digits = int(sum_odd_digits) + int(x)

#Step 3
for x in card_number[1::2]:
	x = int(x)*2
	if(x>=10):
		sum_even_digits = int(sum_even_digits) + (1 + (int(x) % 10))
	else:
		sum_even_digits = int(sum_even_digits) + int(x)

#Step 4
total = sum_odd_digits + sum_even_digits

#Step 5
if total % 10 == 0:
	print("Картата е валидна!")
else:
	print("Картата е НЕ валидна!")