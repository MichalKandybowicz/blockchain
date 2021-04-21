import os
import sys
from types import ModuleType, FunctionType
from gc import get_referents
import pickle


BLACKLIST = type, ModuleType, FunctionType


def add_to_buffer(blockchain):
    """

    :param blockchain:
    :return:
    """
    data = input("What you want to add to the buffer? [q] if you want quit. \n")
    if data == 'q':
        print("back to menu.\n")
    else:
        blockchain.add_to_buffer(data)
        print("added:", data, "\n")


def create_new_block(blockchain):
    """

    :param blockchain:
    :return:
    """
    # take last block
    last_block = blockchain.get_last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # add block to chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    print(
        'New Block Forged\n',
        'index:', {block['index']}, '\n',
    )


def specific_block(blockchain):
    """

    :param blockchain:
    :return:
    """
    choice = ""
    while choice != 'q':
        block_id = input("Which block you want to select 1 - " + str(len(blockchain.chain)) + ",[q] if you want quit.\n")

        try:
            block_id = int(block_id) - 1
            if (0 <= block_id) and (block_id <= len(blockchain.chain)):
                block = blockchain.get_specific_block(block_id=block_id)
                print("BlockID:", block['index'], '\n',
                      "Proof:", block['proof'], '\n',
                      "Previous hash:", block['previous_hash'], '\n',)

                for i in range(len(block['body'])):
                    print("element id:", i, '-',  block['body'][i])

        except ValueError:
            try:
                if block_id == 'q':
                    choice = 'q'
            except ValueError:
                print("ERROR - enter a number in chain range or [q] if you want quit")


def specific_element_from_specific_block(blockchain):
    """

    :param blockchain:
    :return:
    """
    choice = ""
    while choice != 'q':
        block_id = input("Which block you want to select 1 - " + str(len(blockchain.chain)) + ",[q] if you want quit.\n")

        try:
            block_id = int(block_id) - 1
            if (0 <= block_id) and (block_id <= len(blockchain.chain)):

                choice_2 = ""
                while choice_2 != 'q':
                    element_id = input(
                        "Which element you want to select 1 - " +
                        str(len(blockchain.chain[block_id])) + ", [q] if you want quit.\n")
                    try:
                        element_id = int(block_id) - 1
                        if (0 <= element_id) and (element_id <= len(blockchain.chain[element_id])):
                            print(blockchain.get_specific_element_from_specific_block(
                                block_id=block_id, element_id=element_id
                            ))

                    except ValueError:
                        try:
                            if element_id == 'q':
                                choice_2 = 'q'
                        except ValueError:
                            print("ERROR - enter a number in range or [q] if you want quit ")

        except ValueError:
            try:
                if block_id == 'q':
                    choice = 'q'
            except ValueError:
                print("ERROR - enter a number in chain range or [q] if you want quit")


def chain_valid(blockchain):
    is_valid = blockchain.valid_chain(chain=blockchain.chain)
    if is_valid:
        print("Blockchain is valid,\n")
    else:
        print("Blockchain isn't valid")


def get_blockchain_stats(blockchain):
    """
    :param blockchain:
    :return: size in bytes, numbers of blocks
    """
    if isinstance(blockchain, BLACKLIST):
        raise TypeError('getsize() does not take argument of type: ' + str(type(blockchain)))
    seen_ids = set()
    size = 0
    numbers_of_block = len(blockchain.chain)
    objects = [blockchain]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)

    print("size:", size, "\n", "number of blocks:", numbers_of_block, "\n")


def write_to_file(blockchain):
    file_name = input("How to name the saved file?\n")

    with open('data/' + file_name + '.pickle', 'wb') as data:
        pickle.dump(blockchain, data)

    print("Blockchain saved")


def get_data_pickle_files():
    """

    :return: file from data directory but only *.pickle
    """
    files_list = os.listdir("data")
    pickle_files_list = []
    for i in range(len(files_list)):
        if files_list[i][-6:] == 'pickle':
            pickle_files_list.append(files_list[i])
    return pickle_files_list


def load_file():
    """

    :return: blockchain form file
    """

    files_list = get_data_pickle_files()
    if len(files_list) == 0:
        return print("\ndata directory is empty\n")

    print("\n")
    for i in range(len(files_list)):
        print(i, "-", files_list[i])
    print("\n")

    choice = ""
    while choice != 'q':
        try:
            file_id = input("Enter the number of the file you want to load or [q] if you want quit \n")
            try:
                file_id = int(file_id)
                if file_id in range(0, len(files_list)):
                    file_name = files_list[file_id]
                    print("Loading: ", files_list[file_id])
                    with open('data/' + file_name, 'rb') as data:
                        blockchain = pickle.load(data)
                    return blockchain

            except ValueError:
                try:
                    if file_id == 'q':
                        choice = 'q'
                except ValueError:
                    print("ERROR - enter a number in range or [q] if you want quit")

        except ValueError:
            print("ERROR - enter a number in range or [q] if you want quit")
