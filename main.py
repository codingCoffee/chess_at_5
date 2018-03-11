import os, argparse, cv2
import sys


def calc_w_and_b(image):
	white = 0
	black = 0
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			if image[x, y] == 0: white+=1
			else: black+=1
	return white, black
	
def does_piece_exists(image):
	white, black = calc_w_and_b(image)
	# print ('x: '+ str(x) + ' y: ' + str(y) + ' ' + str(abs(white - black)))
	if abs(white - black) > 10000: return 'F'
	else: return 'T'

def thresh_to_fen():
	os.system('clear')
	print('Rough Estimated Piece Detectection')
	chess_board = cv2.imread('thresh_chess.png', cv2.IMREAD_GRAYSCALE)
	square_side = int(chess_board.shape[0]/8)
	old_x = 0
	old_y = 0
	for x in range(8): 
		for y in range(8):
			square = chess_board[
				x*square_side : x*square_side+square_side,
				y*square_side : y*square_side+square_side]
			if x > old_x:
				old_x = x
				print ('')
			sys.stdout.write(str(does_piece_exists(square)))


def cropped_thresh_piece():
	global CHESS_THRESH
	chess_board = cv2.imread('cropped.jpg')
	cv2.imshow('cropped chess board', chess_board)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	chess_board = cv2.cvtColor(chess_board, cv2.COLOR_BGR2GRAY)
	chess_board = cv2.GaussianBlur(chess_board, (5,5), 0)
	cv2.imshow('image',chess_board)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	_, chess_board = cv2.threshold(chess_board,127,255,cv2.THRESH_BINARY)

	cv2.imshow('image',chess_board)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.imwrite('thresh_chess.png',chess_board)
	thresh_to_fen()


if __name__ == "__main__":
	p = argparse.ArgumentParser(description=\
	'Cant come up with anything')
	p.add_argument('--input', type=str, \
			help='input image absolute path (default: input.jpg)')

	args = p.parse_args()
	os.system('cd ../neural-chessboard && python main.py detect --input '+str(args.input)+' --output /home/coding_coffee/Projects/hackathon-18/HACK/chess_at_5/cropped.jpg ')

	cropped_thresh_piece()

'''
python main.py --input /home/coding_coffee/Projects/hackathon-18/HACK/neural-chessboard/test/in/1.jpg
'''