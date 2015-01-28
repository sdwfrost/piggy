import sys
from Bio import Seq,SeqIO

## Set parameters

# Outfile name
oname=str(sys.argv[1])

## V and J
vname=str(sys.argv[2])
jname=str(sys.argv[3])

## Shouldn't have to change anything below

vseqs={}
for record in SeqIO.parse(vname,"fasta"):
  vname=record.id
  vallele=vname.split("*")[1]
  if vallele=="01":
    vseqs[vname]=str(record.seq).upper()
vgenes=vseqs.keys()
vgenes.sort()

jseqs={}
for record in SeqIO.parse(jname,"fasta"):
  jname=record.id
  jallele=jname.split("*")[1]
  if jallele=="01":
    jseqs[record.id]=str(record.seq).upper()
jgenes=jseqs.keys()
jgenes.sort()

ofile=open(oname,'w')
i=1
for vg in vgenes:
  v=vseqs[vg]
  for jg in jgenes:
    j=jseqs[jg]
    ofile.write(">"+vg+"|"+jg+"\n"+v+j+"\n")
    i+=1
ofile.close()
