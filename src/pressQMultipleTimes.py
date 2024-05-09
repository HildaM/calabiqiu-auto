import pydirectinput
import time

def main():
    time.sleep(2)
    count = 1
    # 循环按下 "Q" 键
    for i in range(300):
        pydirectinput.press('q')
        # 添加一点延迟，以防止按键速度过快
        time.sleep(0.05)
        count += 1
        print(count)

if __name__ == '__main__':
    main()