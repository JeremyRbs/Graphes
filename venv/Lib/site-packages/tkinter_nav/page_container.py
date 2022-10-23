from tkinter import Frame


class Container(Frame):
    """Root frame"""

    def __init__(self, root):
        Frame.__init__(self)

        self.pack(side='top', fill='both', expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.__root = root

    @property
    def root(self):
        """Instance of Wrapper(Tk)"""
        return self.__root
