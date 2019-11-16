import unittest
import webstatus


class MyTestCase(unittest.TestCase):
    def __prepare_no_redirect_url_list(self):
        urls = ["http://www.google.com", "http://www.google.pl", "https://www.onet.pl", "https://www.wp.pl",
                "https://jenkins.io", "https://stackoverflow.com"]
        return urls

    def __prepare_redirect_url_list(self):
        urls = ["http://google.com", "http://google.pl", "http://onet.pl", "http://www.wp.pl", "http://jenkins.io",
                "http://stackoverflow.com"]
        return urls

    def test_url_status_no_redirect_url_no_follow_status_eq_200(self):
        urls = self.__prepare_no_redirect_url_list()
        follow = False

        for url in urls:
            result = webstatus.Main().url_status(url, follow)
            self.assertEqual(200, result)

    def test_url_status_redirect_url_follow_status_eq_200(self):
        urls = self.__prepare_redirect_url_list()
        follow = True

        for url in urls:
            result = webstatus.Main().url_status(url, follow)
            self.assertEqual(200, result)

    def test_url_status_redirect_url_no_follow_status_eq_301(self):
        urls = self.__prepare_redirect_url_list()
        follow = False

        for url in urls:
            result = webstatus.Main().url_status(url, follow)
            self.assertEqual(301, result)


if __name__ == '__main__':
    unittest.main()

