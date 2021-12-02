from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

cmc = CoinMarketCapAPI('bbb56466-b301-4cdb-8fa4-13d3f84cea7b')

r = cmc.cryptocurrency_info(symbol='BTC')

print(r.data)
