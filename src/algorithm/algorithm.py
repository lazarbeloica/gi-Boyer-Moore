from abc import ABC, abstractmethod

class Algorithm(ABC):
    
    def __init__(self, pattern=None, text=None):
        self.set_pattern(pattern)
        self.set_text(text)
    
    def set_pattern(self, pattern):
        self._pattern = pattern
        
    def get_pattern(self):
        return self._pattern
        
    def set_text(self, text):
        self._text = text
        
    def get_text(self):
        return self._text
    
    @abstractmethod
    def search_yield(self, text=None, pattern=None, **kwarg):
        pass
    
    @abstractmethod
    def get_results(self, text=None, pattern=None, **kwarg):
        pass
    
    @abstractmethod
    def get_name(self):
        pass