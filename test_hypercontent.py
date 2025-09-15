# test_hypercontent.py
"""
Tests for HyperContent module.
"""

import unittest
from hypercontent import HyperContent

class TestHyperContent(unittest.TestCase):
    """Test cases for HyperContent class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HyperContent()
        self.assertIsInstance(instance, HyperContent)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HyperContent()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
