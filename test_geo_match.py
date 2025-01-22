import unittest
from geo_match import geo_match

class TestGeoMatch(unittest.TestCase):

    def test_simple_case(self):
        # Input arrays
        array1 = [(42.3601, -71.0589)]  # Boston
        array2 = [(32.7157, -117.1611), (51.5074, -0.1278)]  # San Diego, London

        # Expected result
        expected = [((42.3601, -71.0589), (32.7157, -117.1611))] # Closest is San Diego

        # Assert that the result matches the expected output
        self.assertEqual(geo_match(array1, array2), expected)

    def test_multiple_points(self):
        array1 = [(42.3601, -71.0589), (35.6895, 139.6917)]  # Boston, Tokyo
        array2 = [(32.7157, -117.1611), (51.5074, -0.1278)]  # San Diego, London

        expected =  expected = [
            ((42.3601, -71.0589), (32.7157, -117.1611)),  # Boston -> San Diego
            ((35.6895, 139.6917), (32.7157, -117.1611))     # Tokyo -> San Diego
        ]

        self.assertEqual(geo_match(array1, array2), expected)

    def test_same_arrays(self):
        # Test 3: Boston, San Diego, London in both arrays
        array1 = [(42.3601, -71.0589), (32.7157, -117.1611), (51.5074, -0.1278)]  # Boston, San Diego, London
        array2 = [(42.3601, -71.0589), (32.7157, -117.1611), (51.5074, -0.1278)]  # Same points

        # Each point should match itself
        expected = [
            ((42.3601, -71.0589), (42.3601, -71.0589)),
            ((32.7157, -117.1611), (32.7157, -117.1611)),
            ((51.5074, -0.1278), (51.5074, -0.1278))  
        ]

        self.assertEqual(geo_match(array1, array2), expected)

    
if __name__ == "__main__":
    unittest.main()