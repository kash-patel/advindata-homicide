import pandas as pd


def transform_data (data):
    
    data.drop(columns=["uid", "victim_last", "victim_first", "state", "city"], inplace=True)
    
    data.loc[:, "reported_date"] = pd.to_datetime(data["reported_date"].map(lambda d: f"{str(d)[:4]}-{str(d)[4:6]}-{str(d)[-2:]}"))
    max_date = data["reported_date"].max()
    data["month"] = data["reported_date"].dt.month_name().astype("category")
    data["weekday"] = data["reported_date"].dt.day_name().astype("category")
    data["delta_days"] = (max_date - data["reported_date"]).dt.total_seconds() / (60 * 60 * 24)
    
    data["victim_race"] = data["victim_race"].astype("category")
    data["victim_age"] = data["victim_age"].map(lambda s: "-1" if not str(s).isnumeric() else str(s)).astype(int)
    data["victim_sex"] = data["victim_sex"].astype("category")
    data["disposition"] = data["disposition"].astype("category")