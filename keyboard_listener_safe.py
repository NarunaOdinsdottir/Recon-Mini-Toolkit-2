
#!/usr/bin/env python3
# keyboard_listener_safe.py
# Lernzweck: zeigt, wie man mit pynput Keyboard-Events abfängt.
# NICHT für heimliche Überwachung verwenden!

from pynput import keyboard

print("Nachtatem lauscht den Tastenanschlägen...")

def on_press(key):
    try:
        print(f"Pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

def on_release(key):
    # stoppt wenn ESC gedrückt wird
    if key == keyboard.Key.esc:
        print("ESC gedrückt — Listener stoppt.")
        return False

if __name__ == '__main__':
    consent = input("Starte Keyboard-Listener? Du beobachtest deine eigenen Tastendrücke. (j/n) ")
    if consent.lower() != 'j':
        print("Abgebrochen.")
        exit(0)
    print("Listener läuft — drücke ESC zum Beenden.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
