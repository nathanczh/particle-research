#!/usr/bin/env python
"""
Script to convert binary format to root for DRS4 evaluation boards.
http://www.psi.ch/drs/evaluation-board

Jonas Rembser (rembserj@phys.ethz.ch), 2016-04-15 based on work by
Gregor Kasieczka, ETHZ, 2014-01-15
based on decode.C by Dmitry Hits
"""

import numpy as np
from struct import unpack
from EventClasses import *


class DrsoscReader(object):
    """docstring for DrsoscReader."""

    def __init__(self, input_filename):
        self.file = open(input_filename, "rb")
        self.n_ch = 0
        self.n_boards = 0
        self.boards = []

        self.channels = []



    def read_headers(self):
        timebins = []
        current_board = None
        while True:
            header = self.file.read(4)
            # For skipping the initial time header
            if header == b"TIME":
                continue
            elif header.startswith(b"C"):
                print("Channel: ", header)
                self.channels.append(DrsoscEventStream(
                    board = current_board,
                    channel_id = header[1:],
                    timebins = np.array(unpack('f'*1024, self.file.read(4*1024)))
                ))

            # Increment the number of boards when seeing a new serial number
            # and store the serial numbers in the board serial numbers vector
            elif header.startswith(b"B#"):
                current_board = DrsoscBoard(header[2:])
                self.boards.append(current_board)

            # End the loop if header is not CXX or a serial number
            elif header == b"EHDR":
                break

    def read_body(self):
        current_board = None
        while True:
            header = self.file.read(4)
            if header.startswith(b"B#"): # Next Board
                current_board = self.boards[self.boards.index(DrsoscBoard(header[2:]))]
                current_board.trigger_cell = unpack(b'H', f.read(4)[2:])[0]
                continue
            elif header == b"EHDR":
                

    def read(self):
        self.read_headers()
        self.read_body()

    def get_data(self):
        return self.channels
