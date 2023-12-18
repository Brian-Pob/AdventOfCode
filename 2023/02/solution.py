lines = []
with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    lines = [line.strip() for line in lines]

game_sum = 0
game_num = 0
for line in lines:
    game_num += 1
    start = line.find(":") + 1
    rounds = line[start:].split(";")
    possible = True
    for r in rounds:
        if not possible:
            break

        colors = r.split(",")
        color_counts = {"red":0, "blue":0, "green":0}
        for c in colors:
            c = c.strip()
            count = int(c.split(" ")[0])
            color = c.split(" ")[1]
            color_counts[color] += count

        if not (color_counts["red"] <= 12 and color_counts["green"] <= 13 and color_counts["blue"] <= 14):
            possible = False
    if possible:
        game_sum += game_num

print(game_sum)

game_sum = 0
for line in lines:
    game_num += 1
    start = line.find(":") + 1
    rounds = line[start:].split(";")
    color_maxes = {"red":0, "blue":0, "green":0}

    for r in rounds:
        colors = r.split(",")
        color_counts = {"red":0, "blue":0, "green":0}
        for c in colors:
            c = c.strip()
            count = int(c.split(" ")[0])
            color = c.split(" ")[1]
            color_counts[color] += count

            if count > color_maxes[color]:
                color_maxes[color] = count
    
    power = 1
    for v in list(color_maxes.values()):
        power = power * v
    game_sum += power

print(game_sum)
