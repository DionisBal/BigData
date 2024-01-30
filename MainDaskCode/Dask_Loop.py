import pandas as pd


def process_file(filename, save_path):
    data = pd.read_csv(f'E:\InformationSystemsData\data\{filename}')
    print(filename)
    data.to_csv(f'{save_path}/{filename}')
    return 0
