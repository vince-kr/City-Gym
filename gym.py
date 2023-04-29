import PySimpleGUI as sg
import actions
import elements

actions = {
    "Become a member": actions.enlist_new_member,
    "Calcuate cost": actions.calculate_cost,
}

window = elements.build_gui_window(actions)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    action = actions[event]
    action(values)

window.close()
