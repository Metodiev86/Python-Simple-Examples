#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
import random

#● ┌ ─ ┐ │ └ ┘



dice_art = {1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│ ●       │",
                "│         │",
                "│       ● │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│ ●     ● │",
                "│         │",
                "│ ●     ● │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│ ●     ● │",
                "│    ●    │",
                "│ ●     ● │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│ ●     ● │",
                "│ ●     ● │",
                "│ ●     ● │",
                "└─────────┘")
            }

dise = []
total = 0
num_of_dice = int(input("Колко зара използваме: "))

for die in range(num_of_dice):
  dise.append(random.randint(1,6))
print(dise)

# for die in range(num_of_dice):
#   for line in dice_art.get(dise[die]):
#     print(line, end="")

for line in range(5):
  for die in dise:
    print(dice_art.get(die)[line], end="")
  print()


for die in dise:
  total += die
print (total)