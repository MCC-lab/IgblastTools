# IgblastTools
Scripts to streamline Ig Blast operations after. These scripts were designed and tested on Mac. They were desgined to handle analyze mouse V(D)J sequences obtained through sanger sequencing of single B cell cDNA.

See the HOWTO text file on how to use these scripts

-IgBlast query and parser.zip
These scripts allow user to automatically submit sequences in the curated_sequences folder to a local Igblast. It will then parse the results to a table to allow easy analysis of the Igblast output.
This script is dependent on:
Python
Biopython
Igblast
FastX toolkit (Publicly available from http://hannonlab.cshl.edu/fastx_toolkit/index.html)

To use this script:
1) unzip in the root /user/ folder
2) add Igblast to /pipelines/dependencies/ncbi-igblast-1.7.0
3) add fastx toolkit to /pipelines/bin/

  
