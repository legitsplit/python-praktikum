# Zusammenarbeit mit folgenden Teilnehmern:
def floodfill(arr, x, y, value):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    target = arr[y][x]

    if target == value:
        return

    queue = [(x, y)]

    while queue:
        current_x, current_y = queue.pop(0)

        if 0 <= current_x < cols and 0 <= current_y < rows and arr[current_y][current_x] == target:
            arr[current_y][current_x] = value

            queue.append((current_x + 1, current_y))  # Right
            queue.append((current_x - 1, current_y))  # Left
            queue.append((current_x, current_y + 1))  # Down
            queue.append((current_x, current_y - 1))  # Up

def output(arr):
    for line in arr: print(" ".join(line))

a = [["#","#","*","*","*","!"],
     ["*","#","#","*","!","!"],
     ["*","#","#","!","#","#"],
     ["*","#","#","!","#","*"],
     ["#","#","!","!","#","#"],
     ["#","#","#","!","!","#"],
     ["#","*","#","#","#","#"]]

floodfill(a, 1, 0, "-")
output(a)