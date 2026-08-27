import os
import re

root_dir = r"c:\AI\tom-projects\learning\civil-exam-it"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html"):
            filepath = os.path.join(dirpath, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if "tts.js" in content:
                continue
                
            # Calculate relative path to root assets
            rel_path = os.path.relpath(root_dir, dirpath)
            if rel_path == ".":
                script_src = "assets/tts.js"
            else:
                script_src = f"{rel_path.replace(os.sep, '/')}/assets/tts.js"
                
            script_tag = f'\n<script src="{script_src}"></script>\n'
            
            # Inject before </body>
            new_content = content.replace('</body>', f'{script_tag}</body>')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Injected into {filepath}")

print("Injection complete.")
