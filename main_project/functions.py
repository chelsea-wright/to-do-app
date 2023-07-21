FILEPATH = "main_project/input_file.txt"
def get_todos(filepath=FILEPATH):
    """Return the items in a to-do list"""
    with open(filepath, 'r') as file_local:
        object_list_local = file_local.readlines()
    return object_list_local

def write_todos(to_do, filepath_write=FILEPATH):
    """Write a to-do items list in a text file"""
    with open(filepath_write, 'w') as file_to_writeto:
        file_to_writeto.writelines(to_do)