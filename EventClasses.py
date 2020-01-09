import numpy as np

class DrsoscBoard(object):
    def __init__(self, board_serial):
        self.board_id = unpack(b'H', board_serial)[0];


    @property
    def trigger_cell(self):
        return self._trigger_cell

    @trigger_cell.setter
    def trigger_cell(self, value):
        self._trigger_cell = value;

    def __eq__(self, other):
        return self.board_id == other.board_id
    def __repr__(self):
        return str(self.board_id)
    # def __array__(self):
    #     return self.

class DrsoscChannel(object):
    def __init__(self):
        self.boards = np.array()

class DrsoscEventStream(object):
    def __init__(self, board, channel_id, timebins):
        self.board = board
        self.channel_id = int(channel_id)
        self.events = []
        self.timebins = timebins

    # def __array__(self):
    #     return self.events

    def __repr__(self):
        return """
Event Stream:
 - Board: {}
 - Channel: {}
 - Events: {}
 - Timebins: {}
""".format(self.board, self.channel_id, self.events, self.timebins)

class DrsoscEvent(object):
    def __init__(self):
        self.time = np.zeros(1024, dtype=np.float32)
        self.waveform = np.zeros(1024, dtype=np.float32)
