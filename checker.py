from moneywagon import AddressBalance

def balance(addr):
	total = AddressBalance().action('btc', addr)
	balanceout= str(total)


def main():
	addr = input("Enter an Address :>  ")
	balance(addr)

if __name__ == '__main__':
	main()
