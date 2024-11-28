def append_line(given_line):
    with open('someData.txt', 'a') as editedFile:
        editedFile.write("\n")
        editedFile.write(given_line)

def overwrite_file_with_line(given_line):
    with open('someData.txt', 'w') as editedFile:
        editedFile.write(given_line)

while(True):
    line = input("You can append new line (or type 'exit' if you want to continue)): ")
    if line.upper() == 'EXIT':
        break
    append_line(line)

with open('someData.txt', 'r') as file:
    for line in enumerate(file.read().splitlines()):
        print(f'{f'{line[0]+1}:':<5}{line[1]}')

overwrite_file = input('Do you want to edit file? (Type "Yes" if you do): ').upper() == 'YES'
new_file = ''
while(True):
    line = input("You can append new line (or type 'exit' if you want to continue)): ")
    if line.upper() == 'EXIT':
        break
    new_file += line + '\n'
overwrite_file_with_line(new_file)