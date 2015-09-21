import json
import glob
import sys

def output_corpus(folder):

    for filename in glob.glob("{0}/*.json".format(folder)):
        with open(filename) as f:
            data = json.load(f)
        classes = data["results"][0]["result"]["tag"]["classes"]
        with open("{0}.txt".format(filename), "w") as f2:
            f2.write(' '.join(classes))
    print("Number of files: {0}".format(len(glob.glob("{0}/*.json".format(folder)))))


if __name__ == "__main__":
    folder = sys.argv[1]
    output_filename = sys.argv[2]
    output_corpus(folder)