
def time(timeVal, step):
    if timeVal > 0:
        return 0.1 + time(timeVal-step, step)
    else: 
        return 0.0

print(time(2, 0.1))
