import requests, sys

def get_images(file, name):
    urls = []
    with open(file) as f:
        urls = f.readlines()
    for i in range(len(urls)):
        r = requests.get(urls[i])
        with open("{0}/{0}{1}.jpeg".format(name, i), "w") as f:
            f.write(r.content)

if __name__ == "__main__":
    file = sys.argv[1]
    name = sys.argv[2]
    get_images(file, name)
