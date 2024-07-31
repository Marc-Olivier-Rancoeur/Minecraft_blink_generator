import csv
from math import sqrt

header = "summon minecraft:falling_block ~ ~0.5 ~ {time:1,BlockState:{Name:redstone_block},Passengers:[{id:armor_stand,Health:0,Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:["
footer = "{id:command_block_minecart,Command:\"setblock ~ ~1 ~ command_block{auto:1,Command:'fill ~ ~ ~ ~ ~-3 ~ air'}\"},{id:command_block_minecart,Command:\"kill @e[type=command_block_minecart,distance=..1]\"}]}]}]}"
with open("tourEiffel.csv") as csvfile:
    csvData = list(csv.reader(csvfile, delimiter=';'))
    side = round(sqrt(len(csvData)))

    output1 = header
    output2 = header
    output3 = header
    output4 = header

    i = 0
    j = 0
    k = 0
    l = 0

    for row in csvData:
        output1 += "{id:command_block_minecart,Command:\"setblock ~" + str(i + 1) + " ~ ~" + str(j + 1) + " minecraft:repeating_command_block{auto:1,Command:'execute if entity @e[type=pig,distance=0..0.8,name=Epig] run setblock ~" + str(-int(side/2) + ((j%2)*side)) + " ~ ~" + str(side + l + 1 - j) + " minecraft:redstone_block'}\"},"
        output2 += "{id:command_block_minecart,Command:\"setblock ~" + str(-int(side/2) + k + 1) + " ~1 ~" + str(side + l + 2) + " minecraft:repeating_command_block{Command:'setblock ~ ~-1 ~ minecraft:air'}\"},"
        output3 += "{id:command_block_minecart,Command:\"setblock ~" + str(-int(side/2) + k + 1) + " ~1 ~" + str(side + l + 4) + " minecraft:command_block{Command:'setblock " + row[0] + " " + str((int(row[1])-1)) + " " + row[2] + " minecraft:redstone_lamp[lit=true]'}\"},"
        output4 += "{id:command_block_minecart,Command:\"setblock ~" + str(-int(side/2) + k + 1) + " ~1 ~" + str(side + l + 6) + " minecraft:command_block{Command:'setblock " + row[0] + " " + str((int(row[1])-1)) + " " + row[2] + " minecraft:redstone_lamp'}\"},"
        i += 1
        if i == side:
            i = 0
            j += 1
        k += 1
        if k == 2*side:
            k = 0
            l += 6
    output1 += footer
    output2 += footer
    output3 += footer
    output4 += footer

    print(output1)
    print(output2)
    print(output3)
    print(output4)
