#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 03:44:08 2021

@author: hamza
"""

import pandas as pd

def data_read():
    df=pd.read_json (r'http://cf-code-challenge-40ziu6ep60m9.s3-website.eu-central-1.amazonaws.com/ohlcv-btc-usd-history-6min-2020.json')
    return df

def data_transform(df):
    df['timestamp']=pd.to_datetime(df['time_period_start'])
    df['month']=df['timestamp'].dt.strftime('%m')
    df['month'] = df['month'].apply(lambda s: s.lstrip("0"))
    df['day']=df['timestamp'].dt.strftime('%d')
    df['date']=df['timestamp'].dt.strftime('%Y-%m-%d')
    
    df.set_index('timestamp',inplace=True)

    daily_df=pd.DataFrame(columns=['date','volatility','maxPrice','minPrice','maxVolumeTraded','maxtrades'])

    for i in range(1,13):
        df_month=df[df['month']=='{q}'.format(q=i)]
        for j in df_month.day.unique():
            df_day=df_month[df_month['day']=='{q}'.format(q=j)]
            day=df_day.date.unique()
            summ=df_day.price_close.std()
            maxi=df_day.price_close.max()
            mini=df_day.price_close.min()
            maxivolume=df_day.volume_traded.max()
            maxitrades=df_day.trades_count.max()
            daily_df=daily_df.append({'date':day,'volatility':summ,'maxPrice':maxi,'minPrice':mini,'maxVolumeTraded':maxivolume,'maxtrades':maxitrades},ignore_index=True)

    daily_df['date'] = daily_df['date'].str.get(0)
    return daily_df


data=data_read()
data_transformed=data_transform(data)
print(data_transformed)
