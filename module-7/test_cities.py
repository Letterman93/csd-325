# ---------------------------------------------------------------
# Author:       Zak Nizam
# Date:         02/05/2026
# Course:       CSD325 - Advanced Python
# Assignment:   Module 7.2 – Test Cases
#
# Purpose:
#   Contains unit tests for the city_country function to verify
#   correct formatting and handling of optional parameters.
# ---------------------------------------------------------------

import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(
            city_country("Santiago", "Chile"),
            "Santiago, Chile"
        )

    def test_city_country_population(self):
        self.assertEqual(
            city_country("Santiago", "Chile", 5000000),
            "Santiago, Chile - population 5000000"
        )

    def test_city_country_population_language(self):
        self.assertEqual(
            city_country("Santiago", "Chile", 5000000, "Spanish"),
            "Santiago, Chile - population 5000000, Spanish"
        )


if __name__ == "__main__":
    unittest.main()
