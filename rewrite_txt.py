# 定義替換規則
move_mapping = {
    "Move.UP": "1",
    "Move.DOWN": "2",
    "Move.LEFT": "3",
    "Move.RIGHT": "4"
}

# 用於儲存 startRowIdx 和 startColIdx 的值
coordinates = []

# 用於儲存修改後的所有行
modified_lines = []

# 讀取原始 txt 檔案
with open("outputs/output.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        if "startRowIdx" in line:
            coordinates.append(line.split('=')[1].strip())
        elif "startColIdx" in line:
            coordinates.append(line.split('=')[1].strip())
        else:
            for key, value in move_mapping.items():
                line = line.replace(key, value)
            modified_lines.append(line)

# 寫入新的 txt 檔案
with open("output.txt", "w") as file:
    # 寫入 startRowIdx 和 startColIdx 的值
    file.write(','.join(coordinates) + '\n')
    # 寫入替換後的移動指令
    for line in modified_lines:
        file.write(line)

print("File transformation complete!")
