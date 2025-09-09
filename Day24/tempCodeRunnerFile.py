with open("Day24\Input\Letters\starting_letter.txt") as template:
    for name in names_list:
        striped_name = name.strip()
        new_letter = template.replace(PLACE_HOLDER, striped_name)
        print(new_letter)