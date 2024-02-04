import os

def execute_command(command):
    os.system(command)

user_input = input("Enter your name: ")
execute_command("echo Hello, " + user_input)
ai.api_key = "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"
