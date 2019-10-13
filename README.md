# IgblastTools

Edited by Cees van der Poel 12OCT19, Carroll lab, PCMM

Scripts to streamline Ig Blast operations after. These scripts were designed and tested on Mac. They were desgined to handle mouse V(D)J sequences obtained through sanger sequencing of single B cell cDNA.

See the HOWTO text file on how to use these scripts

-SangerCuratorV0.py
Simple python script to find continuous segments of nucleotides in a sequence that have a PHRED score >=20.


-IgBlast query and parser.zip
These scripts allow user to automatically submit sequences in the curated_sequences folder to a local Igblast. It will then parse the results to a table to allow easy analysis of the Igblast output.
This script is dependent on:
Python
Biopython
Igblast
FastX toolkit (Publicly available from http://hannonlab.cshl.edu/fastx_toolkit/index.html)

To get these scripts ready for use:
1) unzip in the root /user/ folder
2) add Igblast to /pipelines/dependencies/ncbi-igblast-1.7.0
3) add fastx toolkit to /pipelines/bin/
4) provide sequences in curated_sequence folder (suggest use SangerCuratorV0.py, though not dependent on this)
  
