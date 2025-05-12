import yfinance as yf


def ticker_to_csv(ticker: str, period: str = "2y"):
    """
    Download the data for a given ticker and save it to a csv file.
    """
    data = yf.download(ticker, period=period)
    data.to_csv(f"dataset/{ticker}.csv", header=True)
    print(f"Data saved to dataset/{ticker}.csv")
