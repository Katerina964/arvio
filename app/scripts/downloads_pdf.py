import requests
import tempfile
import os
from pdfminer.high_level import extract_text


def pdf(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with tempfile.TemporaryDirectory() as d:
            file_name = os.path.join(d, "metadata.pdf")
            with open(file_name, "wb+") as f:
                for chunk in response:
                    f.write(chunk)
            text = extract_text(file_name)
    return text


# pdf("https://whats-that.s3.eu-central-1.amazonaws.com/energy-data/2017-46-77-53527.pdf")
