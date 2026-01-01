FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ This function open the todos.txt file and reads content into list"""
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_local,filepath=FILEPATH):
    with open(filepath,"w") as file_local:
        file_local.writelines(todos_local)

def parse(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet,inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

if __name__ == "__main__":
    todos = get_todos()
    write_todos(todos)
    print("hello from functions")