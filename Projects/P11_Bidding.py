bid = {}

while True:
    name = input("Enter your name: ")
    price = int(input("Enter your bid price: "))
    bid[name] = price
    more_bids = input("Are there any more bidders? Type 'yes' or 'no'.\n")
    if more_bids == "yes":
        name = input("Enter your name: ")
        price = int(input("Enter your bid price: "))
        bid[name] = price

    elif more_bids == "no":
        break

for key in bid:
    if bid[key] == max(bid.values()):
        print(f"The winner is {key} with a bid of {bid[key]}")