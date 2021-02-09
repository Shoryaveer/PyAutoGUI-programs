import pyautogui as pg


def main():

    dist = 200

    while dist > 0:
        pg.dragRel(dist, 0)
        pg.dragRel(0, dist)
        dist -= 5
        pg.dragRel(-dist, 0)
        pg.dragRel(0, -dist)
        dist -= 5


main()
