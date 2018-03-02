# B0
B0 = 0x1

# The controlled signals
# TM - Timing Module
HLT_EN = B0

# IDR - Instruction Decoder Register
IDR_LD = B0 << 1
# IDR_OE = B0 << 2

# IP - Instruction Pointer
IP_LD = B0 << 2
IP_OE = B0 << 3
IP_INC = B0 << 4

# MAR - Memory Address Register
MAR_LD = B0 << 5
MAR_OE = B0 << 6

# REG - Registers
R0_LD = B0 << 7
R0_OE = B0 << 8
R1_LD = B0 << 9
R1_OE = B0 << 10
R2_LD = B0 << 11
R2_OE = B0 << 12
R3_LD = B0 << 13
R3_OE = B0 << 14

# ALU - Arithmatic and Logic Unit
AR0_LD = B0 << 15
AR1_LD = B0 << 16
ALU_AS_OE = B0 << 17
F_SEL_A0 = B0 << 18

# RST - Reset Logic
MR = B0 << 19
T_ST_MR = B0 << 20

# External Control Signals
RD = B0 << 21
WR = B0 << 22
ALE = B0 << 23

# The Instructions and related microcode with T-states
NULL = [0]
# Fetch Cycle - Common for all instructions
FC_T0 = IP_OE | ALE
FC_T1 = RD | IDR_LD | IP_INC
FC = [FC_T0, 0, FC_T1]
# FC = [FC_T0, FC_T1]
# NOP - No Operation - OPC = 00
NOP = FC + [0, T_ST_MR]
# HLT - HALT - OPC = 01
HLT = FC + [HLT_EN]
# MOV - Register Transfers
# MOV R0, R1 - copy data from R1 to R0 - OPC = 02
MOV_R0_R1_T2 = R0_LD | R1_OE
MOV_R0_R1_T3 = T_ST_MR
MOV_R0_R1 = FC + [MOV_R0_R1_T2, MOV_R0_R1_T3]
# MOV R0, R2 - copy data from R2 to R0 - OPC = 03
MOV_R0_R2_T2 = R0_LD | R2_OE
MOV_R0_R2_T3 = T_ST_MR
MOV_R0_R2 = FC + [MOV_R0_R2_T2, MOV_R0_R2_T3]
# MOV R0, R3 - copy data from R3 to R0 - OPC = 04
MOV_R0_R3_T2 = R0_LD | R3_OE
MOV_R0_R3_T3 = T_ST_MR
MOV_R0_R3 = FC + [MOV_R0_R3_T2, MOV_R0_R3_T3]
# MOV R1, R0 - copy data from R0 to R1 - OPC = 05
MOV_R1_R0_T2 = R1_LD | R0_OE
MOV_R1_R0_T3 = T_ST_MR
MOV_R1_R0 = FC + [MOV_R1_R0_T2, MOV_R1_R0_T3]
# MOV R1, R2 - copy data from R2 to R1 - OPC = 06
MOV_R1_R2_T2 = R1_LD | R2_OE
MOV_R1_R2_T3 = T_ST_MR
MOV_R1_R2 = FC + [MOV_R1_R2_T2, MOV_R1_R2_T3]
# MOV R1, R3 - copy data from R3 to R1 - OPC = 07
MOV_R1_R3_T2 = R1_LD | R2_OE
MOV_R1_R3_T3 = T_ST_MR
MOV_R1_R3 = FC + [MOV_R1_R3_T2, MOV_R1_R3_T3]
# MOV R2, R0 - copy data from R0 to R2 - 0PC = 08
MOV_R2_R0_T2 = R2_LD | R0_OE
MOV_R2_R0_T3 = T_ST_MR
MOV_R2_R0 = FC + [MOV_R2_R0_T2, MOV_R2_R0_T3]
# MOV R2, R1 - copy data from R1 to R2 - 0PC = 09
MOV_R2_R1_T2 = R2_LD | R1_OE
MOV_R2_R1_T3 = T_ST_MR
MOV_R2_R1 = FC + [MOV_R2_R1_T2, MOV_R2_R1_T3]
# MOV R2, R3 - copy data from R3 to R2 - OPC = 0A
MOV_R2_R3_T2 = R2_LD | R3_OE
MOV_R2_R3_T3 = T_ST_MR
MOV_R2_R3 = FC + [MOV_R2_R3_T2, MOV_R2_R3_T3]
# MOV R3, R0 - copy data from R0 to R3 - OPC = 0B
MOV_R3_R0_T2 = R3_LD | R0_OE
MOV_R3_R0_T3 = T_ST_MR
MOV_R3_R0 = FC + [MOV_R3_R0_T2, MOV_R3_R0_T3]
# MOV R3, R1 - copy data from R1 to R3 - OPC = 0C
MOV_R3_R1_T2 = R3_LD | R1_OE
MOV_R3_R1_T3 = T_ST_MR
MOV_R3_R1 = FC + [MOV_R3_R1_T2, MOV_R3_R1_T3]
# MOV R3, R2 - copy data from R2 to R3 - OPC = 0D
MOV_R3_R2_T2 = R3_LD | R2_OE
MOV_R3_R2_T3 = T_ST_MR
MOV_R3_R2 = FC + [MOV_R3_R2_T2, MOV_R3_R2_T3]
# MOV R0, ## - copy ## to R0 - OPC = 0E
MOV_R0_B_T2 = IP_OE | ALE | IP_INC
MOV_R0_B_T3 = R0_LD | RD
MOV_R0_B_T4 = T_ST_MR
MOV_R0_B = FC + [MOV_R0_B_T2, 0, MOV_R0_B_T3, MOV_R0_B_T4]
# MOV R1, ## - copy ## to R1 - OPC = 0F
MOV_R1_B_T2 = IP_OE | ALE | IP_INC
MOV_R1_B_T3 = R1_LD | RD
MOV_R1_B_T4 = T_ST_MR
MOV_R1_B = FC + [MOV_R1_B_T2, 0, MOV_R1_B_T3, MOV_R1_B_T4]
# MOV R2, ## - copy ## to R2 - OPC = 10
MOV_R2_B_T2 = IP_OE | ALE | IP_INC
MOV_R2_B_T3 = R2_LD | RD
MOV_R2_B_T4 = T_ST_MR
MOV_R2_B = FC + [MOV_R2_B_T2, 0, MOV_R2_B_T3, MOV_R2_B_T4]
# MOV R2, ## - copy ## to R2 - OPC = 10
MOV_R3_B_T2 = IP_OE | ALE | IP_INC
MOV_R3_B_T3 = R3_LD | RD
MOV_R3_B_T4 = T_ST_MR
MOV_R3_B = FC + [MOV_R3_B_T2, 0, MOV_R3_B_T3, MOV_R3_B_T4]
# MEM to REG transfers
# LD R0, ## - Load R0 with contents of location ##
LD_R0_B_T2 = IP_OE | ALE | IP_INC
LD_R0_B_T3 = RD | ALE
LD_R0_B_T4 = R0_LD | RD
LD_R0_B_T5 = T_ST_MR
LD_R0_B = FC + [LD_R0_B_T2, 0, LD_R0_B_T3, 0, LD_R0_B_T4, LD_R0_B_T5]
# LD R1, ## - Load R1 with contents of location ##
LD_R1_B_T2 = IP_OE | ALE | IP_INC
LD_R1_B_T3 = RD | ALE
LD_R1_B_T4 = R1_LD | RD
LD_R1_B_T5 = T_ST_MR
LD_R1_B = FC + [LD_R1_B_T2, 0, LD_R1_B_T3, 0, LD_R1_B_T4, LD_R1_B_T5]
# LD R2, ## - Load R2 with contents of location ##
LD_R2_B_T2 = IP_OE | ALE | IP_INC
LD_R2_B_T3 = RD | ALE
LD_R2_B_T4 = R2_LD | RD
LD_R2_B_T5 = T_ST_MR
LD_R2_B = FC + [LD_R2_B_T2, 0, LD_R2_B_T3, 0, LD_R2_B_T4, LD_R2_B_T5]
# LD R3, ## - Load R3 with contents of location ##
LD_R3_B_T2 = IP_OE | ALE | IP_INC
LD_R3_B_T3 = RD | ALE
LD_R3_B_T4 = R3_LD | RD
LD_R3_B_T5 = T_ST_MR
LD_R3_B = FC + [LD_R3_B_T2, 0, LD_R3_B_T3, 0, LD_R3_B_T4, LD_R3_B_T5]
# REG to MEM transfers
# ST ##, R0 - Store contents of R0 to location ##
ST_B_R0_T2 = IP_OE | ALE | IP_INC
ST_B_R0_T3 = RD | ALE
ST_B_R0_T4 = R0_OE | WR
ST_B_R0_T5 = T_ST_MR
ST_B_R0 = FC + [ST_B_R0_T2, 0, ST_B_R0_T3, ST_B_R0_T4, ST_B_R0_T5]
# ST ##, R1 - Store contents of R1 to location ##
ST_B_R1_T2 = IP_OE | ALE | IP_INC
ST_B_R1_T3 = RD | ALE
ST_B_R1_T4 = R1_OE | WR
ST_B_R1_T5 = T_ST_MR
ST_B_R1 = FC + [ST_B_R1_T2, 0, ST_B_R1_T3, ST_B_R1_T4, ST_B_R1_T5]
# ST ##, R2 - Store contents of R2 to location ##
ST_B_R2_T2 = IP_OE | ALE | IP_INC
ST_B_R2_T3 = RD | ALE
ST_B_R2_T4 = R2_OE | WR
ST_B_R2_T5 = T_ST_MR
ST_B_R2 = FC + [ST_B_R2_T2, 0, ST_B_R2_T3, ST_B_R2_T4, ST_B_R2_T5]
# ST ##, R3 - Store contents of R3 to location ##
ST_B_R3_T2 = IP_OE | ALE | IP_INC
ST_B_R3_T3 = RD | ALE
ST_B_R3_T4 = R3_OE | WR
ST_B_R3_T5 = T_ST_MR
ST_B_R3 = FC + [ST_B_R3_T2, 0, ST_B_R3_T3, ST_B_R3_T4, ST_B_R3_T5]

# ROM file header
HEADER = 'v2.0 raw'
# ROM instruction contents
MC_V1 = [NOP, HLT,
         MOV_R0_R1, MOV_R0_R2, MOV_R0_R3,
         MOV_R1_R0, MOV_R1_R2, MOV_R1_R3,
         MOV_R2_R0, MOV_R2_R1, MOV_R2_R3,
         MOV_R3_R0, MOV_R3_R1, MOV_R3_R2,
         MOV_R0_B, MOV_R1_B, MOV_R2_B, MOV_R3_B,
         LD_R0_B, LD_R1_B, LD_R2_B, LD_R3_B,
         ST_B_R0, ST_B_R1, ST_B_R2, ST_B_R3]


def generate_rom(micro_code = MC_V1):
	rom = HEADER + '\n'
	for instr in micro_code:
		for micro_instr in instr:
			rom += hex(micro_instr)[2:] + ' '
		rom += str(0x10 - len(instr)) + '*0' + '\n'
	return rom


def main():
	with open('micro_code.rom', 'w') as f:
		print(generate_rom(), file = f)


if __name__ == '__main__':
	main()
