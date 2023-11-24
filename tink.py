import os

from tinkoff.invest import (
    CandleInstrument,
    Client,
    InfoInstrument,
    SubscriptionInterval,
)
from tinkoff.invest.services import MarketDataStreamManager


TOKEN = 't.ZsrYdAC-An0uyHnudfvRJ2MVp39P77b7I7MNsCa3p5zPFpi0xbvLraeMSjQEAdwXN4xaSlCE-w_M6kWlsMpKkA'
# figi='BBG0013HGFT4'
# figi='BBG0013HRTL0', ticker='CNYRUB_TOM'
# def main():
#     with Client(TOKEN) as client:
#         inst = client.instruments.currencies()
#         print(inst)
import os
import os
from tinkoff.invest import CandleInstrument, Client, SubscriptionInterval
from tinkoff.invest.services import MarketDataStreamManager



def main():
    with Client(TOKEN) as client:
        market_data_stream: MarketDataStreamManager = client.create_market_data_stream()
        market_data_stream.candles.waiting_close().subscribe(
            [
                CandleInstrument(
                    figi="BBG0013HGFT4",
                    interval=SubscriptionInterval.SUBSCRIPTION_INTERVAL_ONE_MINUTE,
                )
            ]
        )

        for marketdata in market_data_stream:
            if marketdata.candle:
                last_price = marketdata.candle.close
                print(f"Последняя цена валютной пары: {last_price}")
                break  # Прерываем цикл после получения последней цены

if __name__ == "__main__":
    main()
