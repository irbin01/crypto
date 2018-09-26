gensis_block = {'previous_hash': '',
                'index': 0,
                'transaction': []}
blockchain = [gensis_block]
open_transcation = []
owner = "Nuva"
participants = {owner} #or participants = {'Nuva'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    """ return last value of current bloackchain"""

    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """
    Append new and last value

    Arguments:
        :sender
        :recipient
        :amount
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transcation.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transaction': open_transcation}
    blockchain.append(block)


def get_transaction_value():
    tx_recipient = input("Enter recipient: ")
    tx_amount = float(input('Your transaction please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_choice = input("User choice: ")
    return user_choice


def print_bloackchain_elements():
    for block in blockchain:
        print("outputting block")
        print(block)
    else:
        print("-"*20)


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1: Add new value")
    print("2: Mine block")
    print("3: Output The blockchain blocks")
    print('4: print participants')
    print('h: to hack')
    print('q : Quit')
    user_input = get_user_choice()
    if user_input == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transcation)
    elif user_input == '2':
        mine_block()
    elif user_input == '3':
        print_bloackchain_elements()
    elif user_input == '4':
        print(participants)
    elif user_input == 'h':
        blockchain[0] = {'previous_hash': '',
                         'index': 0,
                         'transaction': [{'sender':'ab', 'recipient': 'bc', 'amount': 34}]}
    elif user_input == 'q':
        print_bloackchain_elements()
        waiting_for_input = False
    else:
        print("please enter valid choice")
    if not verify_chain():
        print_bloackchain_elements()
        print("invalid blockchain")
        break
else:
    print("User left")

print('Done!')
