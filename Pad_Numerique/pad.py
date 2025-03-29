from random import randint, sample

import customtkinter as ctk

import tkinter as tk

from pathlib import Path

import os


ROOT_PATH: Path = Path(os.path.dirname(__file__))
PICTURES_PATH: Path = ROOT_PATH / Path(r".\Pictures")

# imported from https://thenounproject.com/icon/code-5946023 & https://thenounproject.com/icon/lock-7697321
DEFAULT_ICON_PATH: Path = ROOT_PATH / PICTURES_PATH / "pad_bank_picture.ico"


class Pad(ctk.CTk):
    def __init__(
            self,

            name: str = 'Pad',
            resize: bool = False,
            dimension: tuple[int, int] = (500, 600),
            background: str | tuple[str, str] = 'royalblue',
            icon: Path = DEFAULT_ICON_PATH,

            *args, **kwargs
        ):
        r"""A subclass of a base custom tkinter class, to basically implement a touch pad,
        like you can see in mobile bank application for phone. The aim of this pad is to find
        the good code : if the number that you click is the same of the secret code, it
        will become highlight in green, else in red. You can use a 'suppr' touch to erase
        some numbers of the 4 numbers code.

        Args:
            name (str, optional): The main name of the pad application. Defaults to 'Pad'.
            resize (bool, optional): If you want to change the size of the pad window or not. Defaults to False.
            dimension (tuple[int, int], optional): The length and the width of the pad window. Defaults to (500, 600).
            background (str | tuple[str, str], optional): Th colour of the background of the pad window. Defaults to 'royalblue'.
            icon (Path, optional): A path to change the default icon of the window. Defaults to '.\Pictures\pad_bank_picture.ico'.
        """

        super().__init__(*args, **kwargs)

        self.name = name
        self.icon = icon
        self.resize = resize
        self.dimension = dimension
        self.background = background

        self.secret_code: str = "".join([
            str(randint(0, 9)) for _ in range(4)
        ])

        self.numbers_pad: list[str] = sample(
            [str(number) for number in range(10)], 10
        )

        self.number_of_click: int = 0
        self.taped_code: list[str] = ['*'] * 4

        print(f"The secret code is : {self.secret_code}")

        self.title(self.name)
        self.iconbitmap(self.icon)
        self.config(background=self.background)
        self.resizable(self.resize, self.resize)
        self.geometry(f"{self.dimension[0]}x{self.dimension[1]}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # The configuration of the code label
        self.info_frame: ctk.CTkFrame = ctk.CTkFrame(self, corner_radius=40)
        self.info_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.25)

        for i, relx in enumerate([0.1, 0.31, 0.51, 0.7]):
            exec(
                f"self.code_label_{i}: ctk.CTkLabel = ctk.CTkLabel(self.info_frame, text=self.taped_code[{i}], font=ctk.CTkFont('arial', 60))\n" + 
                f"self.code_label_{i}.place(relx={relx}, rely=0.15, relwidth=0.2, relheight=0.7)"
            )

        # The configuration of the keypad
        self.pad_frame: ctk.CTkFrame = ctk.CTkFrame(self, corner_radius=40)
        self.pad_frame.place(relx=0.05, rely=0.40, relwidth=0.9, relheight=0.55)

        for i, relx in enumerate([0.05, 0.35, 0.65]):
            exec(
                f"self.pad_frame_{i}: ctk.CTkFrame = ctk.CTkFrame(self.pad_frame, corner_radius=10)\n" +
                f"self.pad_frame_{i}.place(relx={relx}, rely=0.05, relwidth=0.3, relheight=0.9)"
            )

        # The configuration of boutons on the defined column of the keypad
        for i, (column, rely) in enumerate(
                zip([0, 1, 2] * 3 + [1], [0.05] * 3 + [0.28] * 3 + [0.52] * 3 + [0.75])
            ):

            exec(
                f"self.button_{i}: ctk.CTkButton = ctk.CTkButton(self.pad_frame_{column}, text=self.numbers_pad[{i}], command=lambda: self.on_clicking(self.numbers_pad[{i}]), corner_radius=30, font=ctk.CTkFont('arial', 30))\n" +
                f"self.button_{i}.place(relx=0.05, rely={rely}, relwidth=0.9, relheight=0.2)",

                {'self':self, 'ctk':ctk}
            )

        self.button_backspace = ctk.CTkButton(self.pad_frame_2, text='suppr', command=self.suppr, corner_radius=30, font=ctk.CTkFont("arial", 20, 'bold'))
        self.button_backspace.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.2)

        # To apply the main background color for each surface
        for child in self.children.values():
            child.configure(bg_color=(self.background, self.background))

    def suppr(self):
        """A function call to delete numbers show in the label part of the window."""
        self.number_of_click = (self.number_of_click - 1) % 4
        eval(f"self.code_label_{self.number_of_click}.configure(text='*', text_color='white')")

    def on_closing(self):
        """A function call to ask before the destroy of the window if you want to destroy it."""
        if tk.messagebox.askyesno(title='Quit ?', message="Do you really want to quit ?"):
            self.destroy()

    def on_clicking(self, number: str):
        """A function call when you click in a button of the numeric pad.

        Args:
            number (str): The associated numbers of the button, greater or equal to 0, and lower or equal than 9.
        """
        self.taped_code[self.number_of_click] = number

        check_color = 'green' if self.taped_code[self.number_of_click] == self.secret_code[self.number_of_click] else 'red'
        eval(f"self.code_label_{self.number_of_click}.configure(text=self.taped_code[{self.number_of_click}], text_color='{check_color}')")

        self.number_of_click = (self.number_of_click + 1) % 4

        if " ".join(self.taped_code).replace(' ', '') == self.secret_code:
            tk.messagebox.showinfo(title='And the winner is ...', message=f"You won ! The secret code was {self.secret_code}.")

            self.destroy()

if __name__ == '__main__':
    pad = Pad(
        name="Pad Bank",
        dimension=(500, 600),
        background='royalblue',
        icon=DEFAULT_ICON_PATH,
        resize=True
    )

    pad.mainloop()
