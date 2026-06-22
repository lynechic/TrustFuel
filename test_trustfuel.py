# test_trustfuel.py
"""
Tests for TrustFuel module.
"""

import unittest
from trustfuel import TrustFuel

class TestTrustFuel(unittest.TestCase):
    """Test cases for TrustFuel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrustFuel()
        self.assertIsInstance(instance, TrustFuel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrustFuel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
