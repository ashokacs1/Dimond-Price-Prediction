import os
import sys
from src.logger import logging
from src.Exception import CustomeException
import pandas as pd 

from src.Components.data_ingestion import DataIngestion

if __name__=='__main__':
    obj = DataIngestion()
    train_data_path,test_data_path = obj.intiate_data_ingestion()
    print(train_data_path,test_data_path)