import requests
import json
#Local-link address url for getting the metadata details of aws ec2 instance
metadata_url = 'http://169.254.169.254/latest/'

#Gets the values for each category of instance metadata
def extract(url, arr):
    output = {}
    for item in arr:
        recent = url + item
        r = requests.get(recent)
        text = r.text
        if item[-1] == "/":
            values_list = r.text.splitlines()
            output[item[:-1]] = extract(recent, values_list)
        elif check_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output

def meta():
    first = ["meta-data/"]
    result = extract(metadata_url, first)
    return result

def meta_json():
    metadata = meta()
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json

def check_json(json_file):
    try:
        json.loads(json_file)
    except ValueError:
        return False
    return True

#Prints the AWS metadata in the form of json format
if __name__ == '__main__':
    print(meta_json())
