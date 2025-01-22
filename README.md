# Matching Geolocations (EC530 Assignment 1)
Mission of the module:  If the user gives you two arrays of geo location, match each point in the first array to the closest one in the second array.

---

## How to Add/Run Test Cases

1. Clone this repository.
2. Open the `test_geo_match.py` file.
3. Use the following format to define a new test case:

   ```python
   def test_custom_case(self):
       # Input arrays
       array1 = [(latitude1, longitude1), ...]  # Replace with your points
       array2 = [(latitude2, longitude2), ...]  # Replace with your points

       # Expected result
       expected = [((latitude1, longitude1), (closest_latitude2, closest_longitude2))]
       
       # Assert the result
       self.assertEqual(geo_match(array1, array2), expected)
4. Use the following command to run test cases

   ```python
   python test_geo_match.py

   
