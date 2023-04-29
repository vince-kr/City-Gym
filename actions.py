def calculate_cost(values: dict):
    base_fee = values["Basic"] * 10 or values["Regular"] * 15 or values["Premium"] * 20
    duration = (
        values["months3"] * 13 or values["months12"] * 52 or values["months24"] * 104
    )
    duration_discount = values["months12"] * (52 * 2) or values["months24"] * (104 * 5)
    membership_cost = base_fee * duration - duration_discount
    if values["yes"]:
        membership_cost *= 0.99
    extras_cost = (
        1 * values["Access"] * duration
        + 20 * values["Trainer"] * duration
        + 20 * values["Diet"] * duration
        + 2 * values["Videos"] * duration
    )
    total_fee = membership_cost + extras_cost
    weekly_fee = total_fee / duration
    return f"The weekly fee for your selection is: {weekly_fee:.2f}\nThe total fee for the selected duration is: {total_fee:.2f}"


def enlist_new_member(values: dict):
    pass
