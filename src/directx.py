import time
import pydirectinput
from size import get_resize
from pydirectinput import (
    keyDown,
    keyUp,
    leftClick,
    move,
    moveTo,
    mouseUp,
    mouseDown,
    RIGHT,
    press,
)
from loguru import logger

from settings import map_selecte_settings, kick_settings, key_settings


pydirectinput.PAUSE = 0


def press_and_hold_key(key: str, seconds: float):
    logger.debug(f'press key "{key}" {seconds} seconds')

    keyDown(key)
    time.sleep(seconds)
    keyUp(key)



def move_to_and_left_click(x: int = None, y: int = None):
    logger.debug(f"鼠标移动至 ({x}, {y})，左键点击")

    pydirectinput.moveTo(x, y)
    time.sleep(map_selecte_settings.鼠标移动和单击时间间隔)
    pydirectinput.leftClick()


def run(secons: float):
    keyDown("shiftleft")
    time.sleep(0.001)
    keyDown("w")
    time.sleep(secons)
    keyUp("shiftleft")
    keyUp("w")


def open_map_and_switch_difficulty():
    # 打开地图 - Open map
    press("m")
    time.sleep(1)

    # 点击战争领主的废墟 - Select Warlord's Ruin
    moveTo(get_resize(2360)) #2360
    time.sleep(0.3)
    leftClick()

    # 点开难度选择 - Select Difficulty
    time.sleep(1.5)
    move_to_and_left_click(*get_resize(1960, 1110))

    # 选择大师难度 - Select Master Difficulty
    time.sleep(1.5)
    move_to_and_left_click(*get_resize(455, 460))


def start_next_round():
    open_map_and_switch_difficulty()

    # 点击开始 - Start
    time.sleep(2)
    move_to_and_left_click(*get_resize(2180, 1210))


def refresh_checkpoint():
    open_map_and_switch_difficulty()

    # F进度 - Reset Checkpoint
    moveTo(*get_resize(1805, 1115))
    time.sleep(1)
    press_and_hold_key("f", 4)

    for _ in range(2):
        press("esc")
        time.sleep(0.5)

    run(10)
    logger.info("Progress Reset")


def kick_boss_by_indebted_kindess():
    # 切枪
    press("2")
    time.sleep(2)

    # 开启boss
    move(*kick_settings.command.开BOSS鼠标偏移, relative=True)
    time.sleep(0.5)
    leftClick()
    time.sleep(0.2)

    # 跳x隐身
    press("space")
    time.sleep(0.2)
    press(key_settings.跳隐身按键)
    time.sleep(1)

    # 移动到预设的位置
    press_and_hold_key("a", kick_settings.command.隐身后往左走时间)
    press_and_hold_key("w", kick_settings.command.隐身后往前走时间)

    # 射击黄血小怪
    mouseDown(button=RIGHT)
    time.sleep(0.3)
    move(*kick_settings.command.射击黄血鼠标偏移, relative=True)
    time.sleep(kick_settings.command.等待黄血刷新时间)
    leftClick()
    mouseUp(button=RIGHT)

    # 终结小怪
    keyDown(key_settings.终结技按键)
    run(1.7)
    keyUp(key_settings.终结技按键)


def hide_indebted_kindess():
    move(*kick_settings.command.躲藏第一段位移镜头偏移, relative=True)
    keyDown("w")
    keyDown("shiftleft")
    time.sleep(kick_settings.command.躲藏第一段位移时间)
    move(*kick_settings.command.躲藏第二段位移镜头偏移, relative=True)
    time.sleep(kick_settings.command.躲藏第二段位移时间)

    keyUp("shiftleft")
    keyUp("w")
    time.sleep(0.5)
    press(key_settings.埋头表情按键)






