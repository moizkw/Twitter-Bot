import pandas as pd
import numpy as np
from requests_html import HTMLSession
from datetime import datetime
from datetime import timedelta
from yahoo_earnings_calendar import YahooEarningsCalendar

def force_float(elt):
    try:
        return float(elt)
    except:
        return elt
def _raw_get_daily_info(site):
    session = HTMLSession()
    resp = session.get(site)
    tables = pd.read_html(resp.html.raw_html)
    df = tables[0].copy()
    df.columns = tables[0].columns
    del df["Name"]
    del df["52 Week Range"]
    del df["Change"]
    del df["Volume"]
    del df["Avg Vol (3 month)"]
    del df["Market Cap"]
    del df["PE Ratio (TTM)"]
    df.rename(columns = {'Price (Intraday)':'Price'}, inplace = True)
    df.index = np.arange(1, len(df) + 1)
    df["% Change"] = df["% Change"].map(lambda x: float(x.strip("%+").replace(",", ""))) 
    session.close()
    return df.to_string()

def gainers():
    return(_raw_get_daily_info("https://finance.yahoo.com/gainers?offset=0&count=5"))

def losers():    
    return(_raw_get_daily_info("https://finance.yahoo.com/losers?offset=0&count=5"))

def most_active():
    return(_raw_get_daily_info("https://finance.yahoo.com/most-active?offset=0&count=5")) 
    
def earnings_date(): #this part of the code doesn't work on off-market days/weekends
    DAYS_AHEAD = 0

    # setting the dates
    start_date = datetime.now().date()
    end_date = (datetime.now().date() + timedelta(days=DAYS_AHEAD))

    # downloading the earnings calendar
    yec = YahooEarningsCalendar()
    earnings_list = yec.earnings_between(start_date, end_date)

    # saving the data in a pandas DataFrame
    earnings_df = pd.DataFrame(earnings_list)
    earnings_df.head()
    del earnings_df["companyshortname"]
    del earnings_df["startdatetime"]
    del earnings_df["startdatetimetype"]
    del earnings_df["epsestimate"]
    del earnings_df["epsactual"]
    del earnings_df["epssurprisepct"]
    del earnings_df["timeZoneShortName"]
    del earnings_df["gmtOffsetMilliSeconds"]
    del earnings_df["quoteType"]
    earnings_df.index = np.arange(1, len(earnings_df) + 1)
    print(earnings_df.to_string())
    return(earnings_df.to_string())

def world_indices():
    session = HTMLSession()
    resp = session.get('https://finance.yahoo.com/world-indices')
    tables = pd.read_html(resp.html.raw_html)
    df = tables[0].copy()
    df.columns = tables[0].columns
    df["% Change"] = df["% Change"].map(lambda x: float(x.strip("%+").replace(",", ""))) 
    print("                  Market Summary of World Indices                   ")
    print("--------------------------------------------------------------------")
    print(df.loc[0:7, ['Symbol', 'Name', 'Last Price', '% Change']]) 
    df.index = np.arange(1, len(df) + 1)
    print()
    session.close()
    return df.to_string()
       

if __name__ == "__main__":
    print(), gainers(), losers(), most_active(), world_indices(), earnings_date() 