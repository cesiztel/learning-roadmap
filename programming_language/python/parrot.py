message = input("Tell me something, and I will repeat it back to you:")
print(message)

exit_command = 'quit'
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += f"\nEnter '{exit_command}' to end the program. "
message = ""
while message != exit_command:
    message = input(prompt)
    print(message)