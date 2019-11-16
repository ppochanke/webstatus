import argparse
import requests


class Main:
    site: str = ''
    follow: bool = False

    def parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--url", type=str, required=True, help="Site url")
        parser.add_argument("-f", "--follow-redirects", action='store_true', help="Show status after redirects")
        args = parser.parse_args()
        self.site = args.url
        if args.follow_redirects is True:
            self.follow = True

    def url_status(self, url, follow):
        status: str = ''
        try:
            if follow is False:
                status = requests.head(url).status_code
            else:
                status = requests.get(url).status_code
        except requests.exceptions.MissingSchema:
            if url[:6] != "http://":
                print("No schema provided for " + url + " trying http://" + url)
                url = "http://" + url
                status = self.url_status(url, follow)
        except Exception as e:
            status = str(e)
        return status


if __name__ == '__main__':
    main = Main()
    main.parse_arguments()
    print(f'Requested site status: {main.url_status(main.site, main.follow)}')


