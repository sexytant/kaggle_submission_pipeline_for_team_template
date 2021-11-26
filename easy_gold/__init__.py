# -*- coding: utf-8 -*-
# 
# Keep the file directory as follows:
# /
#   /input (invisible by .gitignore)
#     /{competition_name} (such as "store-sales-time-series-forecasting")
#       - train.csv
#       - test.csv
#   /store_sales
#     - dataloader.py (this file)
#

import pandas as pd
from typing import Optional, List

class DataLoader:
    def __init__(self, competition_name: str, extend_data: Optional[List[str]]):
        self.dataset_path = f"../input/{competition_name}/"
        self.common_load()
        self.extend_load(extend_data)

    def load(self, csv_file: str):
        setattr(self, csv_file, pd.read_csv(self.dataset_path + f"{csv_file}.csv") )

    def common_load(self):
        for csv_file in ["train", "test", "sample_submission"]:
            self.load(csv_file)

    def extend_load(self, extend_data: Optional[List[str]]):
        for csv_file in extend_data:
            self.load(csv_file)
