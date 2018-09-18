JMP @_start             ; Jump to the entry point

_start: MOV R0, 0xaf    ; should load 0xaf into R0
        HLT             ; Halt the cpu
