import time


def countdown(timerLenght):
    while timerLenght:
        mins, secs = divmod(timerLenght, 60)
        timer = f"{mins}:{secs}"
        print(timer)
        time.sleep(1)
        timerLenght -= 1


timerLength = int(input("Kaç saniyeden saymasını istiyorsunuz?"))

countdown(timerLength)
