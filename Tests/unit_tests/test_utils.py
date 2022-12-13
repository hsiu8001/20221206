"""
This file demonstrates writing tests using the unittest module.
"""

import django
from django.test import TestCase
import os
import sys

"""
When we use Django, we have to tell it which settings we are using. We do this by using an environment variable, DJANGO_SETTINGS_MODULE. 
This is set in manage.py. We need to explicitly set it for tests to work with pytest.
"""

sys.path.append(os.path.join(os.getcwd(), 'Application'))
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "python_webapp_django.settings"
)
django.setup()

from app.utils import bmi_calculator

class BmiCalculatorTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(BmiCalculatorTest, cls).setUpClass()

    def test_bmi_result_normal(self):
        """Tests bmi result."""
        height = 1.6
        weight = 55
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 21.48)
        self.assertEqual(bmi_means, '健康體位')

    def test_bmi_result_heavy(self):
        """Tests bmi result."""
        height = 1.7
        weight = 75
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 25.95)
        self.assertEqual(bmi_means, '過重')

    def test_bmi_result_light(self):
        """Tests bmi result."""
        height = 1.6
        weight = 40
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 15.62)
        self.assertEqual(bmi_means, '過輕')

    def test_bmi_result_heavy_l1(self):
        """Tests bmi result."""
        height = 1.6
        weight = 70
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 27.34)
        self.assertEqual(bmi_means, '輕度肥胖')

    def test_bmi_result_heavy_l2(self):
        """Tests bmi result."""
        height = 1.6
        weight = 80
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 31.25)
        self.assertEqual(bmi_means, '中度肥胖')    

    def test_bmi_result_heavy_l3(self):
        """Tests bmi result."""
        height = 1.6
        weight = 90
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 35.16)
        self.assertEqual(bmi_means, '重度肥胖')