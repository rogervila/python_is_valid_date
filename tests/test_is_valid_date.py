import unittest
from is_valid_date import check
from datetime import date, datetime


class test_is_valid_date(unittest.TestCase):
    def test_string_dates(self):
        self.assertTrue(check('1714-09-11'))
        self.assertFalse(check('not a date'))

    def test_date_and_datetime_instances(self):
        self.assertTrue(check(date.today()))
        self.assertTrue(check(datetime.now()))


if __name__ == '__main__':
    unittest.main()
