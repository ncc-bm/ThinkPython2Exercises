chessBoard = {'1h': 'bking',
             '6c': 'wqueen',
             '2g': 'bbishop',
             '5h': 'bqueen',
             '3e': 'wking'}


def isValidChessBoard(dict):
    #for k, v in dict.items():
    #    print("key is: " + k + ' value is: ' + v)
    #print(list(dict.keys()))
    print('wking' in dict.values())
    

isValidChessBoard(chessBoard)