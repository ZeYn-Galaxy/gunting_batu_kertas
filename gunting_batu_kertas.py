import random

def play():
    user = input("gunting(g), batu(b), kertas(k)\n")
    computer = random.choice(['g','b','k'])

    if (user == computer):
        return "Seri!\n" + "Kamu: " + user + "\nComputer: " + computer
    
    if (penentuan(user, computer)):
        return "Kamu Menang!\n" + "Kamu: " + user + "\nComputer: " + computer
    return "Kamu Kalah\n" + "Kamu: " + user + "\nComputer: " + computer

def penentuan(user, computer):
    if (user == "g" and computer == "k") or (user == "b" and computer == "g") or (user == "k" and computer == "b"):
        return True
    else:
        return False
            

print(play())