import os

def execute_command(command):
    result = os.popen(command).read()
    return result

if __name__ == '__main__':
    user_input = input("Enter a filename: ")
    execute_command('ls ' + user_input)
