import PySimpleGUI as sg
from collections import namedtuple

sg.theme("DarkGrey")

TITLE = "Welcome to City Gym"

# I'm using a namedtuple to keep track of label-key combinations
# This is useful for all types of inputs
Lackey = namedtuple("Lackey", ("label", "key"))

# Define input fields for customer details
CUSTOMER_DETAILS = (
    Lackey("First Name", "Fname"),
    Lackey("Last Name", "Lname"),
    Lackey("Age", "Age"),
    Lackey("Address", "Address"),
    Lackey("Mobile number", "Phone"),
)

# Define radio buttons for options
# These are a bit trickier, because you need to keep track of the title and
# group name for each group, so I'm adding another namedtuple
Radiobutton = namedtuple("Radiobutton", ("title", "group", "lackeys"))

RADIO_BUTTONS = [
    Radiobutton(
        "Type Of Membership",
        "membership_type",
        (
            Lackey("Basic $10 per week", "Basic"),
            Lackey("Regular $15 per week", "Regular"),
            Lackey("Premium $20 per week", "Premium"),
        ),
    ),
    Radiobutton(
        "Duration",
        "membership_duration",
        (
            Lackey("3 months", "months3"),
            Lackey("12 months*", "months12"),
            Lackey("24 months**", "months24"),
        ),
    ),
    Radiobutton(
        "Payment Options",
        "payment_freq",
        (
            Lackey("Weekly", "Weekly"),
            Lackey("Monthly", "Monthly"),
        ),
    ),
    Radiobutton(
        "Direct Debit",
        "payment_method",
        (
            Lackey("Yes***", "yes"),
            Lackey("No", "no"),
        ),
    ),
]

# Define checkboxes for more options
# These are similar to the input fields: just a label and key
CHECKBOX_EXTRAS = (
    Lackey("24/7 access ($1 per week)", "Access"),
    Lackey("Personal trainer($20 per week)", "Trainer"),
    Lackey("Diet consultation($20 per week)", "Diet"),
    Lackey("Online fitness videos($2 per week)", "Videos"),
)

# The lines of explanatory text at the bottom
TEXT = (
    "-" * 230,
    "* Sign up for a 12-month contract to receive a $2 per week discount on any membership type.",
    "** Sign up for 24 months to receive a $5 per week discount on any membership type.",
    "*** For direct debits, there is a 1 percent discount on the base membership cost.",
)


# Now add everything to layout
layout = []


# Customer details
layout.append([sg.Text("Customer Details")])

for label, key in CUSTOMER_DETAILS:
    layout.append(
        [
            sg.Text(label, size=(15, 1)),
            sg.InputText(key=key, do_not_clear=False),
        ]
    )


# For the radio buttons I append to layout for each group and inside the group I
# append for each option, so each appears on its own line
for option in RADIO_BUTTONS:
    layout.append([sg.Text(option.title)])
    for label, key in option.lackeys:
        layout.append([sg.Radio(label, option.group, key=key)])


# For the checkboxes I add each Checkbox as a list element and then append to
# the layout once, so they all appear on the same line
layout.append([sg.Text("Extras, Please Select")])

list_of_extras = [sg.Checkbox(label, key=key) for label, key in CHECKBOX_EXTRAS]
layout.append(list_of_extras)


# Text needs to go each on their own line again, so we call a separate append for each
for line in TEXT:
    layout.append([sg.Text(line)])


def build_gui_window(actions: dict, layout: list = layout):
    layout.append([sg.Button(action) for action in actions.keys()])

    return sg.Window(
        TITLE,
        layout,
    )
