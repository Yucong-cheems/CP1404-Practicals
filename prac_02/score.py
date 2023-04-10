import random


def main():
    score = float(input("Enter score: "))
    print_score(score)
    generate_random_score()


def print_score(score):
    """print the score"""
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
    return score


def generate_random_score(score):
    """generate a random score"""
    score = random.randint(0, 10)
    print("result: ", score)
    return score
