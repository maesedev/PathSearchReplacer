import os

def buscar_reemplazar(directory, extencions, word_by_search, word_by_replace):
    for current_path, directorys, files in os.walk(directory):
        for file in files:
            if any(file.endswith(extension) for extension in extencions):
                fila_path = os.path.join(current_path, file)
                with open(fila_path, 'r') as file:
                    content = file.read()
                
                modified_content = content.replace(word_by_search, word_by_replace)
                
                with open(fila_path, 'w') as file:
                    file.write(modified_content)
                
                print(f"the word '{word_by_search}' was replaced by '{word_by_replace}' in the file: '{fila_path}'.")

directory = '[<<The path here>>]'  
extencions = ['.html', '.txt', '.css']  
word_by_search = 'word to search'  
word_by_replace = 'word about to replace' 

buscar_reemplazar(directory, extencions, word_by_search, word_by_replace)


