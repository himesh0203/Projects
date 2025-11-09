pip install yfinance pandas plotly



import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def visualize_stock_data(ticker_symbol, start_date, end_date):
    """
    Fetches stock data and creates an interactive candlestick chart.

    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL', 'MSFT').
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
    """
    print(f"Fetching data for {ticker_symbol} from {start_date} to {end_date}...")
    # Fetch data from Yahoo Finance
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    
    if stock_data.empty:
        print("No data found for the specified ticker and date range.")
        return

    print("Data fetched successfully. Creating visualization...")

    # Create a candlestick trace
    candlestick = go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name="Candlestick"
    )

    # Create a separate subplot for volume as a bar chart
    volume_bars = go.Bar(
        x=stock_data.index,
        y=stock_data['Volume'],
        name="Volume",
        marker_color='blue', # Customize color
        opacity=0.5
    )

    # Create a figure with subplots for price and volume
    fig = go.Figure(data=[candlestick, volume_bars])

    # Customize the layout
    fig.update_layout(
        title=f"{ticker_symbol} Stock Price and Volume Analysis",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        xaxis_rangeslider_visible=False, # Hide the default range slider for cleaner look
        legend=dict(x=0, y=0.9, traceorder="normal"),
        height=600,
        template="plotly_white"
    )

    # Add a range slider for interactive date filtering
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="date"
        )
    )

    # Show the interactive figure
    fig.show()

if __name__ == "__main__":
    # Example usage
    TICKER = 'TSLA'  # Replace with the stock ticker you want to visualize
    START = '2023-01-01'
    END = '2024-11-08'
    visualize_stock_data(TICKER, START, END)






How to Run the Code
Save: Save the code above as a Python file (e.g., stock_visualizer.py).
Execute: Run the file from your terminal: python stock_visualizer.py
View: The interactive chart will open in your web browser. You can hover over data points for details, and use the range slider at the bottom to zoom in on specific periods.
