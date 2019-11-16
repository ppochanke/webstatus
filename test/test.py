import unittest
import webstatus


class MyTestCase(unittest.TestCase):

    def test_url_status_correct_url_no_follow(self):
        url = "http://www.google.com"
        follow = False
        result = webstatus.Main().url_status(url, follow)
        self.assertEqual(200, result)

    def test_url_status_incorrect_url_no_follow(self):
        url = "http://google.com"
        follow = False
        result = webstatus.Main().url_status(url, follow)
        self.assertNotEqual(200, result)

    def test_url_status_correct_url_follow(self):
        url = "http://google.com"
        follow = True
        result = webstatus.Main().url_status(url, follow)
        self.assertEqual(200, result)


if __name__ == '__main__':
    unittest.main()


