
PLACE_HOLDER = "[name]"

with open("Day24\\Input\\Names\\invited_names.txt") as names:
    names_list = names.readlines()
    


with open("Day24\Input\Letters\starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names_list:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACE_HOLDER, striped_name)
        with open(f"Day24\Output\ReadyToSend\{striped_name}.txt", "w") as output:
            output.write(new_letter)





