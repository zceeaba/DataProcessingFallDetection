import pickle
def pickledata(data,filename):
    import pickle
    with open(filename+".txt", "wb") as myFile:
        pickle.dump(data, myFile)
