import sys
from blockchain_parser.blockchain import Blockchain
from blockchain_parser.script import CScriptInvalidError


def is_ascii_text(op):
    return all(32 <= x <= 127 for x in op)


blockchain = Blockchain(sys.argv[1])
for block in blockchain.get_unordered_blocks():
    for transaction in block.transactions:
        coinbase = transaction.inputs[0]
        #btc_test = "MUY0OGppSldkUk53VGF2TVBVaTRFOFd1OXVISmtrdWFYSAo="

        # Some coinbase scripts are not valid scripts
        try:
            script_operations = coinbase.script.operations
        except CScriptInvalidError:
            break

        # An operation is a CScriptOP or pushed bytes
        for operation in script_operations:
            if type(operation) == bytes and len(operation) > 3 \
                    and is_ascii_text(operation):
                print(block.header.timestamp, operation.decode("ascii"))
        break
