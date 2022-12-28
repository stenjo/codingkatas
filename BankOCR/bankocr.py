# https://codingdojo.org/kata/BankOCR/

import math


class Ocr:
    number = 0
    
    def __init__(self):
        self.number = 0
        
    def ScanDigit(self, lines):
        numbers = [
            ' _ | ||_|', # 0
            '     |  |', # 1
            ' _  _||_ ', # 2
            ' _  _| _|', # 3
            '   |_|  |', # 4
            ' _ |_  _|', # 5
            ' _ |_ |_|', # 6
            ' _   |  |', # 7
            ' _ |_||_|', # 8
            ' _ |_| _|'  # 9
        ]
        
        return  numbers.index("".join(lines))
    
    def ScanLine(self, lines):
        number = 0
        for i in range(math.floor(len(lines[0])/3)):
            number *= 10
            digit = [
                lines[0][i*3:i*3+3], 
                lines[1][i*3:i*3+3], 
                lines[2][i*3:i*3+3]
                ]
            number += self.ScanDigit(digit)

        return number