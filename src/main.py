import alpha_vantage_data_fetcher as fetch
import technical_analysis as ta
import data_visualization as dv

df1 = fetch.api_fetch_and_create_df('TIME_SERIES_DAILY', 'IBM')

#df2 = fetch.api_fetch_and_create_df('TIME_SERIES_DAILY', 'TSCO.LON')

#df3 = fetch.api_fetch_and_create_df('TIME_SERIES_DAILY', 'RELIANCE.BSE')

ta.add_ema_to_df(df1, 'short')
#ta.add_ema_to_df(df2, 'medium')
#ta.add_macd_to_df(df3)

fetch.print_df(df1)
#fetch.print_df(df2)
#fetch.print_df(df3)

dv.create_plot(df1,"IBM Time Series Daily plot with Exponential Moving Average analysis using short 20 day period","Close","20d_EMA")

