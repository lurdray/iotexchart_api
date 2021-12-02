import requests

response = requests.get("https://data.gateapi.io/api2/1/tradeHistory/IOTX_USDT").json()


def main():
	return(response)

#print(main())