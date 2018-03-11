JMP @_start             ; jump to entry point

_start: ADD R0, 0x1     ; add 1 to R0
        ST 0xff, R0     ; write R0 contents to PPI data port
        JMP @_start     ; go back to start
        HLT             ; halt the cpu should not reach here
