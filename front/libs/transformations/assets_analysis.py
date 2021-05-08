def get_assets_ids(data, min_date=None, max_date=None, only_active=False):
    min_date = min(data.operations["Date"]) if min_date is None else min_date
    max_date = max(data.operations["Date"]) if max_date is None else max_date
    df = data.operations.loc[(data.operations["Date"] >= min_date) & (data.operations["Date"] <= max_date)]
    df_assets_groupby = df.groupby("AssetId").sum(0)[["Price"]]

    assets_ids = (
        list(df_assets_groupby.loc[df_assets_groupby["Price"] > 0].index)
        if only_active
        else list(df_assets_groupby.index)
    )

    return assets_ids


def get_asset_timeserie(asset_id, data):
    asset_profitability_index = data.assets["ProfitabilityIndex"]
    timeseries = data.investment_status.loc[data.investment_status["AssetId"] == asset_id].sort_values("Date")
    print(timeseries)
    return None
