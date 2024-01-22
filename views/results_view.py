import pandas as pd
import os


class Result:
    def __init__(self, pg, statistics):
        self.pg = pg
        self.statistics = statistics

    def download_csv(self):
        output_csv_folder = "statistics"
        os.makedirs(output_csv_folder, exist_ok=True)
        df = pd.DataFrame(self.pg)
        df.to_csv(f'{output_csv_folder}/population_generation.csv')
        df2 = pd.DataFrame(self.statistics)
        df2.to_csv(f'{output_csv_folder}/population_statistics.csv')
