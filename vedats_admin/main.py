import json
import subprocess

def load_poems_from_json():
    try:
        with open("/Users/vedatvezir/Desktop/Poem_App/quotes.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    poems = load_poems_from_json()
    for poem in poems[0:1]:
        poet = poem['author']
        poem_content = poem['text']
        
        subprocess.run(['python', 'Poems-admin/vedats_admin/adminInterface.py', 'add-poem', poem_content, '--poet', poet])

if __name__ == '__main__':
    main()
