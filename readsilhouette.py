import pickle
def readsilhouette():
    objects = []
    with (open("silhouettes.txt", "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break
    return objects
