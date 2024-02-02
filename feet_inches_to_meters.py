import PySimpleGUI as SimpGUI
from converter_functions import feet_inches_to_meters


SimpGUI.theme("Black")

label1 = SimpGUI.Text("Enter Feet: ")
input1 = SimpGUI.Input()

label2 = SimpGUI.Text("Enter Inches: ")
input2 = SimpGUI.Input()

convert_button = SimpGUI.Button("Convert", key="convert")
exit_button = SimpGUI.Button("Exit", key="exit")
output_label = SimpGUI.Text(text_color="green", key="output")

window = SimpGUI.Window("Convertor",
                        layout=[[label1, input1],
                                [label2, input2],
                                [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()

    if event == SimpGUI.WIN_CLOSED or event == "exit":
        break
    elif event == "convert":
        try:
            window["output"].update(feet_inches_to_meters(float(values[0]), float(values[1])))
        except ValueError:
            SimpGUI.popup("Enter valid values into the input boxes.")

window.close()
