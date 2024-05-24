google_Search_data = "youtube"


url_google = "www.google.com"
url_store = "https://twitter.com/i/flow/login"


def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = "w" if new else "a"
    with open(filename, mode, newline="") as f:
        f.writelines(data)
