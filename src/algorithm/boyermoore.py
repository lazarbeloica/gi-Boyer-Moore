

class BoyerMoore:
    
    def __init__(self, heuristic_=None, pattern=None, text=None): #TODO add default heuristic
        self.set_heuristic(heuristic_)
        self.set_pattern(pattern)
        self.set_text(text)
        
    def get_heuristic(self):
        return self._heuristic
    
    def set_heuristic(self, heuristic_):
        self._heuristic = heuristic_
        
    def set_text(self, text):
        self._text = text
        
    def get_text(self):
        return self._text
    
    def get_pattern(self):
        return self._pattern
    
    def set_pattern(self, pattern):
        self._pattern = pattern
        
    
    def search(self, heuristic_=None, text=None, pattern=None):
        
        if self.get_heuristic() is None and heuristic_ is None:
            raise Exception('Heuristic must be set')
        
        if self.get_pattern()() is None and pattern is None:
            raise Exception('Pattern must be set')
        
        if self.get_text()() is None and text is None:
            raise Exception('Text must be set')
        
        if heuristic_ is not None:
            self.set_heuristic(heuristic_)
            
        if text is not None:
            self.set_text(text)
            
        if pattern is not None:
            self.set_pattern(pattern)
            
            
        m = len(self.get_pattern())
        n = len(self.get_text())
        s = 0
        
        
        while(s <= n-m):
            j = m-1
            
            while j>=0 and self.get_pattern()[j] == self.get_text()[s+j]:
                j -= 1
                
            if j<0:
                print("Pattern occurs at shift = {}".format(s))
                s += self.get_heuristic().get_shift_pattern_found()
            else:
                s += self.get_heuristic().get_shift_pattern_not_found()        
        
        
    