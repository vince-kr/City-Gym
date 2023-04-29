import PySimpleGUI as sg
import actions
import elements

actions = {
    "Calcuate cost": actions.calculate_cost,
    "Become a member": actions.enlist_new_member,
}

window = elements.build_gui_window(actions)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in actions:
        action = actions[event]
        sg.Popup(action(values), title="City Gym")

window.close()
