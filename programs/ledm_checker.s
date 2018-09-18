JMP @_start                 ; Jump to start

_start: MOV R0, 0xf6        ; store starting address of first PPI to R0
        ST 0xfe, R0         ; store the address to control register of first PPI
        MOV R0, 0xfa        ; store starting address of second PPI to R0
        ST 0xff, R0         ; store the address to control register of second PPI
        MOV R0, 0x55
        MOV R1, 0xaa
        ST 0xf6, R0
        ST 0xf7, R1
        ST 0xf8, R0
        ST 0xf9, R1
        ST 0xfa, R0
        ST 0xfb, R1
        ST 0xfc, R0
        ST 0xfd, R1
        HLT
