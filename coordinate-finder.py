from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse clicked at: x={x}, y={y}')
        return False  # Stop the listener after the first click

# Set up the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
