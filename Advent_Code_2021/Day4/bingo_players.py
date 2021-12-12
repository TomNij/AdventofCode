import numpy as np
import time


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(time.time()-t) + ' sec')
        return ret
    return wrapper_method

with open('../Input_files/4.txt') as file:
    input = file.read().split('\n\n')

#input 0 are the nrs that will be drawn 1-100 are the bingo boards
#how to track if a nr was drawn:
#if drawn make those ind 0
#check row/col for all zeroes
#if true multiply sum of board (non zeroes) with last nr
@profiler
def part_12():
    bingo_boards = np.zeros((5,5,100),dtype=int)
    for board_ind,board in enumerate(input[1:len(input)]):
        #reddit, use empty split arg to split on any whitespace char!
        board = [list(map(int, l.split())) for l in board.split('\n')]

        for row_ind in range(len(board)):
            for col_ind in range(len(board[0])):
                try:
                    bingo_boards[row_ind,col_ind,board_ind] = int(board[row_ind][col_ind])
                except(ValueError):
                    a= 1

    bingo_list = list(map(int,input[0].split(',')))
    non_bingo_boards = list(range(100))
    print_bingos = True
    for ball_ind,ball_val in enumerate(bingo_list):
        #mark nrs with -1 since 0 is also on the board
        bingo_boards[bingo_boards == ball_val] = -1
        for board_ind in non_bingo_boards:
            #rowwise and colwise sums
            if -5 in np.sum(bingo_boards[:, :, board_ind], 0) or -5 in np.sum(bingo_boards[:, :, board_ind], 1):
                #bingo found
                if print_bingos:
                    not_min1_ind = bingo_boards[:, :, board_ind] != -1
                    board_sum = np.sum(bingo_boards[not_min1_ind, board_ind])
                    print(f"Part 1:{ball_val*board_sum}")
                print_bingos = False

                if len(non_bingo_boards) == 1:
                    not_min1_ind = bingo_boards[:, :, board_ind] != -1
                    board_sum = np.sum(bingo_boards[not_min1_ind, board_ind])
                    print(f"Part 2:{ball_val*board_sum}")
                non_bingo_boards.remove(board_ind)

if __name__ == "__main__":
    part_12()