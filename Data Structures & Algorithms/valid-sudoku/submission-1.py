class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in range(9):
            row_set = set()
            for i in range(9):
                value = board[row][i]
                if value != '.':
                    if value in row_set:
                        return False
                
                    row_set.add(value)

        for column in range(9):
            column_set = set()
            for i in range(9):
                value = board[i][column]
                if value != '.':
                    if value in column_set:
                        return False
                    
                    column_set.add(value)

        hashmap = {}
        for row in range(9):
            for column in range(9):
                box_row = row // 3
                box_column = column // 3
                if (box_row, box_column) not in hashmap:
                    hashmap[(box_row, box_column)] = set()
                
                if board[row][column] != '.':
                    if board[row][column] in hashmap[(box_row, box_column)]:
                        return False
                    hashmap[(box_row, box_column)].add(board[row][column])
    
        return True