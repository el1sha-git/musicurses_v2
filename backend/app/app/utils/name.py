from slugify import slugify
from transliterate import translit, get_available_language_codes

def get_song_name(name: str, filename: str):
    file_expansion = filename.split('.')[-1]
    translited_name = translit(name, 'ru', reversed=True)
    slugify_name = slugify(translited_name)
    return slugify_name + '.' + file_expansion
