
#!/usr/bin/env python3
# screenshot_tool.py
import pyautogui
from datetime import datetime
from pathlib import Path

print("Nachtatem breitet seine Schwingen aus und macht einen Screenshot...")

def take_screenshot(save_dir='screenshots', region=None):
    Path(save_dir).mkdir(exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = Path(save_dir) / f'screen_{ts}.png'
    # region = (left, top, width, height) oder None
    img = pyautogui.screenshot(region=region)
    img.save(filename)
    return filename

if __name__ == '__main__':
    print("Meschlein, ich mache einen kompletten Screenshot in 2s...")
    pyautogui.sleep(2)
    fn = take_screenshot()
    print(f"Screenshot sicher gespeichert in meinem Hort: {fn}")
