import random

class TicTac:
    
    
    def run(self):
        self.best_x = [' XX', 'X X', 'XX ']
        self.best_o = [' OO', 'O O', 'OO ']
        self.aviliable_coordinates = [1, 2, 3]
        self.empty_cells = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.turn = 0
        self.field = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.x_wins = 'XXX'
        self.o_wins = 'OOO'
        if self.count != 3 or self.count != 4:
            self.printing()
        else:
            self.check_win()
    
    
    def menu(self):
        print("""
What do yo want?
1. Player vs Player
2. Player vs Computer
3. Computer vs Player
4. Computer vs Computer
5. Exit
              """)
        try:
            self.count = int(input())
        except:
            self.menu()
        while self.count != 5:
            if self.count == 2 or self.count == 3:
                print("""Choose level: 
1. Easy
2. Medium""")
            self.level = int(input())
            self.run()
            if self.count == 5:
                break
    def printing(self):
        print('---------')
        print('|', self.field[0], self.field[1], self.field[2], '|')
        print('|', self.field[3], self.field[4], self.field[5], '|')
        print('|', self.field[6], self.field[7], self.field[8], '|')
        print('---------')
        self.check_win()
    
    
    def check_win(self):
        self.horizontal_1 = self.field[0] + self.field[1] + self.field[2]
        self.horizontal_2 = self.field[3] + self.field[4] + self.field[5]
        self.horizontal_3 = self.field[6] + self.field[7] + self.field[8]
        self.vertical_1 = self.field[0] + self.field[3] + self.field[6]
        self.vertical_2 = self.field[1] + self.field[4] + self.field[7]
        self.vertical_3 = self.field[2] + self.field[5] + self.field[8]
        self.diagonal_1 = self.field[0] + self.field[4] + self.field[8]
        self.diagonal_2 = self.field[2] + self.field[4] + self.field[6]
        self.versions = [self.horizontal_1, self.horizontal_2, self.horizontal_3,
                    self.vertical_1, self.vertical_2, self.vertical_3,
                    self.diagonal_1, self.diagonal_2]
        for i in self.versions:
            if i in self.x_wins:
                print("X wins")
                self.menu()
            elif i in self.o_wins:
                print("O wins")
                self.menu()
        if len(self.empty_cells) == 0:
            print("Draw")
            self.menu()
        if self.count == 1:
            self.player()
        elif self.count == 2 and self.level == 2:
            if self.turn % 2 == 0:
                self.player()
            else:
                self.computer_medium()
        elif self.count == 3 and self.level == 2:
            if self.turn % 2 == 0:
                self.computer_medium()
            else:
                self.player()
        elif self.count == 2:
            if self.turn % 2 == 0:
                self.player()
            else:
                self.computer()
        elif self.count == 3:
            if self.turn % 2 == 0:
                self.computer()
            else:
                self.player()
        elif self.count == 4:
            if self.turn % 2 == 0:
                self.computer()
            else:
                self.computer()
        
    
    def player(self):
        try:
            self.a, self.b = list(map(int, input("Enter coordinates: ").split()))
        except:
            print("You should enter numbers!")
            self.player()
        if self.a not in self.aviliable_coordinates and self.b not in self.aviliable_coordinates:
            print("Coordinates should be from 1 to 3!")
            self.player()
        elif self.a == 1 and self.b == 1:
            if 0 in self.empty_cells:
                if self.turn % 2 == 0:
                    self.field[0] = 'X'
                else:
                    self.field[0] = 'O'
                self.empty_cells.remove(0)
            else:
                print("This cell is iccupied! Choose another one!")
                self.player()
        elif self.a == 1 and self.b == 2:
            if 1 in self.empty_cells:
                if self.turn % 2 == 0:
                    self.field[1] = 'X'
                else:
                    self.field[1] = 'O'
                self.empty_cells.remove(1)
            else:
                print("This cell is iccupied! Choose another one!")
                self.player()
        elif self.a == 1 and self.b == 3:
            if 2 in self.empty_cells:
                if self.turn % 2 == 0:
                    self.field[2] = 'X'
                else:
                    self.field[2] = 'O'
                self.empty_cells.remove(2)
            else:
                print("This cell is iccupied! Choose another one!")
                self.player()
        elif self.a == 2 and self.b == 1:
            if 3 in self.empty_cells:
                if self.turn % 2 == 0:
                    self.field[3] = 'X'
                else:
                    self.field[3] = 'O'
                self.empty_cells.remove(3)
            else:
                print("This cell is iccupied! Choose another one!")
                self.player()
        elif self.a == 2 and self.b == 2:
            if 4 in self.empty_cells:
                if self.turn % 2 == 0:
                    self.field[4] = 'X'
                else:
                    self.field[4] = 'O'
                self.empty_cells.remove(4)
            else:
                print("This cell is iccupied! Choose another one!")
                self.player()
        elif self.a == 2 and self.b == 3:
            if 5 in self.empty_cells:
                if self.turn % 2 == 0:
                    self.field[5] = 'X'
                else:
                    self.field[5] = 'O'
                self.empty_cells.remove(5)
            else:
                print("This cell is iccupied! Choose another one!")
                self.player()
        elif self.a == 3 and self.b == 1:
            if 6 in self.empty_cells:
                if self.turn % 2 == 0:
                    self.field[6] = 'X'
                else:
                    self.field[6] = 'O'
                self.empty_cells.remove(6)
            else:
                print("This cell is iccupied! Choose another one!")
                self.player()
        elif self.a == 3 and self.b == 2:
            if 7 in self.empty_cells:
                if self.turn % 2 == 0:
                    self.field[7] = 'X'
                else:
                    self.field[7] = 'O'
                self.empty_cells.remove(7)
            else:
                print("This cell is iccupied! Choose another one!")
                self.player()
        elif self.a == 3 and self.b == 3:
            if 8 in self.empty_cells:
                if self.turn % 2 == 0:
                    self.field[8] = 'X'
                else:
                    self.field[8] = 'O'
                self.empty_cells.remove(8)
            else:
                print("This cell is iccupied! Choose another one!")
                self.player()
        self.turn += 1
        self.printing()
        
    
    def computer(self):
        self.cell = random.choice(self.empty_cells)
        if self.turn % 2 == 0:
            self.field[self.cell] = 'X'
        else:
            self.field[self.cell] = 'O'
        self.empty_cells.remove(self.cell)
        self.turn += 1
        self.printing()
        
    
    def computer_medium(self):
        if self.horizontal_1 in self.best_x:
            for idx,num in enumerate(self.best_x):
                if num == self.horizontal_1:
                    if self.turn % 2 == 0:
                        self.field[idx] = 'X'
                    else:
                        self.field[idx] = 'O'
                    self.empty_cells.remove(idx)
        elif self.horizontal_2 in self.best_x:
            for idx,num in enumerate(self.best_x):
                if num == self.horizontal_2:
                    if self.turn % 2 == 0:
                        self.field[idx + 3] = 'X'
                    else:
                        self.field[idx + 3] = 'O'
                    self.empty_cells.remove(idx + 3)
        elif self.horizontal_3 in self.best_x:
            for idx,num in enumerate(self.best_x):
                if num == self.horizontal_3:
                    if self.turn % 2 == 0:
                        self.field[idx + 6] = 'X'
                    else:
                        self.field[idx + 6] = 'O'
                    self.empty_cells.remove(idx + 6)
        elif self.vertical_1 in self.best_x:
            for idx,num in enumerate(self.best_x):
                if num == self.vertical_1:
                    if self.turn % 2 == 0:
                        self.field[idx * 3] = 'X'
                    else:
                        self.field[idx * 3] = 'O'
                    self.empty_cells.remove(idx * 3)
        elif self.vertical_2 in self.best_x:
            for idx,num in enumerate(self.best_x):
                if num == self.vertical_2:
                    if self.turn % 2 == 0:
                        self.field[idx * 3 + 1] = 'X'
                    else:
                        self.field[idx * 3 + 1] = 'O'
                    self.empty_cells.remove(idx * 3 + 1)
        elif self.vertical_3 in self.best_x:
            for idx,num in enumerate(self.best_x):
                if num == self.vertical_3:
                    if self.turn % 2 == 0:
                        self.field[idx * 3 + 2] = 'X'
                    else:
                        self.field[idx * 3 + 2] = 'O'
                    self.empty_cells.remove(idx * 3 + 2)
        elif self.diagonal_1 in self.best_x:
            for idx,num in enumerate(self.best_x):
                if num == self.diagonal_1:
                    if self.turn % 2 == 0:
                        self.field[idx * 4] = 'X'
                    else:
                        self.field[idx * 4] = 'O'
                    self.empty_cells.remove(idx * 4)
        elif self.diagonal_1 in self.best_x:
            for idx,num in enumerate(self.best_x):
                if num == self.diagonal_1:
                    if self.turn % 2 == 0:
                        self.field[(idx + 1) * 2] = 'X'
                    else:
                        self.field[(idx + 1) * 2] = 'O'
                    self.empty_cells.remove((idx + 1) * 2)
        else:
            self.cell = random.choice(self.empty_cells)
            if self.turn % 2 == 0:
                self.field[self.cell] = 'X'
            else:
                self.field[self.cell] = 'O'
            self.empty_cells.remove(self.cell)
        self.turn += 1
        self.printing()
        
        
tt = TicTac()
tt.menu()

