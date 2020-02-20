#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # Assign max_profit to the absolute lowest profit possible
    max_profit = min(prices) - max(prices)

    # Go through each buy price
    for i in range(len(prices)):

        # Go through each sell price after a buy price
        for j in range(i + 1, len(prices)):
            lowest_price = prices[i]
            highest_price = prices[j]

            profit = highest_price - lowest_price
            print(f'{highest_price} - {lowest_price}')
            if profit > max_profit:
                max_profit = profit
            print(f'profit:{profit}')

    print(f'max_profit:{max_profit}')
    return max_profit


find_max_profit([1000, 90, 80, 50, 1, 10])

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
