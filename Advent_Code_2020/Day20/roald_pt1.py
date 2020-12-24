from dataclasses import dataclass

@dataclass
class Tile: #define class Tile(str) to inherit f.i. from string class
    number : int
    pattern : list

    @property
    def top(self):
        return self.pattern[0]

    @property
    def bottom(self):
        return self.pattern[-1]

    @property
    def left(self):
        return "".join(row[0] for row in self.pattern)

    @property
    def right(self):
        return "".join(row[-1] for row in self.pattern)

    def rotate_90deg(self):
        rotated_pattern = []
        for row in range(len(self.pattern)):
            rotated_pattern.append("".join(
                self.pattern[col][row]
                for col in reversed(range(len(self.pattern[0])))
            ))

        self.pattern = rotated_pattern

    def mirror(self):
        self.pattern = [row[::-1] for row in self.pattern]

with open("../Input_files/20.txt") as file:
    pieces = file.read().split("\n\n")

tiles = []
for piece in pieces:
    piece = piece.split("\n")
    tiles.append(Tile(int(piece[0][5:9]), piece[1:]))

def all_possible_edges(tile):
    edges = []
    edges.append(tile.left)
    edges.append(tile.right)
    edges.append(tile.top)
    edges.append(tile.bottom)
    tile.mirror()
    edges.append(tile.top)
    edges.append(tile.bottom)
    tile.rotate_90deg()
    edges.append(tile.top)
    edges.append(tile.bottom)

    return edges

all_edges = []
for tile in tiles:
    all_edges += all_possible_edges(tile)

ans = 1
for i, tile in enumerate(tiles):
    tile_edges = all_possible_edges(tile)
    matches = len([edge for edge in tile_edges if edge in all_edges[0:i*8] + all_edges[(i+1)*8:]])
    if matches == 4:
        ans *= tile.number

print(ans)