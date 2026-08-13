import pandas as pd


def read(path):
    try:
        df = pd.read_csv(path,header=None, names=["Polish","English"])
        df.drop_duplicates(inplace = True)
    except FileNotFoundError:
        raise FileNotFoundError(f"Given path does not exist {path} ")
    else:
        return df.values.tolist()


def write_to_csv(word_list):
    try:
        duplicate_words = read("Words_to_learn.csv")
    except FileNotFoundError:
        duplicate_words = []

    if not word_list in duplicate_words:
        df = pd.DataFrame([word_list])
        df.to_csv("Words_to_learn.csv",mode='a',index=False,header=False)
    else:
        return