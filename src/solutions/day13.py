from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    blocks = [[line for line in block.split("\n")] for block in data]
    blocks_inverted = []
    for block in blocks:
        blocks_inverted.append([])
        for j in range(len(block[0])):
            blocks_inverted[-1].append("")
            for i in range(len(block)):
                blocks_inverted[-1][j] += block[i][j]
    return blocks, blocks_inverted


def check_symmetry(block, i):
    symmetric = True
    for j in range(min(i + 1, len(block) - i - 1)):
        if not block[i - j] == block[i + j + 1]:
            symmetric = False
    return symmetric


def check_smudge_symmetry(block, i):
    symmetric = True
    found_smudge = False
    for j in range(min(i + 1, len(block) - i - 1)):
        if [block[i - j][x] == block[i + 1 + j][x] for x in range(len(block[i]))].count(
            False
        ) == 1 and not found_smudge:
            found_smudge = True
        elif not block[i - j] == block[i + j + 1]:
            symmetric = False
    if not found_smudge:
        return False
    return symmetric


def find_symmetry(blocks, blocks_inverted, smudge=False):
    horizontal_sum = 0
    vertical_sum = 0
    for n in range(len(blocks)):
        block = blocks[n]
        for i in range(len(block) - 1):
            if [block[i][x] == block[i + 1][x] for x in range(len(block[i]))].count(
                False
            ) <= (1 if smudge else 0):
                if (
                    check_smudge_symmetry(block, i)
                    if smudge
                    else check_symmetry(block, i)
                ):
                    horizontal_sum += 100 * (i + 1)
        inv_block = blocks_inverted[n]
        for i in range(len(inv_block) - 1):
            if [
                inv_block[i][x] == inv_block[i + 1][x] for x in range(len(inv_block[i]))
            ].count(False) <= (1 if smudge else 0):
                if (
                    check_smudge_symmetry(inv_block, i)
                    if smudge
                    else check_symmetry(inv_block, i)
                ):
                    vertical_sum += i + 1
    return horizontal_sum + vertical_sum


if __name__ == "__main__":
    data = load_data(TESTING, "\n\n")
    blocks, blocks_inverted = parse_input(data)

    # PART 1
    # test:     405
    # answer: 37975
    print(find_symmetry(blocks, blocks_inverted))

    # PART 2
    # test:     400
    # answer: 32497
    print(find_symmetry(blocks, blocks_inverted, smudge=True))
