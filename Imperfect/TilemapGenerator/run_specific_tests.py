#!/usr/bin/env python3
"""
Script to run specific categories of tests for the Enemy class.
"""

import unittest
import sys
import os

# Add the test directory to the path
sys.path.append('/tmp/outputs')

from test_enemy import TestEnemy

def run_init_tests():
    """Run all initialization tests."""
    suite = unittest.TestSuite()
    
    # Add all init-related tests
    init_tests = [
        'test_init_no_arguments',
        'test_init_with_valid_type_only',
        'test_init_with_type_and_level_range',
        'test_init_with_level_range_only',
        'test_init_invalid_type',
        'test_init_only_min_level_provided',
        'test_init_only_max_level_provided',
        'test_init_min_level_greater_than_max_level',
        'test_init_min_level_below_zero',
        'test_init_max_level_above_100',
        'test_init_no_enemy_type_in_range',
        'test_init_no_enemy_type_in_valid_range',
        'test_init_boundary_level_values',
        'test_init_equal_min_max_levels',
        'test_init_type_with_narrow_level_range',
        'test_init_type_with_wider_level_range',
        'test_init_all_enemy_types_valid',
        'test_init_random_type_selection',
        'test_init_with_type_case_sensitivity',
        'test_init_with_empty_string_type',
        'test_init_with_whitespace_type',
        'test_init_with_float_levels',
        'test_init_stress_test_random_selection',
        'test_init_with_none_values',
        'test_init_with_boundary_enemy_types',
        'test_init_overlapping_ranges',
        'test_init_with_very_narrow_range'
    ]
    
    for test_name in init_tests:
        suite.addTest(TestEnemy(test_name))
    
    return suite

def run_location_tests():
    """Run all location method tests."""
    suite = unittest.TestSuite()
    
    location_tests = [
        'test_enemy_loc_method',
        'test_enemy_loc_with_various_coordinates',
        'test_enemy_loc_overwrite_location',
        'test_enemy_loc_with_string_coordinates'
    ]
    
    for test_name in location_tests:
        suite.addTest(TestEnemy(test_name))
    
    return suite

def run_integration_tests():
    """Run all integration and behavioral tests."""
    suite = unittest.TestSuite()
    
    integration_tests = [
        'test_multiple_enemy_instances',
        'test_attributes_exist',
        'test_randomization_behavior',
        'test_level_range_filtering_logic',
        'test_level_range_intersection_edge_cases',
        'test_level_range_no_intersection_with_type',
        'test_enemy_attributes_immutability'
    ]
    
    for test_name in integration_tests:
        suite.addTest(TestEnemy(test_name))
    
    return suite

def main():
    """Main function to run specific test categories."""
    if len(sys.argv) < 2:
        print("Usage: python run_specific_tests.py <category>")
        print("Categories: init, location, integration, all")
        sys.exit(1)
    
    category = sys.argv[1].lower()
    
    if category == "init":
        suite = run_init_tests()
        print("Running initialization tests...")
    elif category == "location":
        suite = run_location_tests()
        print("Running location method tests...")
    elif category == "integration":
        suite = run_integration_tests()
        print("Running integration tests...")
    elif category == "all":
        suite = unittest.TestLoader().loadTestsFromTestCase(TestEnemy)
        print("Running all tests...")
    else:
        print(f"Unknown category: {category}")
        print("Available categories: init, location, integration, all")
        sys.exit(1)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print(f"\nTests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("All tests passed! ✅")
    else:
        print("Some tests failed! ❌")
        sys.exit(1)

if __name__ == '__main__':
    main()