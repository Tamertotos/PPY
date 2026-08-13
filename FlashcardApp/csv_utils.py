import pandas as pd

REVIEW_FILE = "Words_to_learn.csv"

def read(path) -> list:
    try:
        df = pd.read_csv(path,header=None, names=["Polish","English"])
        df.drop_duplicates(inplace = True)
    except FileNotFoundError:
        raise FileNotFoundError(f"Given path does not exist {path} ")
    else:
        return df.values.tolist()


def write_to_csv(word_list):
    try:
        duplicate_words = read(REVIEW_FILE)
    except FileNotFoundError:
        duplicate_words = []

    if not word_list in duplicate_words:
        df = pd.DataFrame([word_list])
        df.to_csv(REVIEW_FILE,mode='a',index=False,header=False)

def delete_from_csv(path,word):
    words_in_review_file = read(path)
    words_in_review_file.remove(word)
    df = pd.DataFrame(words_in_review_file)
    df.to_csv(REVIEW_FILE,mode='w', index=False, header=False)
