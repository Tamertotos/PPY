import pandas as pd

class Reader:
    def __init__(self,path):
        try:
            df = pd.read_csv(path)
        except FileNotFoundError:
            print("Given path does not exist")
        else:
            self.words = self.get_languages(df)


    def get_languages(self,data_frame):
        words = {row.Polish: row.English for (index, row) in data_frame.iterrows()}
        return words
