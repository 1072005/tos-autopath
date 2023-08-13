import pygetwindow as gw
import pyautogui

# 初始化陣列
non_pos = [0, 0]
Move = []

with open('output.txt', 'r') as file:
    lines = file.readlines()

    # 處理第一行
    first_line_values = lines[0].strip().split(',')
    non_pos[0] = int(first_line_values[0])
    non_pos[1] = int(first_line_values[1])

    # 處理第二行
    second_line_values = lines[1].strip().split()
    for value in second_line_values:
        Move.append(int(value))

position_x=[
    [60,190,320,450,580,710],
]
position_y=[
    [730,860,990,1120,1250]
]
print(position_x[0][non_pos[0]])

def UP(absolute_y):
    absolute_y = absolute_y -130
    return absolute_y
def DOWN(absolute_y):
    absolute_y = absolute_y +130
    return absolute_y
def LEFT(absolute_x):
    absolute_x = absolute_x -130
    return absolute_x
def RIGHT(absolute_x):
    absolute_x = absolute_x +130
    return absolute_x

if __name__ == '__main__':
    # 獲取特定視窗
    window = gw.getWindowsWithTitle('夜神模擬器1')[0]
    # 計算滑鼠應該移動到的螢幕座標
    absolute_x = window.left + position_x[0][non_pos[1]]
    absolute_y = window.top + position_y[0][non_pos[0]]
    # 移動滑鼠到指定位置
    pyautogui.moveTo(absolute_x, absolute_y)
    pyautogui.mouseDown()
    for i in range(len(Move)):
        if Move[i] == 1:
            new_y = UP(absolute_y)
            pyautogui.moveTo(absolute_x, new_y, duration=0.01)
            absolute_y = new_y
        elif Move[i] == 2:
            new_y = DOWN(absolute_y)
            pyautogui.moveTo(absolute_x, new_y, duration=0.01)
            absolute_y = new_y
        elif Move[i] == 3:
            new_x = LEFT(absolute_x)
            pyautogui.moveTo(new_x, absolute_y, duration=0.01)
            absolute_x = new_x
        elif Move[i] == 4:
            new_x = RIGHT(absolute_x)
            pyautogui.moveTo(new_x, absolute_y, duration=0.01)
            absolute_x = new_x
        # 放開左鍵
    pyautogui.mouseUp()






