import pandas as pd


def read(path):
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Given path does not exist {path} ")
    else:
        words = get_languages(df)
        return words

def get_languages(data_frame):
    words = data_frame.values.tolist()
    return words

    def write_to_csv(self):
        pass