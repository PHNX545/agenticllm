import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:

        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        # Case handling
        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(target_dir) == False:
            return f'Error: "{directory}" is not a directory'
        else:
            lines = []
            for name in os.listdir(target_dir):

                size = os.path.getsize(os.path.join(target_dir, name))
                is_dir = os.path.isdir(os.path.join(target_dir,name))
                lines.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')

            return "\n".join(lines)



    except Exception as e:
        return f'Error: {e}'

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
