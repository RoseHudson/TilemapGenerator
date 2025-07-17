#!/usr/bin/env python3
"""
Test runner for Enemy class unit tests.
This script runs all the unit tests and provides a summary of the results.
"""

import unittest
import sys
import os

# Add the test directory to the path
sys.path.append('/tmp/outputs')

# Import the test module
from test_enemy import TestEnemy

def run_tests():
    """Run all tests and return the results."""
    # Create a test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestEnemy)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    
    return result

if __name__ == '__main__':
    print("Running comprehensive unit tests for Enemy class...")
    print("=" * 60)
    
    result = run_tests()
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\nAll tests passed successfully! ✅")
        sys.exit(0)
    else:
        print("\nSome tests failed! ❌")
        sys.exit(1)