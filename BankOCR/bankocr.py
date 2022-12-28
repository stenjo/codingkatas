
class Ocr:
    number = 0
    
    def __init__(self):
        self.number = 0
        
    def Scan(self, lines):
        if lines[1] == '|_|' and lines[2] == '  |':
            return 4
        if lines[0] == '   ':
            return 1
        if lines[0] == ' _ ' and lines[1] == ' _|' and lines[2] == ' _|':
            return 3
        if lines[0] == ' _ ' and lines[1] == ' _|':
            return 2
        return 0