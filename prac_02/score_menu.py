def main():
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input(">>>Enter choice: ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_score()
            print(score)
        elif choice == "P":
            print_score(score)
        elif choice == "S":
            print_star(score)
        else:
            print("Invalid input!")
        print(MENU)
        choice = input(">>>Enter choice: ").upper()


def print_star(score):
    """print star"""
    print(score * "*")


def get_score():
    """get valid score"""
    score = float(input("Enter a score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = float(input("Enter a score: "))
    return int(score)


def print_score(score):
    """print score"""
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        if score > 50:
            print("Passable")
        if score > 90:
            print("Excellent")
    if score <= 50:
        print("Bad")


main()