## SYN_01 ISA

This file contains the exhaustive list of instructions
supported by this processor. The format is as follows:

```
HEX CODE - INSTRUCTION FORMAT
```
NOTE: `B` stands for a byte data

00 - NOP  
01 - HLT  
02 - MOV R0, R1  
03 - MOV R0, R2  
04 - MOV R0, R3  
05 - MOV R1, R0  
06 - MOV R1, R2  
07 - MOV R1, R3  
08 - MOV R2, R0  
09 - MOV R2, R1  
0A - MOV R2, R3  
0B - MOV R3, R0  
0C - MOV R3, R1  
0D - MOV R3, R2  
0E - MOV R0, B  
0F - MOV R1, B  
10 - MOV R2, B  
11 - MOV R3, B  
12 - LD R0, B  
13 - LD R1, B  
14 - LD R2, B  
15 - LD R3, B  
16 - ST B, R0  
17 - ST B, R1  
18 - ST B, R2  
19 - ST B, R3  
1A - JMP B  
1B - ADD R0, B  
1C - ADD R1, B  
1D - ADD R2, B  
1E - ADD R3, B  
