# Day 42: Spelling Checker

from textblob import TextBlob

def spelling_checker():
    word = input("Enter a word: ")

    blob = TextBlob(word)

    correct_word = blob.correct()

    if word != correct_word:
        try_again = input(f"Did you mean {correct_word} (Y/N): ")

        if try_again == "Y":
            print(f"The correct spelling is {correct_word}")
        else:
            spelling_checker()
    else:
        print(word)

spelling_checker()

# Extra Challenge: Set Alarm

import winsound
import datetime
import time

def set_alarm():
    now = datetime.datetime.now()

    target_hour = int(input("Enter the hour: "))
    taget_minute = int(input("Enter the minute: "))

    target_time = datetime.datetime.now().replace(hour=target_hour, minute=taget_minute, second=0, microsecond=0)

    if target_time < now:
        print("Target time already passed for today. Setting for tomorrow.")
        target_time += datetime.timedelta(days=1)
    
    wait_seconds = (target_time - now).total_seconds()
    print(f"Alarm set for {target_time} which is in {wait_seconds} seconds.")

    time.sleep(wait_seconds)
    
    # Play an alarm sound
    print("Alarm time reached!")
    winsound.Beep(1000, 4000)  # Beep at 1000 Hz for 4000 ms


set_alarm()




