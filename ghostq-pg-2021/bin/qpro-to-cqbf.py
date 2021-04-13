#!/usr/bin/python

##############################################################################
# qpro-to-cqbf.py: Converts from the QPRO format to the loose version of
#                  the GhostQ CQBF format.
# Author: Will Klieber
##############################################################################

import sys
import re
import pdb
import timeit

PrStage = True

sys.setrecursionlimit(10000)

################################################################################
# Utility functions
################################################################################

def die(text): 
    sys.stderr.write("\nERROR: " + text+"\n")
    if sys.argv[1] == '-':
        sys.exit(1)
    pdb.set_trace()

def qdie(text): 
    sys.stderr.write(text + "\n")
    sys.exit(1)

stop = pdb.set_trace
stderr = sys.stderr

timer = timeit.default_timer
start_time = timer()
elapsed_time = (lambda: timer() - start_time)

################################################################################

class LineReader:
    """Reads a file line-by-line."""
    def __init__(self, file):
        self.file = file
        self.cur = None
        self.line_num = 0
        self.IsEOF = False
        self.advance()
    def advance(self):
        self.cur = self.file.readline()
        self.line_num += 1
        if (self.cur == ""):
            self.IsEOF = True
        self.cur = self.cur.strip()
    def close(self):
        self.file.close()

def OpenInputFile(filename):
    filename = sys.argv[1]
    try:
        file_ptr = open(filename, 'r')  if filename != '-' else sys.stdin
    except IOError, e:
        sys.stderr.write(str(e)+"\n")
        sys.exit(1)
    return LineReader(file_ptr)

class ProbInst:
    def __init__(self):
        self.gates = {}
        self.QuantPfx = []

    def NewVar(self):
        self.NumVars += 1
        return self.NumVars

class Fmla:
    def __init__(self, typ):
        self.gtype = typ

    def __str__(self):
        return str(self.__dict__)

class QuantBlk:
    def __init__(self, qtype, qvars):
        self.qtype = qtype
        self.qvars = qvars

class QuantPrefix:
    def __init__(self, gate=0, blks=None):
        self.gate = gate
        if blks==None: blks = []
        self.blks = blks

def ReadQpro():
    prob = ProbInst()
    infile = OpenInputFile(glo.InFile)
    def LineDie(msg):
        stderr.write("Error on line %i. " % infile.line_num)
        stderr.write(msg + "\n")
        sys.exit(1)
    while (infile.cur.startswith("c")):
        infile.advance()
    if not infile.cur.startswith("QBF"): LineDie("Expecting 'QBF'.")
    CurLine = infile.cur.strip()
    if CurLine == "QBF":
        infile.advance()
        CurLine += " " + infile.cur.strip()
    CurLine = CurLine[4:]
    try:
        prob.NumVars = int(CurLine) + glo.VarOffset
        prob.LastInpVar = prob.NumVars
    except:
        LineDie("Expecting an integer, but found '%s'." % CurLine)
    infile.advance()

    def ReadSubfmla():
        infile.cur = infile.cur.strip().lower()
        if infile.cur == 'q': return ReadQb()
        elif infile.cur in ['c', 'd']: return ReadGate()
        else: LineDie("Expected 'c', 'd', or 'q', but found '%s'." % infile.cur)

    def ReadQb():
        assert(infile.cur == 'q');
        infile.advance()
        num_q = 1
        ret = QuantPrefix()
        ret.blks = []
        while 1:
            CurLine = infile.cur.strip()
            if CurLine == 'q':
                infile.advance()
                num_q += 1
                continue
            qtype = CurLine[0]
            if (qtype not in ['a','e']):
                break
            try:
                qvars = tuple([int(x) + glo.VarOffset for x in CurLine[2:].split()])
                qvars = tuple([x for x in qvars if (x not in glo.InterestVars)])
            except:
                LineDie("")
            ret.blks.append(QuantBlk(qtype, qvars))
            infile.advance()
        if (CurLine not in ['c','d']):
            LineDie("Expected one of ['a', 'e', 'c', 'd'], but found '%s'." % CurLine)
        ret.gate = ReadGate()
        while num_q > 0:
            if infile.cur != '/q':
                LineDie("Expected '/q'.")
            infile.advance()
            num_q -= 1
        prob.QuantPfx.append(ret)
        return ret.gate

    def ReadGate():
        assert(infile.cur in ['c', 'd']);
        GateType = infile.cur 
        ret = Fmla(GateType)
        infile.advance()
        args = []
        try:
            for sign in [1, -1]:
                args.extend([(int(x) + glo.VarOffset)*sign for x in infile.cur.split()])
                infile.advance()
        except:
            LineDie("")
        while 1:
            if infile.cur.startswith("/"):
                if (infile.cur != ("/" + GateType)):
                    LineDie("Expected '/%s'." % GateType)
                infile.advance()
                break
            args.append(ReadSubfmla())
        ret.args = args
        ret.gtype = {'c':'and', 'd':'or'}[ret.gtype]
        ret.GateNum = prob.NewVar()
        prob.gates[ret.GateNum] = ret
        return ret.GateNum

    prob.out = ReadSubfmla()
    if len(glo.InterestVars) > 0:
        free_blk = QuantBlk('f', list(sorted(glo.InterestVars)))
        outer_pfx = None
        for pfx in prob.QuantPfx:
            if pfx.gate == prob.out:
                outer_pfx = pfx
                break
        if outer_pfx == None:
            outer_pfx = QuantPrefix(prob.out)
            prob.QuantPfx.append(outer_pfx)
        outer_pfx.blks = [free_blk] + outer_pfx.blks
        prob.QuantPfx.append
    return prob

def WriteCqbf(prob):
    outf = glo.OutFile
    outf.write("CktQBF\n")
    outf.write("LastInputVar %i\n" % prob.LastInpVar)
    #outf.write("FirstGateVar %i\n" % 0)
    outf.write("LastGateVar %i\n" % prob.NumVars)
    outf.write("OutputGateLit %i\n" % prob.out)

    for quant in prob.QuantPfx:
        outf.write("<q gate=%i>\n" % quant.gate)
        for qb in quant.blks:
            outf.write("%s " % qb.qtype)
            outf.write(" ".join([str(x) for x in qb.qvars]) + "\n")
        outf.write("</q>\n")

    for (GateNum, gate) in reversed(prob.gates.items()):
        GateType = gate.gtype
        GateArgs = ", ".join([str(x) for x in gate.args])
        outf.write("%i = %s(%s)\n" % (GateNum, GateType, GateArgs))
        
class GloOpt:
    pass

def main():
    global glo
    glo = GloOpt()
    argv = sys.argv
    UsageMsg = "Usage: 'python %s InputFile -o OutputFile [options]'" % (sys.argv[0])
    if len(argv) < 2 or (sys.argv[1] in ["-h", "--help", "-help", "/h"]):
        if len(argv) < 2: print "No filename given!"
        print UsageMsg
        print "Note: Pass this script's output thru cqbf-conv.py before giving it to GhostQ."
        sys.exit(1)
    glo.InFile = sys.argv[1]
    glo.OutFile = sys.stdout
    glo.InterestFile = None
    glo.InterestOffset = None
    glo.InterestVars = set()
    glo.quiet = False
    i=2
    while (i < len(argv)):
        sArg = argv[i]
        if (False): pass
        elif sArg in ["-h", "--help", "-help"]:
            print UsageMsg
            sys.exit(0)
        elif sArg in ["-q", "--quiet"]:
            glo.quiet = True
        elif (i == len(argv)-1):
            qdie("Error: option '%s' is unrecognized or needs a parameter" % sArg)
        elif (sArg=='-interest'):
            i+=1
            glo.InterestFile = argv[i]
        elif (sArg=='-interest-offset'):
            i+=1
            glo.InterestOffset = int(argv[i])
            if not glo.InterestFile:
                glo.InterestFile = glo.InFile.replace(".qpro", ".interest")
        elif (sArg=='-o'):
            i+=1
            glo.OutFile = open(argv[i], 'w')
        else: qdie("Error: unrecognized option '%s'" % sArg)
        i += 1

    if glo.InterestFile:
        if glo.InterestOffset == None:
            qdie("Error: must specify '-interest-offset' option.")
        file = LineReader(open(glo.InterestFile, 'r'))
        if file.cur != "Variables of interest:":
            die("Bad interest file.")
        file.advance()
        while True:
            if file.IsEOF:
                die("Unexpected end of interest file.")
            var = int(file.cur)
            if var == -1:
                break
            #var -= glo.InterestOffset
            file.advance()
            glo.InterestVars.add(var)

    glo.VarOffset = 0
    if glo.InterestOffset != None:
        glo.VarOffset = glo.InterestOffset
    prob = ReadQpro()
    WriteCqbf(prob)
    if (not glo.quiet):
        sys.stderr.write("Done converting from QPRO, %.4f sec\n" % (elapsed_time()))

main()
