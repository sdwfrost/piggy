# piggy
Python for immunoglobulin sequence analysis

- ```extract_CDR3.py``` : extracts CDR3 sequences from FASTA files using a regexp. This only extracts hits, so the number of CDR3 may well be less.
- ```extract_V.py``` : extracts sequences upstream of the CDR3 (including the CDR3 bit of V) using a regexp.
- ```join_VJ.py``` : prepares a reference alignment by joining a multiple sequence alignment (MSA) of V with a MSA of J regions, for use with standard alignment software.
