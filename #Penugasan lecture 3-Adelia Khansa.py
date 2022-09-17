#Penugasan lecture 3-Adelia Khansa

answer = input("Whats Greeting ")

new_answer = answer.lower().strip()

if answer == ("hello" or "Hello"):
    print("0$")
elif answer == "hello, newman":
    print("0$")
elif answer.startswith("h"):
    print("20$")
else:
    print("100$")