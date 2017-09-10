import requests


def test_request():
    def request(url):
        try:
            response = requests.get(url)

            return response.status_code
        except Exception:
            return -1

    result = request("https://translate.google.com")

    assert result == 200
