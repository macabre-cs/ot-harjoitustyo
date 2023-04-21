from tkinter import ttk, constants


class WelcomeView:
    def __init__(self, root, handle_show_login_view, handle_show_adopt_view):
        self._root = root
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_adopt_view = handle_show_adopt_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        welcome_label = ttk.Label(master=self._frame, text="Welcome back?")

        login_button = ttk.Button(
            master=self._frame, text="I already have a pet", command=self._handle_show_login_view)
        register_button = ttk.Button(
            master=self._frame, text="I don't have a pet yet", command=self._handle_show_adopt_view)

        welcome_label.grid(row=0, column=0, padx=10, pady=10)
        login_button.grid(row=1, column=0, padx=10, pady=10)
        register_button.grid(row=1, column=1, padx=10, pady=10)
