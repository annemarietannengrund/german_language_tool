import json
import platform
import tkinter as tk
from os.path import splitext, realpath, join as os_join, isfile

from playsound import playsound

from appframes import PageBaseFrame
from page_toc import get_toc


class GermanLanguageTool(tk.Tk):
    lang: str
    title = "German Language Tool"
    translation_file = "translated.json"
    translate_map: dict
    frameregister = {}

    LARGE_FONT = ("Arial", 24)
    MEDIUM_FONT = ("Arial", 18)
    SMALL_FONT = ("Arial", 12)

    DISPLAY_FRAME_COLORED = False
    DISPLAY_CANVAS_COLORED = False
    language_switcher_path = ""

    def __init__(self, lang="en", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, self.title)
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.minsize(800, 600)
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())
        self.translate_map = {}
        self.translate_raw_map = {}
        self.available_languages = {}
        self.platform = platform.system()
        self.set_language(lang)
        self.init_mainframe_container()
        self.init_page_frames()
        self.show_frame(self.default)

    def join_path(self, part1, part2):
        return os_join(part1, part2)

    def is_file(self, path):
        return isfile(path)

    # silly pathhandling for mac app
    def get_filepath(self, filename):
        name = splitext(filename)[0]
        ext = splitext(filename)[1]
        if self.platform == "Darwin":
            from AppKit import NSBundle
            file = NSBundle.mainBundle().pathForResource_ofType_(name, ext)
            return file or realpath(filename)
        else:
            return realpath(filename)

    # LANGUAGE

    def set_language(self, lang):
        self.lang = lang
        self.load_translations(self.lang)

    def handle_language_dropdown(self, option):
        if (dropdown := self.nametowidget(self.language_switcher_path)):
            lang = dropdown.get().split('-')[0].strip()
            self.set_language(lang)

    def load_translations(self, lang):
        self.translate_map = {}
        self.translate_raw_map = {}
        path = self.get_filepath(self.translation_file)
        with open(path, "r", encoding="utf-8") as f:
            translations = json.loads(f.read())
        if not self.available_languages:
            for code, content in translations.items():
                self.available_languages[code] = {
                    "language_name_english": content.get("language_name_english"),
                    "language_name_native": content.get("language_name_native"),
                }
        self.translate_raw_map = translations.get(lang)
        self.init_string_var_translation_components()

    def update_translation(self, key, new_text):
        self.translate_map[key].set(new_text)

    def init_string_var_translation_components(self):
        for key, translation in self.translate_raw_map.items():
            translation = translation.replace('__UUNNDD__', 'und')
            translation = translation.replace('__SZ__', 'ß')
            translation = translation.replace('__DREI__', 'Drei')
            translation = translation.replace('__ZWEI__', 'Zwei')
            translation = translation.replace('__VIER__', 'Vier')
            translation = translation.replace('__DREISZIG__', 'Dreißig')
            translation = translation.replace('__20__', 'Zwanzig')
            translation = translation.replace('__30__', 'Dreißig')
            translation = translation.replace('__90__', 'Neunzig')
            translation = translation.replace('__HUNDERT__', 'hundert')
            translation = translation.replace('__TAUSEND__', 'tausend')
            if key in self.translate_map.keys():
                self.update_translation(key, translation)
            else:
                self.translate_map[key] = tk.StringVar(value=translation, name=key)

    def translate(self, key, raw_text=False):
        if key not in self.translate_map.keys():
            return key
        if raw_text:
            return self.translate_map[key].get()
        return self.translate_map[key]

    def get_language_dropdown_options(self):
        return [f"{key} - {c.get('language_name_native')}" for key, c in self.available_languages.items()]

    def register_frame(self, frame, framekey):
        self.frameregister[framekey] = frame

    def get_frame(self, key):
        return self.frameregister.get(key)

    def get_available_pages(self):
        return get_toc()

    def init_mainframe_container(self):
        # initializing the main frame container
        self.container = tk.Frame(self, name="base_container")
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.pack()

    def init_page_frames(self):
        self.frames = {}
        for PageName, PageData in self.get_available_pages().items():
            PageClass = type(PageName, (PageBaseFrame,), {})
            frame = PageClass(self.container, PageData)
            if PageData.get("default"):
                self.default = PageClass
            self.frames[PageClass] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
            frame.grid_rowconfigure(0, weight=1)

    def show_frame(self, cont, lookup_class=False):
        if lookup_class:
            for frame_class in self.frames.keys():
                if f"<class '__main__.{cont}'>" in str(frame_class):
                    cont = frame_class
                    break
        frame = self.frames[cont]
        frame.tkraise()

    def quit(self):
        self.destroy()

    def play_sound(self, filepath):
        for path in filepath:
            playsound(path)


if __name__ == "__main__":
    app = GermanLanguageTool(lang="en")
    app.mainloop()
