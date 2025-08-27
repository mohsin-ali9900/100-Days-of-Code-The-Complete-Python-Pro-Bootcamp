import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to secret Auction Program")
more = "yes"
bids = {}
while more == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    more = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear_screen()

highest_bid = 0
winnerBidder = ""
for i in bids:
    if bids[i] > highest_bid:
        highest_bid = bids[i]
        winnerBidder = i
print(f"Winner is {winnerBidder} and the winning bid amount is {highest_bid}")
