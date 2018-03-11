#!/usr/bin/env python3
# a very simple assembler to generate raw bin file
import re

import rply
from ruamel.yaml import YAML as yaml


class Assembler:
    RAW_HEADER = 'v2.0 raw'
    CPU_VER = 'cpu_version'
    RAM_ADDR_W = 'ram_address_width'
    RAM_D_W = 'ram_data_width'
    OPD = "opcode_def"
    ALIAS = "alias"
    NUM_ARG = "num_args"
    IS_ARG = "is_arg"
    AS_REGEX = "as_regex"
    AS_G_TRANSFORMS = "as_global_transforms"

    LABEL_DEF_CHAR = ':'
    LABEL_USE_CHAR = '@'

    def __init__(self, configfile):
        self.configfile = configfile
        with open(configfile) as f:
            yaml_decoder = yaml()
            self.config = yaml_decoder.load(f)
        self.cpu_version = self.config[self.CPU_VER]
        self.ram_addr_w = self.config[self.RAM_ADDR_W]
        self.ram_d_w = self.config[self.RAM_D_W]
        self.opcodes = self.config[self.OPD]
        self.as_g_tr = self.config[self.AS_G_TRANSFORMS]
        # self.asm = rply.LexerGenerator()
        # # ignore comments
        # self.asm.ignore(";(.+)?\n")
        # # ignore white spaces
        # self.asm.ignore("\s+")
        self.aliases = [op[self.ALIAS] for op in self.opcodes]
        self.num_args = [op[self.NUM_ARG] for op in self.opcodes]
        self.is_args = self.config[self.IS_ARG]
        # self.label_addr_map = {}
        self.ram = []
        # self._process_opcodes()

    # makes a regex
    # def _process_opcodes(self):
    #     """sets up the lexer generator to work with opcodes"""
    #     for op in self.opcodes:
    #         asr = op[self.AS_REGEX]
    #         for tr in self.as_g_tr:
    #             asr = asr.replace(tr, self.as_g_tr[tr])
    #         self.asm.add(op[self.ALIAS], asr)
    #         self.aliases.append(op[self.ALIAS])

    def _pass1(self, source):
        """calculates label addresses and removes labels from source"""
        LabelLexer = rply.LexerGenerator()
        LabelLexer.add("LABEL_DEF", "[_A-Za-z][_A-Za-z0-9]+" + self.LABEL_DEF_CHAR)
        LabelLexer.add("LABEL_USE", self.LABEL_USE_CHAR + "[_A-Za-z][_A-Za-z0-9]+")
        LabelLexer.ignore(";(.+)?\n")
        LabelLexer.ignore("\s+")
        for op in self.opcodes:
            asr = op[self.AS_REGEX]
            for arg in self.is_args:
                if arg in asr:
                    LabelLexer.add(op[self.ALIAS] + "_ARG_REM", asr.replace(arg, ""))
            for tr in self.as_g_tr:
                asr = asr.replace(tr, self.as_g_tr[tr])
            LabelLexer.add(op[self.ALIAS], asr)

        cur_addr = 0
        for tok in LabelLexer.build().lex(source):
            if tok.name == 'LABEL_DEF':
                source = source.replace(self.LABEL_USE_CHAR + tok.value[:-1], hex(cur_addr))
                source = source.replace(tok.value, '')
            elif tok.name == 'LABEL_USE':
                continue
            elif '_ARG_REM' in tok.name:
                cur_addr += self.num_args[self.aliases.index(tok.name.replace('_ARG_REM', ''))] + 1
            else:
                cur_addr += self.num_args[self.aliases.index(tok.name)] + 1

        return source

    def _pass2(self, source):
        """removes labels from source"""
        ArgLexer = rply.LexerGenerator()
        ArgLexer.ignore(";(.+)?\n")
        ArgLexer.ignore("\s+")
        recargs = []
        for tr in self.as_g_tr:
            if tr in self.is_args:
                recargs.append(re.compile(self.as_g_tr[tr]))
        for op in self.opcodes:
            asr = op[self.AS_REGEX]
            for tr in self.as_g_tr:
                asr = asr.replace(tr, self.as_g_tr[tr])
            ArgLexer.add(op[self.ALIAS], asr)

        for tok in ArgLexer.build().lex(source):
            narg = self.num_args[self.aliases.index(tok.name)]
            self.ram.append(hex(self.aliases.index(tok.name))[2:])
            if narg:
                for arg in recargs:
                    m = arg.findall(tok.value)
                    if m:
                        self.ram.append(m[0][2:])

    def generate(self, source, prefix=''):
        with open(source) as f:
            source = ''.join(f.readlines())

        source = self._pass1(source)
        # print(source)
        self._pass2(source)
        # print(self.ram)

        if prefix == '':
            prefix = source + '.hex'
        with open(prefix, 'w') as f:
            print(self.RAW_HEADER, file=f)
            for i in range(len(self.ram)):
                print(self.ram[i], end=' ', file=f)
                # if i % 10 != 0:
                #     print(file=f)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        prog='assemble',
        description='Generate compiled hex file from given assembly source code and processor configuration'
    )
    parser.add_argument('config', type=str,
                        help='the processor configuration filename')
    parser.add_argument('source', type=str,
                        help='the assembly file to be compiled')
    parser.add_argument('-o', '--prefix', type=str, default='',
                        help='set the hex filename prefix')
    args = parser.parse_args()

    a = Assembler(args.config)
    a.generate(args.source, args.prefix)
