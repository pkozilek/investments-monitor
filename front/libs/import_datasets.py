import pandas as pd


class Datasets:
    def __init__(self):
        xls = pd.ExcelFile('datasets/Investment Monitor.xlsx', engine='openpyxl')
        self.index_values = pd.read_excel(xls, "IndexValues", index_col=0)
        self.operations = pd.read_excel(xls, "Operations", index_col=0)
        self.operation_types = pd.read_excel(xls, "OperationTypes", index_col=0)
        self.dividends = pd.read_excel(xls, "Dividends", index_col=0)
        self.assets = pd.read_excel(xls, "Assets", index_col=0)
        self.indexes = pd.read_excel(xls, "Indexes", index_col=0)
        self.asset_types = pd.read_excel(xls, "AssetTypes", index_col=0)
        self.investment_status = pd.read_excel(xls, "InvestmentStatus", index_col=0)
