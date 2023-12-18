from src.tools.loader import load_data
from tqdm import tqdm

TESTING = False


def get_new_direction(symbol, direction):
    if symbol == ".":
        new_direction = direction
    elif symbol == "/":
        if direction == (0, 1):
            new_direction = (-1, 0)
        elif direction == (0, -1):
            new_direction = (1, 0)
        elif direction == (1, 0):
            new_direction = (0, -1)
        elif direction == (-1, 0):
            new_direction = (0, 1)
    elif symbol == "\\":
        if direction == (0, 1):
            new_direction = (1, 0)
        elif direction == (0, -1):
            new_direction = (-1, 0)
        elif direction == (1, 0):
            new_direction = (0, 1)
        elif direction == (-1, 0):
            new_direction = (0, -1)
    elif symbol == "|":
        if direction == (0, 1):
            new_direction = [(1, 0), (-1, 0)]
        elif direction == (0, -1):
            new_direction = [(-1, 0), (1, 0)]
        elif direction == (1, 0):
            new_direction = (1, 0)
        elif direction == (-1, 0):
            new_direction = (-1, 0)
    elif symbol == "-":
        if direction == (0, 1):
            new_direction = (0, 1)
        elif direction == (0, -1):
            new_direction = (0, -1)
        elif direction == (1, 0):
            new_direction = [(0, 1), (0, -1)]
        elif direction == (-1, 0):
            new_direction = [(0, 1), (0, -1)]
    return new_direction


if __name__ == "__main__":
    grid = load_data(TESTING, "\n")
    beam_positions = [(0, -1)]
    beam_directions = [(0, 1)]
    poss_max_values = []
    poss_starts = []

    for i in range(len(grid)):
        poss_starts.append(([(i, -1)], [(0, 1)]))
        poss_starts.append(([(i, len(grid[0]))], [(0, -1)]))
    for j in range(len(grid[0])):
        poss_starts.append(([(-1, j)], [(1, 0)]))
        poss_starts.append(([(len(grid), j)], [(-1, 0)]))

    counter_new = 0
    for beam_positions, beam_directions in tqdm(poss_starts):
        counter_new += 1
        passed_positions = []
        set_lengths = []
        while beam_positions:
            nbp = []
            nbd = []
            visited = set()
            for i in range(len(beam_positions)):
                if (beam_positions[i], beam_directions[i]) not in visited:
                    nbp.append(beam_positions[i])
                    nbd.append(beam_directions[i])
                visited.add((beam_positions[i], beam_directions[i]))
            beam_positions = nbp
            beam_directions = nbd
            beam_positions_new = []
            beam_directions_new = []
            for i, (x, y) in enumerate(beam_positions):
                beam_positions_new.append((x, y))
                beam_directions_new.append(beam_directions[i])
                new_position = (x + beam_directions[i][0], y + beam_directions[i][1])
                x, y = new_position
                if (
                    (-1 in new_position)
                    or (new_position[0] == len(grid))
                    or (new_position[1] == len(grid[0]))
                ):
                    del beam_positions_new[-1]
                    del beam_directions_new[-1]
                    continue
                symbol = grid[new_position[0]][new_position[1]]
                new_direction = get_new_direction(symbol, beam_directions[i])
                if symbol != ".":
                    if type(new_direction) is list:
                        del beam_positions_new[-1]
                        beam_positions_new.append(new_position)
                        passed_positions.append(new_position)
                        beam_positions_new.append(new_position)
                        passed_positions.append(new_position)
                        del beam_directions_new[-1]
                        beam_directions_new.append(new_direction[0])
                        beam_directions_new.append(new_direction[1])
                    else:
                        del beam_positions_new[-1]
                        beam_positions_new.append(new_position)
                        passed_positions.append(new_position)
                        del beam_directions_new[-1]
                        beam_directions_new.append(new_direction)
                elif symbol == ".":
                    del beam_positions_new[-1]
                    beam_positions_new.append(new_position)
                    passed_positions.append(new_position)
                    del beam_directions_new[-1]
                    beam_directions_new.append(new_direction)
                else:
                    raise ValueError("what is symbol?", symbol)
            beam_positions = beam_positions_new
            beam_directions = beam_directions_new
            set_lengths.append(len(set(passed_positions)))
            if len(set_lengths) > 10 and set_lengths[-8:].count(set_lengths[-1]) == 8:
                poss_max_values.append(set_lengths[-1])
                break
        poss_max_values.append(set_lengths[-1])

    print(max(poss_max_values))
    print(len(set(passed_positions)))
    print(poss_max_values)
