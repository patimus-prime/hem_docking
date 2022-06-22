#!/bin/bash

# WARNING: this .sh should be in the project directory
    # if it ain't, need to make the files below more explicit
# WARNING: heme_prep.py relies on index for naming, will
    # need to be altered for alternate repositories to work.


pwd 


for pdbfile in pdb_src/*.pdb
do
    echo $pdbfile
    
    # fyi on below, for sys.argv in the heme_prep.py
    #  [0]    [1]     [2]         [3]
    chimera --nogui heme_prep.py $pdbfile
    # therefore we reference sys.argv[3] to enable iterating through file

    # works so far, fuck yeah. need to test with multiple files...
    # ... later.

    # very, very strange problems with
    # installation of rkit and meeko. not detected
    # therefore need to use command line...
    # so python get_macro... to use
done

for hememol2 in mol2_heme/*.mol2
do
    echo $hememol2
    python get_macro_conforms.py $hememol2
    # shit works with other macrocycles in that example :X

done