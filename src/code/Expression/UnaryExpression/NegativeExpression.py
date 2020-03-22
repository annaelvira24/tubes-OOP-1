from .UnaryExpression import UnaryExpression

class NegativeExpression(UnaryExpression):
    
    ''' value : TerminalExpression '''
    
    def __init__(self, value):
        super().__init__(value.solve())
    
    def __eq__(self, other):
        if not isinstance(other, NegativeExpression):
            return NotImplemented
        
        return self.solve() == other.solve()
    
    def solve(self):
        return -self.value
