import ollama
import os
import json
import numpy as np
from numpy.linalg import norm


def parse_file(filename):
    # open a file and return paragraphs
    with open(filename, encoding="utf-8-sig") as f:
        paragraphs = []
        buffer = []
        for line in f.readlines():
            line = line.strip()
            if line:
                buffer.append(line)
            elif len(buffer):
                paragraphs.append((" ").join(buffer))
                buffer = []
        if len(buffer):
            paragraphs.append((" ").join(buffer))
        return paragraphs


def save_embeddings(filename, embeddings):
    # create dir if it doesn't exist
    if not os.path.exists("embeddings"):
        os.makedirs("embeddings")
    # dump embeddings to json
    with open(f"embeddings/{filename}.json", "w") as f:
        json.dump(embeddings, f)


def load_embeddings(filename):
    # check if file exists
    if not os.path.exists(f"embeddings/{filename}.json"):
        return False
    # load embeddings from json
    with open(f"embeddings/{filename}.json", "r") as f:
        return json.load(f)


def get_embeddings(filename, modelname, chunks):
    # def get_embeddings(modelname,chunks):
    # check if embeddings are already saved
    # TODO: use model specific for embedding - bge, phi, etc
    if (embeddings := load_embeddings(filename)) is not False:
        return embeddings
    # get embeddings from ollama
    embeddings = [
        ollama.embeddings(model=modelname, prompt=chunk)["embedding"]
        for chunk in chunks
    ]
    # save embeddings
    save_embeddings(filename, embeddings)
    return embeddings


# find cosine similarity of every chunk to a given embedding
def find_most_similar(needle, haystack):
    # The norm of a vector is a measure of its length (magnitude),
    # calculated as the square root of the sum of the squares of its components
    needle_norm = norm(needle)

    # dot product/ product of their norms - measure of the cosine similarity between the two vectors,
    similarity_scores = [
        np.dot(needle, item) / (needle_norm * norm(item)) for item in haystack
    ]
    return sorted(zip(similarity_scores, range(len(haystack))), reverse=True)


## chat
def chat(modelname="phi", messages=[]):
    result = ollama.chat(
        model="phi",
        messages=[{"role": "user", "content": "Why is the sky blue"}],
    )

    return result


if __name__ == "__main__":
    import time

    # result = chat()
    # print(result)
    story_file = "peter-pan.txt"
    paragraphs = parse_file(story_file)
    # print(len(paragraphs))
    start = time.perf_counter()
    embeddings = get_embeddings(story_file, "phi", paragraphs)
    print(len(embeddings))

    print(time.perf_counter() - start)  # time taken
