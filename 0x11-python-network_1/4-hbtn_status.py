#!/usr/bin/python3
"""
<<<<<<< HEAD
Fetches https://alx-intranet.hbtn.io/status using the requests package
and displays the body of the response in a specific format.
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

=======
Fetch URL using requests package:
This Python script fetches https://alx-intranet.hbtn.io/status using requests
"""
import requests


def fetch_url():
    """This method fetchs https://alx-intranet.hbtn.io/status using requests"""
   res = requests.get("https://alx-intranet.hbtn.io/status")
   return res.text


def main():
    """Main Entry - This is the main entry of the program"""
    body = fetch_url()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")


if __name__ == "__main__":
    main()
>>>>>>> 836a4ba7b816653ccf235c25d2efa81efbffc189
