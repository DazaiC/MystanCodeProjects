"""
File: my_drawing
Name: Dazai
----------------------
TODO: Use basic shape to make an abstract collage-art
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc
from campy.graphics.gwindow import GWindow

WIDTH = 627
HEIGHT = 813

def main():
    """
    TODO:
    """
    window = GWindow(WIDTH, HEIGHT)

    y_rect = GRect(147, HEIGHT)
    y_rect.filled = True
    y_rect.fill_color = 'orange'
    y_rect.color = 'orange'
    window.add(y_rect)

    y_arc = GArc(250, 500, 0, 180)
    window.add(y_arc, x=20, y=535)
    y_arc2 = GArc(240, 480, 0, 180)
    y_arc2.filled = True
    window.add(y_arc2, x=25, y=540)

    p_rect = GRect(309, 278)
    p_rect.filled = True
    p_rect.fill_color = 'purple'
    p_rect.color = 'purple'
    window.add(p_rect, x=169, y=17)
    p_cir = GOval(250, 250)
    p_cir.filled = True
    window.add(p_cir, x=200, y=30)
    p_cir2 = GOval(240, 240)
    p_cir2.filled = True
    p_cir2.fill_color = 'purple'
    window.add(p_cir2, x=205, y=35)

    r_rect = GRect(WIDTH-30, 122)
    r_rect.filled = True
    r_rect.fill_color = 'red'
    r_rect.color = 'red'
    window.add(r_rect, x=0, y=402)

    b_rect = GRect(134, HEIGHT)
    b_rect.filled = True
    b_rect.fill_color = 'blue'
    b_rect.color = 'blue'
    window.add(b_rect, x=478, y=17)

    up_black = GRect(WIDTH, 17)
    up_black.filled = True
    up_black.fill_color = 'black'
    up_black.color = 'black'
    window.add(up_black)

    down_black = GRect(WIDTH, 17)
    down_black.filled = True
    down_black.fill_color = 'black'
    down_black.color = 'black'
    window.add(down_black, x=0, y=HEIGHT-18)

    right_black = GRect(12, HEIGHT)
    right_black.filled = True
    right_black.fill_color = 'black'
    right_black.color = 'black'
    window.add(right_black)

    left_black = GRect(13, HEIGHT)
    left_black.filled = True
    left_black.fill_color = 'black'
    left_black.color = 'black'
    window.add(left_black, x=WIDTH-14, y=0)

    r2 = GRect(80, 80)
    r2.filled = True
    window.add(r2, x=(window.width - r2.width) / 2 - 38, y=(window.height - r2.height) / 2 - 38)
    r2_b = GRect(74, 74)
    r2_b.filled = True
    r2_b.fill_color = 'blue'
    window.add(r2_b, x=(window.width-r2.width)/2 - 35, y=(window.height-r2.height)/2 - 35)


    r1 = GRect(80, 80)
    r1.filled = True
    window.add(r1, x=(window.width-r1.width)/2, y=(window.height-r1.height)/2)
    r1_y = GRect(74, 74)
    r1_y.filled = True
    r1_y.fill_color = 'orange'
    window.add(r1_y, x=(window.width - r1.width) / 2 + 3, y=(window.height - r1.height) / 2 + 3)

    g1 = GRect(80, 80)
    g1.filled = True
    window.add(g1, x=(window.width - r1.width) / 2 + 35, y=(window.height - r1.height) / 2 + 35)
    g1_g = GRect(74, 74)
    g1_g.filled = True
    g1_g.fill_color = 'green'
    window.add(g1_g, x=(window.width - r1.width) / 2 + 38, y=(window.height - r1.height) / 2 + 38)

if __name__ == '__main__':
    main()
