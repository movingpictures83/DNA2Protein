import PyPluMA

CODING_TABLE = dict()
CODING_TABLE["TTT"] = 'F'
CODING_TABLE["TTC"] = 'F'
CODING_TABLE["TTA"] = 'L'
CODING_TABLE["TTG"] = 'L'

CODING_TABLE["TCT"] = 'S'
CODING_TABLE["TCC"] = 'S'
CODING_TABLE["TCA"] = 'S'
CODING_TABLE["TCG"] = 'S'

CODING_TABLE["TAT"] = 'Y'
CODING_TABLE["TAC"] = 'Y'
CODING_TABLE["TAA"] = ''
CODING_TABLE["TAG"] = ''

CODING_TABLE["TGT"] = 'C'
CODING_TABLE["TGC"] = 'C'
CODING_TABLE["TGA"] = ''
CODING_TABLE["TGG"] = 'W'

CODING_TABLE["CTT"] = 'L'
CODING_TABLE["CTC"] = 'L'
CODING_TABLE["CTA"] = 'L'
CODING_TABLE["CTG"] = 'L'

CODING_TABLE["CCT"] = 'P'
CODING_TABLE["CCC"] = 'P'
CODING_TABLE["CCA"] = 'P'
CODING_TABLE["CCG"] = 'P'

CODING_TABLE["CAT"] = 'H'
CODING_TABLE["CAC"] = 'H'
CODING_TABLE["CAA"] = 'Q'
CODING_TABLE["CAG"] = 'Q'

CODING_TABLE["CGT"] = 'R'
CODING_TABLE["CGC"] = 'R'
CODING_TABLE["CGA"] = 'R'
CODING_TABLE["CGG"] = 'R'

CODING_TABLE["ATT"] = 'I'
CODING_TABLE["ATC"] = 'I'
CODING_TABLE["ATA"] = 'I'
CODING_TABLE["ATG"] = 'M'

CODING_TABLE["ACT"] = 'T'
CODING_TABLE["ACC"] = 'T'
CODING_TABLE["ACA"] = 'T'
CODING_TABLE["ACG"] = 'T'

CODING_TABLE["AAT"] = 'N'
CODING_TABLE["AAC"] = 'N'
CODING_TABLE["AAA"] = 'K'
CODING_TABLE["AAG"] = 'K'

CODING_TABLE["AGT"] = 'S'
CODING_TABLE["AGC"] = 'S'
CODING_TABLE["AGA"] = 'R'
CODING_TABLE["AGG"] = 'R'

CODING_TABLE["GTT"] = 'V'
CODING_TABLE["GTC"] = 'V'
CODING_TABLE["GTA"] = 'V'
CODING_TABLE["GTG"] = 'V'

CODING_TABLE["GCT"] = 'A'
CODING_TABLE["GCC"] = 'A'
CODING_TABLE["GCA"] = 'A'
CODING_TABLE["GCG"] = 'A'

CODING_TABLE["GAT"] = 'D'
CODING_TABLE["GAC"] = 'D'
CODING_TABLE["GAA"] = 'E'
CODING_TABLE["GAG"] = 'E'

CODING_TABLE["GGT"] = 'G'
CODING_TABLE["GGC"] = 'G'
CODING_TABLE["GGA"] = 'G'
CODING_TABLE["GGG"] = 'G'




class DNA2ProteinPlugin:
    def input(self, filename):
       fastafile = open(filename, 'r')
       self.header = fastafile.readline().strip()
       self.DNA = ''
       for line in fastafile:
           self.DNA += line.strip()

    def run(self):
       if (len(self.DNA) % 3 != 0):
           print("WARNING: Coding region length is not a multiple of 3")
       if (CODING_TABLE[self.DNA[len(self.DNA)-3:]] != ''):
           print("WARNING: Sequence does not end with a STOP codon")
       nucnum = 0
       self.protein = ''
       while (nucnum < len(self.DNA)):
           codon = self.DNA[nucnum:nucnum+3]
           self.protein += CODING_TABLE[codon]
           nucnum += 3
        

    def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write(self.header+"\n")
       outfile.write(self.protein)
