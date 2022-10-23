class EmptyPageListError(Exception):
    """Raised when the page list is empty"""

    def __init__(self):
        self.msg = 'Page list must not be empty'

    def __str__(self):
        return repr(self.msg)


class PageNotFoundError(Exception):
    """Raised when a page is not found"""

    def __init__(self):
        self.msg = 'No page with that name was found'

    def __str__(self):
        return repr(self.msg)
