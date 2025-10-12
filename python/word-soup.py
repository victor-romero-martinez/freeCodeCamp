from typing import Union

sopa = [
    ['C', 'A', 'T', 'G', 'F'],
    ['P', 'E', 'R', 'R', 'O'],
    ['L', 'A', 'P', 'I', 'Z'],
    ['C', 'O', 'D', 'E', 'R']
]

palabra_a_buscar = ['PERRO', 'GATO', 'LAP', 'EPE', 'PIZ']


# horizontal
def match_h(word: str, matriz: list[list[str]]):
    res: list[Union[str, bool, int, int]] = [word, False, 0, 0]

    for row_idx in range(len(matriz)):
        maybe_match = ''
        word_idx = 0

        for col_idx in range(len(matriz[row_idx])):
            if word[word_idx] == matriz[row_idx][col_idx]:
                maybe_match += matriz[row_idx][col_idx]
                word_idx += 1

            if maybe_match == word:
                new_col_idx = col_idx - (len(word) - 1)
                res[1] = True
                res[2] = row_idx
                res[3] = new_col_idx if new_col_idx > 0 else 0

                break

        maybe_match = ''
        word_idx = 0

    return res


# vertical
def match_v(word: str, matriz: list[list[str]]):
    res: list[Union[str, bool, int, int]] = [word, False, 0, 0]

    for row_idx in range(len(matriz)):
        current_row = 0
        maybe_match = ''
        word_idx = 0

        while current_row < len(matriz):

            if word[word_idx] == matriz[current_row][row_idx]:
                maybe_match += matriz[current_row][row_idx]
                word_idx += 1

            if maybe_match == word:
                new_row_idx = current_row - (len(word) - 1)
                res[1] = True
                res[2] = new_row_idx if new_row_idx > 0 else 0
                res[3] = row_idx

                break

            current_row += 1

        maybe_match = ''
        word_idx = 0
        current_row = 0

    return res


# diagonal ad
def match_d(word: str, matriz: list[list[str]]):
    res: list[Union[str, bool, int, int]] = [word, False, 0, 0]
    num_row = len(matriz)
    num_col = len(matriz[0])

    for row in range(num_row):
        for col in range(num_col):
            maybe_match = ''

            for k in range(len(word)):
                if row + k >= num_row or col + k >= num_col:
                    break
                if matriz[row + k][col + k] != word[k]:
                    break

                maybe_match += matriz[row + k][col + k]

            if maybe_match == word:
                res[1] = True
                res[2] = row
                res[3] = col
                return res

    return res


# [['PERRO', TRUE, 1, 0], ...]


def soup_solver():
    res_aux: dict[str, list[Union[str, bool, int, int]]] = {}
    result: list[list[Union[str, bool, int, int]]] = []

    for p in palabra_a_buscar:
        h = match_h(p, sopa)
        v = match_v(p, sopa)
        d = match_d(p, sopa)

        if h[1]:
            res_aux[p] = h
        elif v[1]:
            res_aux[p] = v
        elif d[1]:
            res_aux[p] = d
        else:
            res_aux[p] = h

    for r in res_aux.values():
        result.append(r)

    print(result)


if __name__ == '__main__':
    soup_solver()
