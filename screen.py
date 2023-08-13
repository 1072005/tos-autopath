import pygetwindow as gw
import pyautogui

# 獲取特定視窗
window = gw.getWindowsWithTitle('夜神模擬器1')[0]

# 截取該視窗
screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
screenshot.save('input.png')
