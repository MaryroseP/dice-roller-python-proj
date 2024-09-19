import random

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
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
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []   # list
total = 0
num_of_dice = 3 #int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for line in range(5): # for each line
    for die in dice: # for each die in the list (dice)
        print(dice_art.get(die)[line], end="") # print the dice art for the die by line next to each other
    print() # print a newline so another line of the dice art can be printed

# ┌─────────┐< line art of the first die ┌─────────┐< line art of the second die ┌─────────┐< last die


for die in dice:
    total += die

print(f"Total: {total}")