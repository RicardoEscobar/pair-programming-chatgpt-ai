from pathlib import Path


def generate_prompt(prompt: str, text_file_path: str | Path = None) -> str:
    # Load source code file
    if text_file_path:
        with open(text_file_path, mode='r', encoding='utf-8') as file:
            python_source_code = f"```python\n{file.read()}```"
    else:
        python_source_code = ''

    return prompt + python_source_code
