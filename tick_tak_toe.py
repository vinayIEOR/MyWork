import numpy as np


class Tic_tac_toe():
    """this is Tic Tac Toe game now Enjiy this Game"""
    def __init__(self):
        print("game is start now follow rule for play game")
        print("""Rule:
         locatiob of game[00, 01, 02
                          10 ,11, 12
                          20 ,21, 22 ]
        enter the location and for entry      
        game always start with player 1 and next entry input 
        by player2 and so on upto one player not win
        write name and . PlayGame""")

        self.game= np.empty((3,3))
        self.count=0
    
    def PlayGame(self):
        if self.count==0 or self.count%2 ==0:
            print(self.game)
            loc= input("enter the location for entry player 1 separated by comma ',' :")
            loc_list=loc.split(sep=',')
            if self.game[int(loc_list[0]),int(loc_list[1])]<1:
                self.game[int(loc_list[0]),int(loc_list[1])]=1
                self.count+=1
            else:
                print("you can not replace entry")
            
        else:
            print(self.game)
            loc=input("enter the location for entry player 2 separated by comma ',' :")
            loc_list=loc.split(sep=',')
            if self.game[int(loc_list[0]),int(loc_list[1])]<=1:
                self.game[int(loc_list[0]),int(loc_list[1])]=2
                self.count+=1
            else:
                print("you can not replace entry")
                
        self.CheckGame()
    
    
    
    def RowCheck(self):
        for i in range(3):
            if len(np.unique(self.game[i]))==1 and self.game[i,0]!=0:
                return self.game[i,0]
        return 0
    def ColumnCheck(self):
        self.gameTr=np.transpose(self.game)
        for i in range(3):
            if len(np.unique(self.gameTr[i]))==1 and self.game[i,0]!=0:
                return self.gameTr[i,0]
        return 0
    def DiagonalCheck(self):
        if self.game[0,0]==self.game[1,1]==self.game[2,2] or self.game[0,2]==self.game[1,1]==self.game[2,0] and self.game[0,0]!=0:
            return self.game[1,1]
        return 0
    
    def CheckGame(self):
        if self.RowCheck()>0:
            print("player "+str(self.RowCheck())+" win")
        elif self.ColumnCheck()>0:
            print("player "+str(self.ColumnCheck())+" win")
        elif self.DiagonalCheck()>0:
            print("player "+str(self.DiagonalCheck())+" win") 
        else:
            print("Game is ONN")
            if self.count<=8:
                self.PlayGame()
            else:
                print("game draw")
        
vinay=Tic_tac_toe()
vinay.PlayGame()