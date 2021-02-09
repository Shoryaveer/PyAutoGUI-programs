import pyautogui as pg
import os
import csv
import time
import sys


def tab():
    pg.press(['tab'], interval=0.10)


def MCQ(option):
    try:
        option = int(option)
    except ValueError:
        pass

    if option == 1 :
        pg.press(['space'])

    elif option > 1 :
        press_lst = ['right']
        press_lst *= option
        pg.press(press_lst)


def kill(sec):
    for rem in range(sec, 0, -1) :
        st = f'{rem} seconds remaining'
        print(st, end='')
        time.sleep(1)
        print('\b'*len(st), end='', flush=True)


# link address
lnk_addrs = r'https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform'

# # directory of CSV
# os.chdir(r'.\form project')
# print('Dir changed')


file_in = open('form data.txt', 'r')  # open CSV
print('file opened')

print('Make sure the form is in view')

kill(5)

data = csv.reader(file_in)  # getting CSV object

# constants
itr_no = 0  # for debug
brk = False  # master break
sintrvl = 0.04  # samll interval
lintrvl = 0.05  # large interval

while True:  # true until file ends

    if brk:  # master break
        break

    file_in.seek(0)  # seek zero if run again is engaged

    try:
        for fill in data:  # getting the data list from CSV

            if not fill:  # if empty activate master break
                brk = True
                break

            # name
            name_pos = pg.locateOnScreen('1_name.PNG')  # finding initial field
            pg.click(name_pos[0] + 10 , name_pos[1]+(name_pos[3] - 30))  # clicking initial field
            pg.typewrite(fill[0], interval=lintrvl)  # filling initial field using csv[0]

            # greatest fears
            tab()
            pg.typewrite(fill[1], interval = lintrvl) #writing field

            # wizard power
            tab()
            pg.press(fill[2][0:1]) # pressing the first letter of the choice due to unique fields

            # robocop
            tab()
            MCQ(fill[3])

            # add comments
            tab()
            if fill[3] != '0' :
                tab() #to jump clear selection
            pg.typewrite(fill[4], interval = sintrvl)

            # submit
            tab()
            pg.press(['enter'])

            itr_no += 1 #iteration number inc.

            # reopen the form
            adrs_pos = pg.locateOnScreen('2_lock.PNG')
            pg.click(adrs_pos[0] + 60, adrs_pos[1] + 20 )
            pg.typewrite(lnk_addrs)
            pg.press(['enter'])

            kill(3)


    except Exception as error_name :

        exc_type, exc_obj, tb = sys.exc_info()
        print(f'Error {error_name} on line {tb.tb_lineno} of itr {itr_no}')

        choose = input('Run again(r), Quit(q), Stay(s) --> ')

        if choose == 'r' :
            continue
        elif choose == 'q' :
            break
        elif choose == 's' :
            while True : #to see input infinite loop
                pass
        else :
            while True : #to see input infinite loop
                pass
