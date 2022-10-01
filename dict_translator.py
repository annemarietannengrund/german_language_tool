
import googletrans
from googletrans import Translator
from progress.bar import Bar
import json

TRANSLATOR = Translator()

def list_available_languages()->None:
    for language_key, language_name in googletrans.LANGUAGES.items():
        print(language_key, language_name)

def load_language_json(path_to_json:str)->dict:
    with open(path_to_json, "r") as f:
        try:
            return json.loads(f.read())
        except Exception as exc:
            print(exc)

def create_language_from_dict(src_dict:dict, src_lang:str, tgt_lang:str)->dict:
    new_language = {}
    bar = Bar(f"Processing {src_lang} -> {tgt_lang}", max=len(src_dict))
    for key, value in src_dict.items():
        translation = value if src_lang == tgt_lang else get_gt(value, src_lang, tgt_lang)
        new_language[key] = translation
        bar.next()
    bar.finish()
    return new_language

def get_gt(value, src_lang, tgt_lang)->str:
    return TRANSLATOR.translate(value, src=src_lang, dest=tgt_lang).text

def dump_to_json(data:dict, tgt_path:str)->None:
    with open(tgt_path, 'w') as f:
        f.write(json.dumps(data, indent=4))

def create_i18n_files_from_config(config:dict)->None:
    src_lang = config.get("src_path").format(config.get("src_language"))
    print(f"parsing source json: {src_lang}")
    src_language_dict = load_language_json(path_to_json=src_lang)
    languages_compiled = {}
    compiled_src = {}
    for key, item in src_language_dict.items():
        compiled_src[key] = item
    compiled_src["language_name"] = googletrans.LANGUAGES.get(config.get("src_language"))
    languages_compiled[config.get("src_language")] = compiled_src
    for target_language_code in config.get("tgt_languages"):
        if config.get("tgt_languages") == config.get("src_language"):
            continue
        target_language = create_language_from_dict(
            src_dict=src_language_dict,
            src_lang=config.get("src_language"),
            tgt_lang=target_language_code
        )
        eng_lang_name = googletrans.LANGUAGES.get(target_language_code)
        target_language["language_name_english"] = eng_lang_name
        target_language["language_name_native"] = get_gt(eng_lang_name, "en", target_language_code)
        languages_compiled[target_language_code] = target_language
    dump_to_json(languages_compiled, "translated.json")

if __name__ == "__main__":
    config = {
        "src_language": "en",
        "tgt_languages": ["de", "en",],#"bg", "fr", "it", "pl", "es", "fa"], # use googletrans.LANGUAGES.keys() for all 107 languages
        "src_path": "translation.en.json"
    }
    create_i18n_files_from_config(config)
    #for key, lang in googletrans.LANGUAGES.items():
        #print(key, lang)
    #lang = load_language_json(config.get("src_path"))
    #print(lang)