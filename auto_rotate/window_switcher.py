import win32gui
import win32con
import win32process


class WindowSwitcher:
    def __init__(self):
        self.app_windows = []
        self.current_index = 0

    # Quick test
    def test_alt_esc_method():
        import pyautogui

        print("Opening 3 apps (Excel, Notepad, Chrome)...")
        input("Open 3 apps, then press Enter...")

        for i in range(5):
            print(f"Switch {i + 1}")
            pyautogui.hotkey('alt', 'esc')
            time.sleep(0.5)

            # Maximize current window
            hwnd = user32.GetForegroundWindow()
            user32.ShowWindow(hwnd, 3)  # Maximize

            time.sleep(2)

    test_alt_esc_method()