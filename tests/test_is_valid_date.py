import unittest
from is_valid_date import check


class test_is_valid_date(unittest.TestCase):
    def test_dates(self):
        self.assertTrue(check('1714-09-11'))
        self.assertFalse(check('not a date'))


if __name__ == '__main__':
    unittest.main()
