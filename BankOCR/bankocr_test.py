import unittest
from bankocr import Ocr

class TestOCR(unittest.TestCase):
    
    def test_ocr_load(self):
        ocr = Ocr()
        
        self.assertIsNotNone(ocr)
    
    def test_decode_scan_of_0(self):
        ocr = Ocr()     
        image = [
            ' _ ', 
            '| |',
            '|_|'
        ]
        
        num = ocr.Scan(image)
        
        self.assertEqual(num, 0, "Should be 0")
        
    def test_decode_scan_of_1(self):
        ocr = Ocr()
        image = [
            '   ', 
            '  |',
            '  |'
        ]
        
        num = ocr.Scan(image)
        
        self.assertEqual(num, 1, "Should be 1")
        
    def test_decode_scan_of_2(self):
        ocr = Ocr()
        image = [
            ' _ ', 
            ' _|',
            '|_ '
        ]
        
        num = ocr.Scan(image)
        
        self.assertEqual(num, 2, "Should be 2")
        
    def test_decode_scan_of_3(self):
        ocr = Ocr()
        image = [
            ' _ ', 
            ' _|',
            ' _|'
        ]
        
        num = ocr.Scan(image)
        
        self.assertEqual(num, 3, "Should be 3")
    
    def test_decode_scan_of_4(self):
        ocr = Ocr()
        image = [
            '   ', 
            '|_|',
            '  |'
        ]
        
        num = ocr.Scan(image)
        
        self.assertEqual(num, 4, "Should be 4")
            