import os

def get_files_info(working_directory: str, directory: str | None = None) -> str:
    if directory is None:
        directory = "."
    target = os.path.abspath(os.path.join(working_directory, directory))
    working = os.path.abspath(working_directory)
    if not target.startswith(working):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(target):
        return f'Error: "{directory}" is not a directory'
    else:
        try:
            content_list: list[str] = []
            for content in os.listdir(target):
                full_path = os.path.join(target, content)
                file_name = content 
                file_size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                string = f'{file_name}: file_size={file_size} bytes, is_dir={is_dir}'
                content_list.append(string)
            return "\n".join(content_list)
        except Exception as e:
            return f'Error: An error occured: {e}'
