import os, argparse, cv2



def cropped_thresh_piece():
	chess_board = cv2.imread('cropped.jpg')
	cv2.imshow('cropped chess board', chess_board)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


	chess_board = cv2.cvtColor(chess_board, cv2.COLOR_BGR2GRAY)
	chess_board = cv2.GaussianBlur(chess_board, (5,5), 0)
	_, chess_board = cv2.threshold(chess_board,127,255,cv2.THRESH_BINARY)

	cv2.imshow('image',chess_board)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.imwrite('thresh_chess.png',chess_board)



if __name__ == "__main__":
	p = argparse.ArgumentParser(description=\
	'Cant come up with anything')
	p.add_argument('--input', type=str, \
			help='input image absolute path (default: input.jpg)')
	p.add_argument('--output', type=str, \
			help='output path absolute path (default: output.jpg)')

	args = p.parse_args()
	os.system('cd ../neural-chessboard && python main.py detect --input '+str(args.input)+' --output '+str(args.output))

	cropped_thresh_piece()

'''
python main.py --input /home/coding_coffee/Projects/hackathon-18/HACK/neural-chessboard/test/in/1.jpg --output /home/coding_coffee/Projects/hackathon-18/HACK/chess_at_5/cropped.jpg
'''