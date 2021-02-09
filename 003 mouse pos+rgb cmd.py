import pyautogui as pg


while True:
    x, y = pg.position()
    R, G, B = pg.screenshot().getpixel(pg.position())
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    rgb = '  R: ' + str(R).rjust(3) + ' G: ' + str(G).rjust(3) + ' B: ' + str(B).rjust(3)
    positionStr += rgb
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)
