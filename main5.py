import random

MOVES = ["rock", "paper", "scissor"]
NAME = input("\nEnter your name: ")
win = lose = draw = 0

while True:
    print("\nEnter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    try:
        user_choice = int(input("\nEnter choice: "))
        if user_choice in [1, 2, 3]:
            user_choice = MOVES[user_choice-1]
        else:
            print("\nInvalid choice. Please try again.\n")
            continue
    except:
        print("\nInvalid choice. Please try again.\n")
        continue
    comp_choice = random.choice(MOVES)
    print(f"\n{NAME} chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")
    for i, j in enumerate(MOVES):
        if user_choice == j:
            if comp_choice == j: 
                print("\nDRAW"); draw += 1
            elif comp_choice == MOVES[(i+1)%3]: 
                print("\nYOU LOSE"); lose += 1
            else: 
                print("\nYOU WIN"); win += 1
    while True:
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again in ['y', 'n']:
            break
        else:
            print("\nInvalid choice. Please try again.\n")
            continue
    if play_again == 'n':
        break

print(f"\n\n{NAME}'s SCORE:")
print(f"WINS  : {win}")
print(f"LOSSES: {lose}")
print(f"DRAWS : {draw}\n")