from collections import defaultdict

def count_paths(grid):
    if not grid:
        return 0

    H = len(grid)
    W = len(grid[0])

    dp = [[0] * W for _ in range(H)]
    letter_last_pos = [defaultdict(int) for _ in range(W)]

    for row in range(H):
        dp[row][0] = 1
        letter_last_pos[0][grid[row][0]] += 1

    for col in range(1, W):
        for row in range(H):
            step = dp[row][col - 1]

            jump = letter_last_pos[col - 1].get(grid[row][col], 0)

            if grid[row][col] == grid[row][col - 1]:
                jump -= step

            dp[row][col] = step + jump

        for row in range(H):
            letter_last_pos[col][grid[row][col]] += dp[row][col]

    return dp[0][W - 1] + dp[H - 1][W - 1]



def read_input_file(filename):
    with open(filename, 'r') as f:
        W, H = map(int, f.readline().split())
        grid = [list(f.readline().strip()) for _ in range(H)]
    return grid


def write_output_file(filename, result):
    with open(filename, 'w') as f:
        f.write(f"{result}\n")


def main():
    grid = read_input_file("ijones.in")
    result = count_paths(grid)
    write_output_file("ijones.out", result)


if __name__ == "__main__":
    main()
