# Auto Rotate — TODO

## Bugs
- [ ] Fix overly broad `try/except` in `on_key_press` (catches all exceptions silently)
- [ ] Correct comment "F1 pressed" in `event_listeners.py:34` — it checks `Key.f12`, not F1
- [ ] Fix mismatched comment "F2 pressed" for `Key.f11` in `event_listeners.py:38`
- [ ] `fg='Orange'` should be `fg='orange'` (tkinter color names are lowercase)

## Features
- [ ] Add F1/F2 manual rotation buttons to the UI
- [ ] Show current rotation state / countdown in the UI
- [ ] Add a system tray icon for background operation
- [ ] Allow user to configure rotation interval via UI
- [ ] Make the window stay-on-top while auto-rotating

## Improvements
- [ ] Use `threading` instead of sequential `after()` timers for activity checking
- [ ] Refactor `UI.auto_rotate()` — it's called both as initial start and as loop step
- [ ] Consolidate `rotate_forward()` / `rotate_backward()` into a single method with direction param
- [ ] Add logging instead of bare `print()` calls
- [ ] Add type hints
- [ ] Package with PyInstaller (`.spec` already exists)
