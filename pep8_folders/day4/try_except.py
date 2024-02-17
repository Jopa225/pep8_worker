counter = 50000000
try:
    while(1):
        counter -= 1
        res = 6 / counter
except KeyboardInterrupt:
    print(counter)
except Exception:
    print("Dividing by zero rip")


