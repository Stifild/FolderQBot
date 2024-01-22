from iop import IOP


class Photos:
    pass


class Notes:
    progress = 0

    def __init__(self):
        self.quest = IOP()

    def next_note(self):
        self.progress += 1
        if self.progress == 10:
            self.progress = 0
        return self.quest.get_file(12)[self.progress]
