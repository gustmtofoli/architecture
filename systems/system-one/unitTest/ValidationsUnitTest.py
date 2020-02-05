import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest
from validations import Validations as validations

class ValidationsUnitTes(unittest.TestCase):
    
    def test_validCpf(self):
        self.assertTrue(validations.isValidCpf("22544050047"))
    
    def test_invalidCpf(self):
        self.assertFalse(validations.isValidCpf("12345"))

if __name__ == '__main__':
    unittest.main()