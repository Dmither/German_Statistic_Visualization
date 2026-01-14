import pandas as pd

def csv_concat(path1, path2):
    data1 = pd.read_csv(path1, index_col=0)
    data2 = pd.read_csv(path2, index_col=0)
    data = pd.concat([data1, data2], axis=1)
    return data

if __name__ == '__main__':
    first_path = 'germany_big_cities_density_gdp.csv'
    second_path = 'germany_big_cities_crime_tourism_rent.csv'
    res_path = './germany_big_cities.csv'

    data = csv_concat(first_path, second_path)

    data.to_csv(res_path)

