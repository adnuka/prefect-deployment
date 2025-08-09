from prefect import flow
from main import main

@flow(log_prints=True, persist_result=True)
def market_prices_flow():
    main()

if __name__ == "__main__":
    market_prices_flow.serve(name="market-prices-deployment", tags=["market-prices"], interval=1800) # 30 minutes in seconds