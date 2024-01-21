from iop import Quest


class Photos:
    pass


class Notes:
    progress = 0

    def __init__(self):
        self.quest = Quest()

    def next_note(self):
        self.progress += 1
        if self.progress == 10:
            self.progress = 0
        return self.quest.get_file(12)[self.progress]
