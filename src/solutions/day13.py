from src.tools.loader import load_data

TESTING = True


def parse_input(data):
    blocks = []
    blocks_inverted = []
    for block in data:
        blocks.append([])
        for line in block.split("\n"):
            blocks[-1].append(line)
    for block in blocks:
        blocks_inverted.append([])
        for j in range(len(block[0])):
            blocks_inverted[-1].append("")
            for i in range(len(block)):
                blocks_inverted[-1][j] += block[i][j]
    return blocks, blocks_inverted


def print_block(block):
    for i, line in enumerate(block):
        print(f"{i+1:02}", line)
    print()


def check_symmetry(block, i):
    num_iterations = min(i + 1, len(block) - i - 1)
    symmetric = True
    for j in range(num_iterations):
        # print(block[i - j], "and", block[i + j + 1])
        # print("equal?", block[i - j] == block[i + j + 1])
        if not block[i - j] == block[i + j + 1]:
            # print("got here")
            symmetric = False
    return symmetric

def check_smudge_symmetry(block, i):


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    blocks, blocks_inverted = parse_input(data)
    # print_block(blocks[0])
    # print_block(blocks_inverted[0])

    horizontal_sum = 0
    vertical_sum = 0
    for x in range(len(blocks)):
        #print()
        #print("NEW BLOCK", x)
        #print()
        block = blocks[x]
        #print_block(block)
        found_match = False
        for i in range(len(block) - 1):
            if block[i] == block[i + 1]:
                if check_symmetry(block, i):
                    horizontal_sum += 100 * (i + 1)
                    #print("horizontal symmetry at", i + 1)
                    #print("adding", 100 * (i + 1))
                    if found_match == True:
                        raise ValueError("already found symmetry")
                    found_match = True
        inv_block = blocks_inverted[x]
        #print_block(inv_block)
        for i in range(len(inv_block) - 1):
            if inv_block[i] == inv_block[i + 1]:
                if check_symmetry(inv_block, i):
                    vertical_sum += i + 1
                    #print("vertical symmetry at ", i + 1)
                    #print("adding", i + 1)
                    if found_match == True:
                        raise ValueError("already found symmetry")
                    found_match = True
        if not found_match:
            raise ValueError("no symmetry found")

    print(horizontal_sum)
    print(vertical_sum)
    print(horizontal_sum + vertical_sum)
