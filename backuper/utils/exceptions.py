class BackuperError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class BackuperConfigError(BackuperError):
    pass

class BackuperNoSnapshotMatchError(BackuperError):
    pass