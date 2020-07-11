
import curses
import curses.panel
from curses.textpad import Textbox, rectangle

def curmain(stdscr):
	stdscr = curses.initscr()
	stdscr.clear()
	stdscr.keypad(True) # Sppport keypad functional keys
	#curses.noecho()
	#curses.cbreak()
	
	# Clear screen
	
	win_log = curses.newwin(curses.LINES-3,curses.COLS-2, 1,1)
	win_log.addstr(0, 0, "Current mode: Typing mode\n", curses.A_REVERSE)
	rectangle(stdscr, 0,0, curses.LINES-2, curses.COLS-1)
	win_com = curses.newwin(1,curses.COLS-1, curses.LINES-1,1)
	stdscr.addstr(curses.LINES-1, 0, ">")
	stdscr.refresh()
	win_log.refresh()
	
	#stdscr.getkey()
	#log = Textbox(win_log)
	com = Textbox(win_com)
	#log.edit()
	y = 0
	x = 0
	
	while(True):
		# Let the user edit until Ctrl-G is struck.
		com.edit()
		# Get resulting contents
		message = com.gather()
		#curses.nocbreak()
		win_log.addstr(message, curses.A_REVERSE)
		win_log.addstr("\n", curses.A_REVERSE)
		win_log.refresh()
		win_com.clear()
		
		resize = curses.is_term_resized(y, x)
		if resize:
			y, x = stdscr.getmaxyx()
			stdscr.clear()
			curses.resizeterm(y, x)
			stdscr.refresh()
		
	stdscr.keypad(False)
	#curses.echo()
	curses.endwin()


curses.wrapper(curmain)
