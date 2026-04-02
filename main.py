import os
import html
import re


def define_env(env):
    @env.macro
    def code_from_file(filepath, start_line=None, end_line=None, language="python"):
        docs_dir = env.conf['docs_dir']
        file_path = os.path.abspath(os.path.join(docs_dir, filepath))

        if not os.path.exists(file_path):
            return f"<div class='error'>Файл не найден: {filepath}</div>"

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Если указаны start_line и end_line, обрезаем
        if start_line is not None and end_line is not None:
            lines = content.split('\n')
            selected_lines = lines[start_line - 1:end_line]
            code_content = '\n'.join(selected_lines)
        else:
            code_content = content

        code_content = html.escape(code_content)
        return f"```{language}\n{code_content}\n```"

    @env.macro
    def code_block(filepath, block_name=None, language="python"):
        """Вставка кода по меткам (аналог codeinclude)"""
        docs_dir = env.conf['docs_dir']
        file_path = os.path.abspath(os.path.join(docs_dir, filepath))

        if not os.path.exists(file_path):
            return f"<div class='error'>Файл не найден: {filepath}</div>"

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if block_name:
            # Ищем блок между метками <-- block-name и --> block-name
            start_pattern = rf'#\s*<--\s*{block_name}\s*-->?\s*$'
            end_pattern = rf'#\s*-->\s*{block_name}\s*$'

            in_block = False
            block_lines = []

            for line in lines:
                if re.match(start_pattern, line.strip()):
                    in_block = True
                    continue
                if in_block and re.match(end_pattern, line.strip()):
                    in_block = False
                    continue
                if in_block:
                    block_lines.append(line.rstrip())

            if block_lines:
                code_content = '\n'.join(block_lines)
            else:
                # Если не нашли блок, ищем старый формат с <-- block-name -->
                start_pattern_old = rf'#\s*<--\s*{block_name}'
                end_pattern_old = rf'#\s*-->\s*{block_name}'

                in_block = False
                block_lines = []

                for line in lines:
                    if re.match(start_pattern_old, line.strip()):
                        in_block = True
                        continue
                    if in_block and re.match(end_pattern_old, line.strip()):
                        in_block = False
                        continue
                    if in_block:
                        block_lines.append(line.rstrip())
        else:
            # Если block_name не указан, берем весь файл
            code_content = ''.join(lines)
            block_lines = code_content.split('\n')

        if not block_lines:
            return f"<div class='error'>Блок '{block_name}' не найден в {filepath}</div>"

        code_content = '\n'.join(block_lines)
        code_content = html.escape(code_content)
        return f"```{language}\n{code_content}\n```"