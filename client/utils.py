import requests, json
import nmf_featurize
import landmark_classifier

TOTAL_TRAINING_SIZE = 2620

def run_nmf():
    nmf_featurize.run()
    return landmark_classifier.classify_kaggle()

def get_tags(image_url):

    headers = {"Authorization": "Bearer fvprKiHDx7UZgpvTNoONFVTqNBoyoO"}
    params = {'url': image_url}
    url = "https://api.clarifai.com/v1/tag/"
    r = requests.get(url, params=params, headers=headers)
    data = r.json()["results"][0]["result"]["tag"]["classes"]

    with open("client/test/0.txt", "w") as f:
        f.write(' '.join(data))
