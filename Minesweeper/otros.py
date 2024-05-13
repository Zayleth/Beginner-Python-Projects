def __str__(self): 
        # magic function 
        # controla cómo se muestran como cadenas de texto los objetos de una clase. codigo legible y comprensible
        # lets create a new array that represents what the user would see

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        #-------------------------------------------

            if isinstance(self.board[row][col], str):
                visible_board[row][col] = self.board[row][col]  # Ya es una cadena
            else:
                visible_board[row][col] = str(self.board[row][col])  # Convertir valores que no son cadenas