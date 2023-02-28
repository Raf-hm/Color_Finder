try:
    import PIL.ImageGrab
    import pyautogui
    import colorsys
    from pynput import keyboard
except:
    print("ERROR: importing modules.")
    input()
    exit()


data = {
    "x":"",
    "y":"",
    "rgb":"",
    "hex":"",
    "hsv":"",
    "hsl":""
}


print("Press F to find the color under your cursor (Main screen only)")
print("--------------------------------------------------------------")


def rgb_hsv(rgb):
    rgbSpliced = str(rgb).replace("(","").replace(")","").split(",")
    r, g, b = int(rgbSpliced[0]), int(rgbSpliced[1]), int(rgbSpliced[2])
    r, g, b = r / 255, g / 255, b / 255

    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    (h, s, v) = (int(h * 360), int(s * 100), int(v * 100))
    return h, s, v

def rgb_hls(rgb):
    rgbSpliced = str(rgb).replace("(","").replace(")","").split(",")
    r, g, b = int(rgbSpliced[0]), int(rgbSpliced[1]), int(rgbSpliced[2])
    r, g, b = r / 255, g / 255, b / 255

    (h, s, l) = colorsys.rgb_to_hls(r, g, b)
    (h, s, l) = (int(h * 360), int(s * 100), int(l * 100))
    return h, l, s


def main(key):
    try:
        if key.char=="f":
            data["x"] = pyautogui.position().x
            data["y"] = pyautogui.position().y

            data["rgb"] = PIL.ImageGrab.grab().load()[data["x"],data["y"]]
            data["hex"] = "#%02x%02x%02x" % data["rgb"]
            data["hsv"] = rgb_hsv(data["rgb"])
            data["hsl"] = rgb_hls(data["rgb"])

            print("X: " + str(data["x"]) + " | Y: " + str(data["y"]) + "\n")
            print("HEX --> " + str(data["hex"]))
            print("RGB --> " + str(data["rgb"]))
            print("HSV --> " + str(data["hsv"]))
            print("HSL --> " + str(data["hsl"]))
            print("-----------------------")
    except AttributeError:
        pass


with keyboard.Listener(on_press=main) as listener:
    listener.join()

