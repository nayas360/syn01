#!/usr/bin/env python3
# this generates rom code for cpu logic
from ruamel.yaml import YAML as yaml


# tries to generate code for cpu logic rom for given yml configuration
class RomMicroCodeGenerator:
    RAW_HEADER = 'v2.0 raw'
    CPU_VER = 'cpu_version'
    ROM_ADDR_W = 'rom_address_width'
    ROM_D_W = 'rom_data_width'
    MAX_TS = 'max_tstates'
    MCI = 'micro_instruction'
    FCD = 'fetch_cycle_def'
    OPD = 'opcode_def'
    OPD_ALIAS = 'alias'
    OPD_DEF = 'def'

    def __init__(self, config_file):
        self.config_file = config_file
        # try loading the configuration from the file
        with open(config_file) as f:
            yaml_decoder = yaml()
            self.config = yaml_decoder.load(f)
        self.cpu_version = self.config[self.CPU_VER]
        self.rom_addr_w = self.config[self.ROM_ADDR_W]
        self.rom_d_w = self.config[self.ROM_D_W]
        self.max_ts = self.config[self.MAX_TS]
        self.micro_code_sym_def = self.config[self.MCI]
        # generate a control code for each of the microcode instructions
        self.mci_ctrlc_map = {}
        for i in range(len(self.micro_code_sym_def)):
            self.mci_ctrlc_map[self.micro_code_sym_def[i]] = 0x1 << i  # (i % (self.rom_d_w - 1))
            if self.mci_ctrlc_map[self.micro_code_sym_def[i]] > (pow(2, self.rom_d_w) - 1):
                self.mci_ctrlc_map[self.micro_code_sym_def[i]] = self.mci_ctrlc_map[
                                                                     self.micro_code_sym_def[i]] >> (
                                                                         self.rom_d_w * self._rom_bank_num(
                                                                     self.micro_code_sym_def[i]))
        # self.mci_ctrlc_map['T_W'] = 0
        # prepare the rom banks
        max_rom_banks = ((len(self.micro_code_sym_def) - 1) // self.rom_d_w)
        self.rom_banks = [[] for i in range(max_rom_banks + 1)]
        # load the fetch cycle
        self.fc = self.config[self.FCD]
        # load the opcodes
        self.opcodes = self.config[self.OPD]
        # load opcodes to rom banks
        for op in self.opcodes:
            for i in self.fc:
                self._add_mci(i)
            for i in op[self.OPD_DEF]:
                self._add_mci(i)
            for i in range(len(self.rom_banks)):
                self.rom_banks[i].append(str(self.max_ts - (len(self.fc) + len(op[self.OPD_DEF]))) + '*0' + '\n')

    # generates the rom from the generated rom banks
    def generate(self, prefix=''):
        if prefix == '':
            prefix = self.cpu_version
        for i in range(len(self.rom_banks)):
            with open(prefix + '_' + str(i) + '.rom', 'w') as f:
                s = '\n'.join([i.strip() for i in ' '.join(self.rom_banks[i]).split('\n')])[:-1]
                print(self.RAW_HEADER, s, sep='\n', end='', file=f)

    # properly formats and adds microcode instructions to the available rom banks
    def _add_mci(self, mci):
        for i in range(len(self.rom_banks)):
            self.rom_banks[i].append('0')
        if 'T_W' in mci:
            return
        for i in mci.split('|'):
            i = i.strip()
            self.rom_banks[self._rom_bank_num(i)][-1] = hex((int(self.rom_banks[self._rom_bank_num(i)][-1], 16) | \
                                                             self.mci_ctrlc_map[i]))[2:]

    # returns corresponding rom bank number for given micro instruction
    def _rom_bank_num(self, mci):
        return self.micro_code_sym_def.index(mci) // self.rom_d_w


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        prog='mcgen',
        # usage='micro_code_gen mcg_configuration_file.yml',
        description='Generate microcode rom file(s) based on given configuration'
    )
    parser.add_argument('filename', type=str,
                        help='the configuration filename')
    parser.add_argument('-o', '--prefix', type=str, default='',
                        help='set the rom filename prefix')
    args = parser.parse_args()
    rmcg = RomMicroCodeGenerator(args.filename)
    rmcg.generate(args.prefix)
