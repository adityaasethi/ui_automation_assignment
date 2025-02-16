import json
import os

def load_test_data(filename):
    file_path = os.path.join(os.path.dirname(__file__), "../../TestData", filename)
    with open(file_path, "r") as file:
        return json.load(file)
