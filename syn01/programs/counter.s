JMP @_start

_start: ADD R0, 0x1
        ST 0xff, R0
        JMP @_start
        HLT