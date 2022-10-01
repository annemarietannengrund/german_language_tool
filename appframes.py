import tkinter as tk
from tkinter.ttk import Button, Scrollbar, Combobox, Separator

class BaseFrame(tk.Frame):
    """Base Frame abstraction layer, to provide basic functionality like translations, layout and other stuff
    for specialized frame classes (PageFrame/ScrollFrame)
    The Page Frame is intended as a Frame that holds the contents of a page (menu and content)
    the scrollframe is intended to hold the content only.
    """

    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)
        self.controller = self.nametowidget('.')
        self.translate = self.controller.translate
        self.menu = []
        self.toc = {}
        self.config = {}

    page_toc = {}

    def create_content_frame(self, content_key):
        if (frame := self.controller.get_frame(content_key)):
            return frame
        content_frame = ScrollBaseFrame(self)
        content = self.toc.get(content_key).get("content")
        # wrapsize = 900
        # print("setting wrapsize to", wrapsize)
        self.build_page_by_toc(content, content_frame.interior)
        self.controller.register_frame(content_frame, content_key)
        return content_frame

    def set_default_content(self):
        for page_key, page_data in self.toc.items():
            if page_data.get("default"):
                self.default_page = page_key
                return
        raise Exception(f"couldnt find default content for {self.__class__}")

    def build_page_by_toc(self, content, page_container):
        for item in content:
            if item.get("type") == "seperator":
                self.horizontal_seperator(page_container)
                continue
            if item.get("type") == "audio_examples":
                speakers = self.config.get("available_speakers")
                basepath = self.config.get("audio_examples_path")
                filename_tpl = self.config.get("audio_examples_filename")
                number_item = item.get("data")
                button_frame = tk.Frame(master=page_container)
                for speaker in speakers:
                    snumber = speaker.get('number')
                    sname = speaker.get('name')
                    sgender = speaker.get('gender')
                    path: list[str] = []
                    for inumber in number_item:
                        fname = filename_tpl.format(snumber, inumber)
                        tpath = self.controller.get_filepath(self.controller.join_path(basepath, fname))
                        if not self.controller.is_file(tpath):
                            tpath = self.controller.get_filepath(fname)
                        # create filepath correctly
                        path.append(tpath)
                    Button(
                        button_frame,
                        text=f"🔊 {sgender} {sname}",
                        command=lambda p=path: self.controller.play_sound(p),
                    ).pack(anchor=tk.NW, side=tk.LEFT)
                button_frame.pack(anchor=tk.NW)
                continue
            key = item.get("key")
            key_exists = key in self.controller.translate_map.keys()
            translation = self.translate(key) if key_exists else key
            if item.get("type") == "headline":
                self.set_headline(page_container, translation)
            elif item.get("type") == "paragraph":
                self.set_paragraph(page_container, translation)
            elif item.get("type") == "newline":
                self.set_newline(page_container)

    def change_content(self, content_frame):
        self.content = self.create_content_frame(content_frame)
        self.content.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)
        self.content.tkraise()

    def get_menu_items(self) -> list:
        return self.menu

    def build_menu(self, menu):
        self.init_sidebar()
        for i, item in enumerate(menu):
            itype = item.get('type')
            textvar = self.translate(item.get("key"))
            if itype in ["button"]:
                element = Button(
                    self.sidebar,
                    command=item.get("function"),
                    textvariable=textvar
                )
            elif itype in ["quit_button"]:
                element = Button(
                    self.sidebar,
                    command=self.controller.quit,
                    textvariable=textvar
                )
            elif itype in ["switch_page"]:
                element = Button(
                    self.sidebar,
                    command=lambda target=item.get("target"): self.controller.show_frame(target, True),
                    textvariable=textvar
                )
            elif itype in ["switch_content"]:
                element = Button(
                    self.sidebar,
                    command=lambda target=item.get("target"): self.change_content(target),
                    textvariable=textvar
                )
            elif itype == "language_switcher":
                element = Combobox(
                    self.sidebar,
                    textvariable=textvar
                )
                self.controller.language_switcher_path = self.nametowidget(element)
                val = textvar if type(textvar) == str else textvar.get()
                element.set(val)
                element['values'] = self.controller.get_language_dropdown_options()
                element.bind('<<ComboboxSelected>>', self.controller.handle_language_dropdown)
            else:
                element = tk.Label(
                    self.sidebar,
                    textvariable=textvar
                )
            element.grid(row=i, column=0, sticky=tk.EW, padx=5)

    def init_sidebar(self):
        self.sidebar = BaseFrame(self, self, name="sidebar_menu")
        if self.controller.DISPLAY_FRAME_COLORED:
            self.sidebar.configure(bg='green')
        self.sidebar.grid(row=0, column=0, sticky=tk.NS, padx=5, pady=5)

    def set_headline(self, frame, text, wrapsize=0) -> tk.Label:
        label = tk.Label(
            frame,
            anchor=tk.NW,
            textvariable=text,
            wraplength=wrapsize,
            justify=tk.LEFT
        )
        label.config(font=self.controller.LARGE_FONT)
        label.pack(side=tk.TOP, anchor=tk.NW)
        label.bind('<Configure>', lambda e: label.config(wraplength=label.winfo_width()))
        return label

    def set_newline(self, frame, num_lines=1) -> tk.Label:
        label = tk.Label(
            frame,
            text="".join(["\n" for i in range(num_lines)]),
            anchor=tk.NW,
        )
        label.pack(side=tk.TOP, anchor=tk.NW)
        return label

    def set_paragraph(self, frame, text, wrapsize=0) -> tk.Label:
        label = tk.Label(
            frame,
            anchor=tk.NW,
            wraplength=wrapsize,
            justify=tk.LEFT
        )
        if type(text) is tk.StringVar:
            label.configure(textvariable=text)
        else:
            label.configure(text=text)
        label.config(font=self.controller.MEDIUM_FONT)
        label.bind('<Configure>', lambda e: label.config(wraplength=label.winfo_width()))
        label.pack(side=tk.TOP, anchor=tk.NW)
        return label

    def horizontal_seperator(self, frame):
        sep = Separator(frame, orient='horizontal')
        sep.pack(fill='x')


class ScrollBaseFrame(BaseFrame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.

    maybe make usage of pack/grids configurable
    so far only pack is used because of a lot of labels
    later when interactions are needed for the content, i may want to plaace UI elements in a grid
    """

    def __init__(self, parent):
        super(ScrollBaseFrame, self).__init__(parent)
        self.add_scrollbar(parent)

    def add_scrollbar(self, parent):
        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set)
        if self.controller.DISPLAY_CANVAS_COLORED:
            canvas.configure(bg='cyan')
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = tk.Frame(canvas)
        if self.controller.DISPLAY_FRAME_COLORED:
            self.interior.configure(background="red")
        self.interior.pack(anchor=tk.NW, fill=tk.BOTH)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())

            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        def _bound_to_mousewheel(event):
            # skip scrollbarbehavior if the window height exceeds the required interior space
            if parent.winfo_height() > interior.winfo_reqheight():
                return None
            canvas.bind_all("<MouseWheel>", _on_mousewheel)
            canvas.bind_all("<Button-4>", _on_mousewheel)
            canvas.bind_all("<Button-5>", _on_mousewheel)

        def _unbound_to_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")
            canvas.unbind_all("<Button-4>")
            canvas.unbind_all("<Button-5>")

        def _on_mousewheel(event):
            if self.controller.platform == 'darwin':  # for OS X # also, if platform.system() == 'Darwin':
                delta = event.delta
            else:  # for Windows, Linux
                delta = event.delta // 120
            canvas.yview_scroll(int(-1 * delta), "units")

        canvas.bind('<Configure>', _configure_canvas)
        canvas.bind('<Enter>', _bound_to_mousewheel)
        canvas.bind('<Leave>', _unbound_to_mousewheel)


class PageBaseFrame(BaseFrame):
    def __init__(self, parent, PageData):
        super(PageBaseFrame, self).__init__(parent)
        self.config = PageData.get("config")
        self.menu = PageData.get("menu")
        self.toc = PageData.get("TOC")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=50)
        self.build_menu(self.get_menu_items())
        self.set_default_content()
        self.change_content(self.default_page)
