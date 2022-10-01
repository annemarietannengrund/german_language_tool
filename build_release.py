import PyInstaller.__main__
from googletrans import Translator, LANGUAGES
import json

TRANSLATOR = Translator()


def list_available_languages() -> None:
    for language_key, language_name in LANGUAGES.items():
        print(language_key, language_name)


def load_language_json(path_to_json: str) -> dict:
    with open(path_to_json, "r") as f:
        try:
            return json.loads(f.read())
        except Exception as exc:
            print(exc)


def create_language_from_dict(src_dict: dict, src_lang: str, tgt_lang: str) -> dict:
    new_language = {}
    for key, value in src_dict.items():
        translation = value if src_lang == tgt_lang else get_gt(value, src_lang, tgt_lang)
        new_language[key] = translation
    return new_language


def get_gt(value, src_lang, tgt_lang) -> str:
    return TRANSLATOR.translate(value, src=src_lang, dest=tgt_lang).text


def dump_to_json(data: dict, tgt_path: str) -> None:
    with open(tgt_path, 'w') as f:
        f.write(json.dumps(data, indent=4))


def translate_content(config: dict) -> None:
    src_json_path = config.get("src_path").format(config.get("src_language"))
    src_language_dict = load_language_json(src_json_path)
    translation_base = src_language_dict.get('translation_base')
    reserved = src_language_dict.get("translation_reserved")

    languages_compiled = {}
    compiled_src = {}
    for key, item in translation_base.items():
        compiled_src[key] = item
    compiled_src["language_name"] = LANGUAGES.get(config.get("src_language"))
    languages_compiled[config.get("src_language")] = compiled_src
    for target_language_code in config.get("tgt_languages"):
        if config.get("tgt_languages") == config.get("src_language"):
            continue
        target_language = create_language_from_dict(
            src_dict=src_language_dict.get('translation_base'),
            src_lang=config.get("src_language"),
            tgt_lang=target_language_code
        )
        eng_lang_name = LANGUAGES.get(target_language_code)
        target_language["language_name_english"] = eng_lang_name
        target_language["language_name_native"] = get_gt(eng_lang_name, "en", target_language_code)
        languages_compiled[target_language_code] = target_language

    dump_to_json({"translation_base": languages_compiled, "reserved": reserved}, "assets/translated.json")


def get_translation_config() -> dict:
    return {
        "src_language": "en",
        "tgt_languages": ["de", "en"],
        "src_path": "translation.base.json"
    }


if __name__ == "__main__":
    # list_available_languages()
    translate_content(get_translation_config())
    PyInstaller.__main__.run([
        '-y',
        'main.spec',
    ])
