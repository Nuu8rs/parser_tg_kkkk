def format_message(title, user, text):
    return f'''
📢:{title}
🗣:{user}

💬:{text}
    '''

def get_keywords():
    with open("keywords.txt", "r") as f:
        return f.read().split(",")
   

def add_keyword(word):
    try:
        with open("keywords.txt", "r") as f:
            data = f.read().split(",")
    except:
        data = []
    finally:
        data.append(word)
        with open("keywords.txt", "w") as f:
            f.write(",".join(data))

def del_keyword(word):
    try:
        with open("keywords.txt", "r") as f:
            data = f.read().split(",")
    except:
        data = []
    finally:
        if word in data:
            data.remove(word)
            result = f"Успешно удалено слово '{word}'"
            with open("keywords.txt", "w") as f:
                f.write(",".join(data))
        else:
            result = f"Слово '{word}' не найдено среди стоп слов"
        return result
