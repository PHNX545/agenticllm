import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if valid_target_file == False:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file) == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        else:
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            with open(target_file, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": (
            "Writes text content to a file, overwriting it if it already exists and "
            "creating any missing parent directories."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "Path to the file to write, relative to the working directory "
                        "(e.g., \"main.py\" or \"pkg/calculator.py\"). Paths that resolve "
                        "outside the working directory are rejected."
                    ),
                },
                "content": {
                    "type": "string",
                    "description": "The full text to write to the file.",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
