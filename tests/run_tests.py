import unittest
import sys
import os

# Discover and run all the tests
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
