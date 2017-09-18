import pandas as pd
import numpy as np

class Loader:


    def __init__(self, file):
        self.data_frame = pd.read_csv(file);
