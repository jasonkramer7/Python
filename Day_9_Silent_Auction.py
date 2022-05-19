import os
clear = lambda: os.system('cls')
clear()
from gavel import logo
print(logo)

auction_bids = {}
bidding_finished = False

def find_highest_bidder(bid):
    clear()
    winner = ""
    highest_bid = 0
    for key in auction_bids:
        if auction_bids[key] > highest_bid:
            winner = key
            highest_bid = auction_bids[key]
    
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_bids[name] = bid

    end = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if end == 'no':
        bidding_finished = True
        find_highest_bidder(auction_bids)
    elif end == 'yes':
        clear()
