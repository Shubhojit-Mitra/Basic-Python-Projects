import time
import re

def countdown(user_time):
    seconds = int(user_time.split(':')[0]) * 3600 + int(user_time.split(':')[1]) * 60 + int(user_time.split(':')[2])
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print('Times UP!')

def main():
    user_time = input("Set the Timer (hh:mm:ss): ")
    if re.match(r'^\d{2}:\d{2}:\d{2}$', user_time):
        countdown(user_time)
    else:
        print("Invalid time format. Please try again.")
        main()

if __name__ == '__main__':
    main()