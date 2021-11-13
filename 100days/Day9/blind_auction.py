from os import system
from art import logo 
bid_data = {}
def find_highest_bidder(bid_data):
    tally = 0
    for bid_name in bid_data:
        if bid_data[bid_name] > tally:
            tally = bid_data[bid_name]

        elif bid_data[bid_name] == tally:
            print("Draw")
    print(f"The winner is {bid_name} with a bid of {tally}")

def store_users( uname, ubid):
    bid_data[uname] = ubid 
#    for x in bid_data:
    
#    bid_data += new_bidder
#from replit import clear
#HINT: You can call clear() to clear the output in the console.
system('clear')
print(logo)
other_bidders = True 

while other_bidders: 
    name = input("What is your name?\n")
    bid = int(input("What's your bid? \n"))

    store_users(uname = name, ubid = bid)
    more_bids = str(input("Are there other bidders? (YES/NO)? \n").lower())
    if more_bids == "no":
        other_bidders = False
    system('clear')
    print(logo)

#print(bid_data)
print(20 * "=")
find_highest_bidder(bid_data)



