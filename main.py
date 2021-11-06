# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def read_template():
    with open("./Input/Letters/starting_letter.docx", "r") as temp:
        lines = temp.readlines();
    return lines


def read_names():
    lines = []
    with open("./Input/Names/invited_names.txt", "r") as names_lines:
        for name_line in names_lines:
            replaced = name_line.rstrip('\r\n')
            lines.append(replaced)  # strip out all tailing whitespace
    return lines


names = read_names()
template = read_template()

for n in names:
    lines = []
    for line in template.copy():
        lines.append(line.replace("[name]", n))
    with open(f"./Output/ReadyToSend/letter_{n}.txt", "w") as letter:
        letter.writelines(lines)
