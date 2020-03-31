class sudoku:
    def __init__(self,list):
        self.list = list
        
    @property
    def rows(self):
        return  [x for x in self.list]
        
    @property
    def flatlist(self):
        return [item for sublist in self.list for item in sublist]
    
    @property
    def columns(self):
        return [[j[i] for j in self.list] for i in range(9)] 
        
    @property
    def subsquare(self):
        return [[self.list[i+m][j+n] for n in range(3) for m in range(3)]for i in [0,3,6]for j in [0,3,6]]
    
        
    def check_inrow(self, n, value):
        return True if value not in self.rows[n] else False
    
    def check_incolumn(self, n, value):
        return True if value not in self.columns[n] else False
    
    def check_insubsquare(self, n, value):
        return True if value not in self.subsquare[n] else False
    
    def check_row(self, n):
        numset = set()
        for num in self.rows[n]:
            if num in numset:
                return False
            else:
                numset.add(num)         
        return True

    def check_column(self, n):
        numset = set()
        for num in self.columns[n]:
            if num in numset:
                return False
            else:
                numset.add(num)         
        return True
    def check_subsquare(self, n):
        numset = set()
        for num in self.subsquare[n]:
            if num in numset:
                return False
            else:
                numset.add(num)         
        return True
    
    def check_filled(self):
        for i in range(9):
            if 0 in self.rows[i]:
                return False
        return True
    
    def check_grid(self):
        if not self.check_filled():
            return False
        for i in range(9):
            if (self.check_row(i) == False) or (self.check_column(i) == False) or (self.check_subsquare(i) == False):
                return False
        return True
    