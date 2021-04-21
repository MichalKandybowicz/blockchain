import blockchain as b
import actions as actions

# --- Load blockchain from the disk. 1
# --- Create new blockchain 2
#  |- Add element to buffer 1
#  |- Add block to blockchain 2
#  |- Get specific block 3
#  |- Get specific element from specific block 4
#  |   |- select block in chain range
#  |      |- select element in block range
#  |- Check blockchain integrity 5
#  |- Get blockchain statistics 6
#  |- Write the blockchain to the disk. 7
#  |- Q
# --- Q


def display_title_bar():
    # Clears the terminal screen, and displays a title bar.

    print("\t**********************************************")
    print("\t***        Hello, in my blockchain         ***")
    print("\t**********************************************\n")


def get_user_main_choice():
    # Let users know what they can do.
    print("[1] Load blockchain from the disk.")
    print("[2] Create new blockchain.")
    print("[q] Quit.")
    return input("What would you like to do? \n")


def get_user_blockchain_choice():
    # Let users know what they can do.
    print("[1] Add element to buffer.")
    print("[2] Add block to blockchain.")
    print("[3] Get specific block. ")
    print("[4] Get specific element from specific block.")
    print("[5] Check blockchain integrity. ")
    print("[6] Get blockchain statistics. ")
    print("[7] Write the blockchain to the disk. ")
    print("[q] Quit.")
    return input("What would you like to do? \n")


def main():
    choice = ''
    display_title_bar()
    while choice != 'q':

        choice = get_user_main_choice()

        # Respond to the user's choice.
        if choice == '1':  # [1] Load blockchain from the disk.
            blockchain = actions.load_file()
            if blockchain is not None:
                blockchain_menu(blockchain=blockchain)

        elif choice == '2':  # [2] Create new blockchain.
            blockchain = b.Blockchain()
            blockchain_menu(blockchain=blockchain)
        elif choice == 'q':
            print("\nBye.")
        else:
            print("\nI didn't understand that choice.\n")


def blockchain_menu(blockchain):

    choice = ''
    while choice != 'q':

        choice = get_user_blockchain_choice()

        # Respond to the user's choice.
        if choice == '1':  # Add element to buffer
            actions.add_to_buffer(blockchain=blockchain)
        elif choice == '2':  # Add block to blockchain
            actions.create_new_block(blockchain=blockchain)
        elif choice == '3':  # get specific block
            actions.specific_block(blockchain=blockchain)
        elif choice == '4':  # Get specific element from specific block
            actions.specific_element_from_specific_block(blockchain=blockchain)
        elif choice == '5':  # Check blockchain integrity
            actions.chain_valid(blockchain=blockchain)
        elif choice == '6':  # Get blockchain statistics.
            actions.get_blockchain_stats(blockchain=blockchain)
        elif choice == '7':  # Write the blockchain to the disk
            actions.write_to_file(blockchain=blockchain)
        elif choice == 'q':
            print("\n")
        else:
            print("\nI didn't understand that choice.\n")


if __name__ == '__main__':
    main()