import sys
import re
from Bio import Seq,SeqIO

iname=sys.argv[1]

cdr3p=re.compile("(TT[TC]|TA[CT])(TT[CT]|TA[TC]|CA[TC]|GT[AGCT]|TGG)(TG[TC])(([GA][AGCT])|TC)[AGCT]([ACGT]{3}){5,32}TGGG[GCT][GCT]")

# Utility functions
def get_records(filename):
  records=[]
  for record in SeqIO.parse(filename,"fasta"):
    records.append(record)
  return records

records=get_records(iname)

numrecords=len(records)
results=[]
for i in range(numrecords):
  r=records[i]
  strseq=str(r.seq)
  m=cdr3p.search(strseq)
  if m!=None:
    mspan=m.span()
    result=strseq[0:(mspan[0]+9)]
  else:
    result=""
  results.append(result)

for i in range(numrecords):
  r=records[i]
  des=r.description
  res=results[i]
  if res!="":
    print ">"+des+"\n"+res
