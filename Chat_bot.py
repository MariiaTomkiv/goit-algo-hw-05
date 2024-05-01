def input_error(func):
    def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "Give me name and phone please."
            except KeyError:
                return "Contact not found"
            except IndexError:
                return "Not found"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Changed."
    else:
        return "Contact not found"

def phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"

def all(args, contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change(args, contacts))
        elif command == "phone":
            print(phone(args, contacts))
        elif command == "all":
            print(all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()