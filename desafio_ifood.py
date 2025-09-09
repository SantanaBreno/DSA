class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.stack.isEmpty:
            return "Empty"
        return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0
  
# empilhar os elementos do array e verificar se está vazio    
def convert_lisp(string):
    string.split()
    
    
    
