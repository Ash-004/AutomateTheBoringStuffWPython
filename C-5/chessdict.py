def isValidChessBoard(board):
    countWhitePawn=0
    countBlackPawn=0
    countWhiteKing=0
    countBlackKing=0
    
    for i in board.values():
        if i[0]!="w" and "b":
            print("Hello? Only whites and blacks allowed")
        if i[1:]!="pawn" or "queen" or "king" or "knight" or "bishop" or "rook":
            print("Rnadom ass piece")
            
        if i[0]=="w" and i[1:]=="pawn":
            countWhitePawn+=1
        if i[0]=="b" and i[1:]=="pawn":
            countBlackPawn+=1
            
        if countWhitePawn>8:
            print("wPawn Count off")                
        if countBlackPawn>8:
            print("bPawnn Count off")
            
        
        if i[0]=="w" and i[1:]=="king":
            countWhiteKing+=1
        if i[0]=="b" and i[1:]=="king":
            countBlackKing+=1
            
        if countBlackKing!=1:
            print("check your king, black")
        if countWhiteKing!=1:
            print("check your king, white")
                
            