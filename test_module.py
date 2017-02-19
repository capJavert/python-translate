import requests


def test_request():
    def request(url):
        try:
            response = requests.get(url)

            return response.status_code
        except Exception:
            return -1

    result = request("http://www.design-ers.net/eh-rjecnik.asp")

    assert result == 200
