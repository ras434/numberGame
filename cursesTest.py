import unicurses
begin_x = 20; begin_y = 7
height = 20; width = 40
stdscr = curses.initscr()
stdscr.echo()
win = curses.newwin(height, width, begin_y, begin_x)
