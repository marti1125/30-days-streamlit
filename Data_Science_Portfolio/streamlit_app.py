import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime


df_agg = pd.read_csv("data/Aggregated_Metrics_By_Video.csv").iloc[1:, :]
df_agg.columns = [
    "Video",
    "Video title",
    "Video publish time",
    "Comments added",
    "Shares",
    "Dislikes",
    "Likes",
    "Subscribers lost",
    "Subscribers gained",
    "RPM(USD)",
    "CPM(USD)",
    "Average % viewed",
    "Average view duration",
    "Views",
    "Watch time (hours)",
    "Subscribers",
    "Your estimated revenue (USD)",
    "Impressions",
    "Impressions ctr(%)",
]
df_agg["Video publish time"] = pd.to_datetime(df_agg["Video publish time"], format="%b %d, %Y")
df_agg["Average view duration"] = df_agg["Average view duration"].apply(lambda x: datetime.strptime(x, "%H:%M:%S"))
df_agg["Avg_duration_sec"] = df_agg["Average view duration"].apply(lambda x: x.second + x.minute * 60 + x.hour * 3600)
df_agg["Engagement_ratio"] = (
    df_agg["Comments added"] + df_agg["Shares"] + df_agg["Dislikes"] + df_agg["Likes"]
) / df_agg.Views
df_agg["Views / sub gained"] = df_agg["Views"] / df_agg["Subscribers gained"]
df_agg.sort_values("Video publish time", ascending=False, inplace=True)

df_agg_sub = pd.read_csv("data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv")

df_comments = pd.read_csv("data/All_Comments_Final.csv")

df_time = pd.read_csv("data/Video_Performance_Over_Time.csv")
df_time["Date"] = df_time["Date"].str.replace("Sept", "Sep")
df_time["Date"] = pd.to_datetime(df_time["Date"], format="%d %b %Y")
