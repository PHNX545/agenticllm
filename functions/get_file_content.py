import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        # Case handling
        if valid_target_dir == False:
            return f'Error: Cannot read "{target_file}" as it is outside the permitted working directory'
        if os.path.isfile(target_file) == False:
            return f'Error: File not found or is not a regular file: "{target_file}"'

        else:
            try:
                with open(target_file, "r") as f:
                    content = f.read(MAX_CHARS)
                    if f.read(1):
                        content += f'[...File "{target_file}" truncated at {MAX_CHARS} characters]'
                return content

            except Exception as e:
                return f'Error: {e}'


    except Exception as e:
        return f'Error: {e}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads contents of a specified file up to a given number of characters (MAX_CHARS)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory (e.g., \"main.py\" or \"pkg/calculator.py\"). Must point to a regular file inside the working directory; paths that resolve outside it are rejected.",
                },
            },
        },
    },
}
