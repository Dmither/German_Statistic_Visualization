import pandas as pd

def csv_concat(path1, path2):
    data1 = pd.read_csv(path1, index_col=0)
    data2 = pd.read_csv(path2, index_col=0)
    data = pd.concat([data1, data2], axis=1)
    return data

if __name__ == '__main__':
    path1 = './germany_states_environment.csv'
    path2 = './germany_states_forest_cover.csv'
    res_path = './germany_states_environment.csv'

    data = csv_concat(path1, path2)

    data.to_csv(res_path)

