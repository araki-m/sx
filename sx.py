import curses
import time
import signal
import sys

N_CNT = 20
M_CNT = 24

MIN_NUM = 1
MAX_NUM = 15

MAX_CT = 3 
MAX_RT = 7 

def handler(signal, frame):
        print('Done');
        sys.exit(0)
signal.signal(signal.SIGINT, handler)
 
stdscr = curses.initscr()

def main(stdscr):

    n = N_CNT
    m = M_CNT

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

#1st
    while(True):

        for i in range(MIN_NUM, MAX_NUM):

	    if n == 0:
                break

            n =  n - 1

            stdscr.clear()

            stdscr.addstr(n, m, 'X')
            stdscr.addstr(n, m+1, 'X')
            stdscr.addstr(n+1, m, 'X')
            stdscr.addstr(n+1, m+1, 'X')
            stdscr.addstr(n+2, m, 'X')
            stdscr.addstr(n+2, m+1, 'X')
            stdscr.addstr(n+3, m, 'X',curses.color_pair(1))
            stdscr.addstr(n+3, m+1, 'X',curses.color_pair(1))

            stdscr.addstr(n-1, m+1+MAX_CT, 'X')
            stdscr.addstr(n, m+MAX_CT, 'X')
            stdscr.addstr(n, m+1+MAX_CT, 'X')
            stdscr.addstr(n, m+2+MAX_CT, 'X')
            stdscr.addstr(n+1, m+MAX_CT, 'X')
            stdscr.addstr(n+1, m+1+MAX_CT, 'X')
            stdscr.addstr(n+1, m+2+MAX_CT, 'X')
            stdscr.addstr(n+2, m+MAX_CT, 'X')
            stdscr.addstr(n+2, m+1+MAX_CT, 'X')
            stdscr.addstr(n+2, m+2+MAX_CT, 'X')
            stdscr.addstr(n+3, m+MAX_CT, 'X',curses.color_pair(1))
            stdscr.addstr(n+3, m+1+MAX_CT, 'X',curses.color_pair(1))
            stdscr.addstr(n+3, m+2+MAX_CT, 'X',curses.color_pair(1))

            stdscr.addstr(n, m+MAX_RT, 'X')
            stdscr.addstr(n, m+1+MAX_RT, 'X')
            stdscr.addstr(n+1, m+MAX_RT, 'X')
            stdscr.addstr(n+1, m+1+MAX_RT, 'X')
            stdscr.addstr(n+2, m+MAX_RT, 'X')
            stdscr.addstr(n+2, m+1+MAX_RT, 'X')
            stdscr.addstr(n+3, m+MAX_RT, 'X',curses.color_pair(1))
            stdscr.addstr(n+3, m+1+MAX_RT, 'X',curses.color_pair(1))

            stdscr.refresh()

            time.sleep(0.2)

        #stdscr.getkey()

#1st-2
        for i in range(1, 5):

	    if n == 0:
                break

            n =  n - 1

            stdscr.clear()

            stdscr.addstr(n, m, 'X')
            stdscr.addstr(n, m+1, 'X')
            stdscr.addstr(n+1, m, 'X')
            stdscr.addstr(n+1, m+1, 'X')
            stdscr.addstr(n+2, m, 'X')
            stdscr.addstr(n+2, m+1, 'X')
            stdscr.addstr(n+3, m, 'X',curses.color_pair(1))
            stdscr.addstr(n+3, m+1, 'X',curses.color_pair(1))

            stdscr.addstr(n-1, m+1+MAX_CT, 'X')
            stdscr.addstr(n, m+MAX_CT, 'X')
            stdscr.addstr(n, m+1+MAX_CT, 'X')
            stdscr.addstr(n, m+2+MAX_CT, 'X')
            stdscr.addstr(n+1, m+MAX_CT, 'X')
            stdscr.addstr(n+1, m+1+MAX_CT, 'X')
            stdscr.addstr(n+1, m+2+MAX_CT, 'X')
            stdscr.addstr(n+2, m+MAX_CT, 'X')
            stdscr.addstr(n+2, m+1+MAX_CT, 'X')
            stdscr.addstr(n+2, m+2+MAX_CT, 'X')
            stdscr.addstr(n+3, m+MAX_CT, 'X',curses.color_pair(1))
            stdscr.addstr(n+3, m+1+MAX_CT, 'X',curses.color_pair(1))
            stdscr.addstr(n+3, m+2+MAX_CT, 'X',curses.color_pair(1))

            stdscr.addstr(n, m+MAX_RT, 'X')
            stdscr.addstr(n, m+1+MAX_RT, 'X')
            stdscr.addstr(n+1, m+MAX_RT, 'X')
            stdscr.addstr(n+1, m+1+MAX_RT, 'X')
            stdscr.addstr(n+2, m+MAX_RT, 'X')
            stdscr.addstr(n+2, m+1+MAX_RT, 'X')
            stdscr.addstr(n+3, m+MAX_RT, 'X',curses.color_pair(1))
            stdscr.addstr(n+3, m+1+MAX_RT, 'X',curses.color_pair(1))

            stdscr.refresh()

            time.sleep(0.2)

        #stdscr.getkey()

#2nd-before
 
        for i in range(1, 5):

            n =  n + 1

            stdscr.clear()
            stdscr.addstr(n, m, 'X')
            stdscr.addstr(n, m+1, 'X')
            stdscr.addstr(n+1, m, 'X')
            stdscr.addstr(n+1, m+1, 'X')
            stdscr.addstr(n+2, m, 'X')
            stdscr.addstr(n+2, m+1, 'X')
            stdscr.addstr(n+3, m, 'X',curses.color_pair(2))
            stdscr.addstr(n+3, m+1, 'X',curses.color_pair(2))

#

            stdscr.addstr(n, m+MAX_RT, 'X')
            stdscr.addstr(n, m+1+MAX_RT, 'X')
            stdscr.addstr(n+1, m+MAX_RT, 'X')
            stdscr.addstr(n+1, m+1+MAX_RT, 'X')
            stdscr.addstr(n+2, m+MAX_RT, 'X')
            stdscr.addstr(n+2, m+1+MAX_RT, 'X')
            stdscr.addstr(n+3, m+MAX_RT, 'X',curses.color_pair(2))
            stdscr.addstr(n+3, m+1+MAX_RT, 'X',curses.color_pair(2))

            stdscr.refresh()

            time.sleep(0.3)

#2nd
        for i in range(MIN_NUM, MAX_NUM):

            n =  n + 1

            stdscr.clear()
            stdscr.addstr(n, m, 'X')
            stdscr.addstr(n, m+1, 'X')
            stdscr.addstr(n+1, m, 'X')
            stdscr.addstr(n+1, m+1, 'X')
            stdscr.addstr(n+2, m, 'X')
            stdscr.addstr(n+2, m+1, 'X')
            stdscr.addstr(n+3, m, 'X',curses.color_pair(2))
            stdscr.addstr(n+3, m+1, 'X',curses.color_pair(2))

#

            stdscr.addstr(n, m+MAX_RT, 'X')
            stdscr.addstr(n, m+1+MAX_RT, 'X')
            stdscr.addstr(n+1, m+MAX_RT, 'X')
            stdscr.addstr(n+1, m+1+MAX_RT, 'X')
            stdscr.addstr(n+2, m+MAX_RT, 'X')
            stdscr.addstr(n+2, m+1+MAX_RT, 'X')
            stdscr.addstr(n+3, m+MAX_RT, 'X',curses.color_pair(2))
            stdscr.addstr(n+3, m+1+MAX_RT, 'X',curses.color_pair(2))

            stdscr.refresh()

            time.sleep(0.3)

    pass

if __name__ == '__main__':
    curses.wrapper(main)
