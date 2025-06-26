import os

def get_file_content(working_directory: str, file_path: str) -> str:
    if file_path not in working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        MAX_CHARS = 10000

        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)


