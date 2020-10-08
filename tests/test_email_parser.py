from src import email_parser
import unittest


class TestEmailParser(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(email_parser.EmailParser.parse('name@gmail.com'), {'username': 'name', 'domain': 'gmail.com'})
        self.assertEqual(email_parser.EmailParser.parse('name+surname@gmail.com'), {'username': 'name+surname', 'domain': 'gmail.com'})
        self.assertEqual(email_parser.EmailParser.parse('adejoke@yahoo.com'), {'username': 'adejoke', 'domain': 'yahoo.com'})

    def test_easy_parse(self):
        self.assertEqual(email_parser.EmailParser.parse('adejoke@hotmail.net'), None)
        self.assertEqual(email_parser.EmailParser.parse('ade#joke@gmail.com'), None)
        self.assertEqual(email_parser.EmailParser.parse('ade_joke@g_mail.com'), None)

    def test_medium_parse(self):
        self.assertEqual(email_parser.EmailParser.parse('1adejoke@gmail.com'), None)
        self.assertEqual(email_parser.EmailParser.parse('123@gmail.com'), None)

    def test_hard_parse(self):
        self.assertEqual(email_parser.EmailParser.parse('adejoke@1gmail.com'), None)
        self.assertEqual(email_parser.EmailParser.parse('adejoke@123.com'), None)

    def test_other_parse(self):
        self.assertEqual(email_parser.EmailParser.parse(''), None)
        self.assertEqual(email_parser.EmailParser.parse('adejoke@1gmail.com'), None)
        self.assertEqual(email_parser.EmailParser.parse('123+rem@456.com'), None)
        self.assertEqual(email_parser.EmailParser.parse('009@900.com'), None)


if __name__ == '__main__':
    unittest.main()
