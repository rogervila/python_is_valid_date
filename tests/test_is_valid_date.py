import unittest
from datetime import date, datetime
from is_valid_date import check


class test_is_valid_date(unittest.TestCase):
    def test_string_dates(self):
        self.assertTrue(check('1714-09-11'))
        self.assertFalse(check('not a date'))

    def test_date_and_datetime_instances(self):
        self.assertTrue(check(date.today()))
        self.assertTrue(check(datetime.now()))

    def test_other_types(self):
        class Foo:
            pass

        values = [b'not a date', {}, [], 288, 42.0, Foo, Foo()]

        for value in values:
            self.assertFalse(check(value))


if __name__ == '__main__':
    unittest.main()
