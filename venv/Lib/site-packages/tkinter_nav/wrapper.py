from tkinter import Tk

from .errors import EmptyPageListError, PageNotFoundError
from .page_container import Container


class Wrapper(Tk):
    """Tkinter-nav entry class"""

    def __init__(self, pages, start_state=None):
        Tk.__init__(self)

        self.app_state = start_state or {}

        self.__pages = {}
        self.__current_page = None
        self.__container = Container(self)
        self.__register_pages(pages)

    @property
    def pages(self):
        """Registered pages"""
        return self.__pages

    @property
    def current_page(self):
        """Current page"""
        return self.__current_page

    @property
    def container(self):
        """Root frame"""
        return self.__container

    def show_page(self, name):
        """Hides the current page and shows the given page

        :param name: Name of the page to be shown

        :raises PageNotFoundError: Raised when given page doesn't exist
        """
        page = self.__pages[name]
        if page:
            self.__handle_hide(page)

            page.page_did_mount()
            page.tkraise()
        else:
            raise PageNotFoundError()

    def __register_pages(self, pages):
        """Creates an instance of each page

        :param pages: List of pages to be registered

        :raises EmptyPageListError: Raised when the page list is empty
        """
        if len(pages) == 0:
            raise EmptyPageListError()

        for P in pages:
            page = P(parent=self.container)
            name = page.name or page.__name__
            self.__pages[name] = page

    def __handle_hide(self, new_page):
        """Takes care of changing the page state

        :param new_page: The page to be shown
        """
        if self.current_page:
            self.current_page.update_state()
            self.current_page.page_did_unmount()

        self.__current_page = new_page
