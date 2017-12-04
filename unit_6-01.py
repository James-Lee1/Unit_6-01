# Created by: James Lee
# Created on: Nov 2017
# Created for: ICS3U
# This program displays an enumerated type

from enum import Enum

# an enumerated type of days of the week
Days = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

day_selected = int(input('Enter the number that corresponds to your favorite day of the week: '))

try:
    if Days[day_selected - 1] in Days:
        print('Your favorite day of the week is: ')
        print(Days[day_of_the_week_selected - 1])
except:
    print("Please enter a valid number")
