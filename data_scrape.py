import pyautogui
import time
import keyboard

prompt_list = []
with open("questions.txt", "r") as file:
    for line in file:
        prompt_list.append(line.strip())


time.sleep(5)

done = False
while not done:
    for prompt in prompt_list:
        if keyboard.is_pressed('shift'):
            break
        pyautogui.typewrite(f"'{prompt}' write 10 answer each in one line and write the question as number one")
        pyautogui.hotkey('enter')
        time.sleep(14)

        pyautogui.moveTo(706, 365)

        # Simulate a mouse click (holding down the left button)
        pyautogui.mouseDown()

        # Move the mouse to the ending position to complete the drag
        pyautogui.moveTo(1605, 741, duration=1)  # You can adjust the duration as needed

        # Release the mouse button (end the drag)
        pyautogui.mouseUp()
        #
        pyautogui.hotkey('ctrl', 'c')

        pyautogui.moveTo(1147, 1048)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(775,73)
        pyautogui.click()
        time.sleep(1)
        pyautogui.hotkey('ctrl','v')
        pyautogui.hotkey('enter')
        pyautogui.moveTo(928,1042)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(751,916)
        pyautogui.click()
        pyautogui.hotkey('ctrl','a')
    done = True

# # top left x:694 y:191
# bottom right x:1500 y:747
