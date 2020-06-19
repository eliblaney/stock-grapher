from alpha_vantage.timeseries import TimeSeries
import configManager
import pandas
import matplotlib.pyplot as plt
from pprint import pprint

def main():
    config = configManager.load()

    # Obtain stock data from Alpha Vantage
    ts = TimeSeries(key=config["API_KEY"], output_format='pandas')
    data, meta_data = ts.get_intraday(
            symbol=config["symbol"],
            interval=config["interval"],
            outputsize='full')

    # Read and display summary of stock prices
    result = data.head(config["numPoints"])
    pprint(result)
    
    # Plot only open, high, low, and close prices
    # Volume is too big to be on the same graph
    data = data.iloc[:,0:4] 
    plot(data, "{} Stock Prices".format(config["symbol"]))

def plot(data, title="Stock Prices"):
    data.plot()
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    main()
