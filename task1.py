import requests
import json


def fetch_data() -> None:
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    with open("data/data.json", "w") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
        file.close()


def main() -> None:
    fetch_data()


if "__main__" == __name__:
    main()
