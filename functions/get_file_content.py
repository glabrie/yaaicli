import os

def get_file_content(working_directory: str, file_path: str) -> str:
    target = os.path.abspath(os.path.join(working_directory, file_path))
    working = os.path.abspath(working_directory)
    if not target.startswith(working):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        MAX_CHARS = 10000
        try:
            with open(target, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                
                if len(file_content_string) >= MAX_CHARS:



