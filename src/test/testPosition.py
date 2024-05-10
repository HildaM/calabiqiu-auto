import pyautogui
import pydirectinput

def check_one_image(image_path):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=5, confidence=0.8)
        if location:
            return location
    except pyautogui.ImageNotFoundException:
        pass
    return False

def main():
    test_image_paths = "D:\\GitHub\\calabiqiu-auto\\src\\images\\test.png"
    location = check_one_image(test_image_paths)
    print(location.x, location.y)
    pydirectinput.moveTo(location.x, location.y)
    pydirectinput.click()


if __name__ == '__main__':
    main()