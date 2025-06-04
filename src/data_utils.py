"""Data utils. 2025-06-04"""
import pandas as pd, numpy as np

def load_als(path):
    df = pd.read_csv(path)
    df = df.dropna(thresh=int(len(df)*0.6), axis=1)
    return df

def severity_groups(score):
    return pd.cut(score,bins=[0,16,32,48],labels=["severe","moderate","mild"])

def feature_summary(df):
    return pd.DataFrame({"missing_pct":df.isnull().mean()*100,"unique":df.nunique()})
