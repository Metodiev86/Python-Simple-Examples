import random

option = ("rock", "papper", "scissor")
play = True
while play:
	player = None
	computer = random.choice(option)
	while player not in (option):

		player = input("Въведете rock, papper или scissor: ")

	print(f"Избор на играча: {player}")
	print(f"Избор на компютъра: {computer}")
	if player == computer:
		print("Равен резултат!")
	elif (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "papper")or (player
	                                                                                                    =="papper" and computer == "rock"):
		print("Ти печелиш!")
	else:
		print("Ти губиш!")
	if not input("Още една игра y/n: ").lower() == "y":
		play = False
		print("Благодаря за играта! :)")

