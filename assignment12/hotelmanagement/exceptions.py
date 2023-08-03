# exceptions.py
class GuestNotFoundException(Exception):
    pass

class GuestAlreadyCheckedInException(Exception):
    pass

class GuestNotCheckedInException(Exception):
    pass
