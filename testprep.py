# chimera --nogui heme_prep.py ARGS

# Receive pdb and produce the ligand file,
# perhaps also the chain A of pdb
# NOTE: mucho weirdness. elaboration below on execution
# ---------------------------------

import os #necessary to define file path
import os.path #this is necessary to overcome python not recognizing ~
import sys
import chimera

from chimera import runCommand as rc
from chimera import replyobj # gives status messages
from chimera import dialogs # LOL the reply log keeps spilling over
#import settings

#replyDialog = dialogs.find("reply")
#replyDialog.Clear()
#print('this:' , sys.path)
print('hola jefe')

#DIR = "~/project/"
#os.chdir('~/project')

# sys.argv[0] will be name of this ,py

#print('idk how args work one sec')
print('0: '+ sys.argv[0])
print('1: '+ sys.argv[1])
print('2: '+ sys.argv[2])
#print('3: '+ sys.argv[3])
#current_pdb = sys.argv[1] 

currentPDB = sys.argv[3]
print("Current pdb:", currentPDB)
#pdb_src_dir = os.path.expanduser("~/project/pdb_src/")
#os.chdir(pdb_src_dir)

#print("X:",pdb_src_dir)


#print(sys.path)
rc("open " + currentPDB)
rc("write format pdb 0 ~/project/copy.pdb")
#working so far

rc("sel :.A") # get only chain A
rc("del ~sel") # delete not chain A

# get hem, delete everything else

rc("sel :HEM") #get only the heme inside chain A
rc("del ~sel") # delete not heme in chain A
#rc("del Fe")
# create the bonds
#rc("sel @NA | Fe; bond sel")
#rc("sel @NB | Fe; bond sel")
#rc("sel @NC | Fe; bond sel")
#rc("sel @ND | Fe; bond sel")
#rc("addh")

# done. now export this as a pdb
#
# ... or rather as a mol2, can easi
# ly change
#rc("write format mol2 0 " +pdb_src_dir+"heme-1w0e.mol2")
rc("write format mol2 0 ~/project/heme-test.mol2")

rc("close all")
# rc(("write format pdb 0 "+unexpandedResultPath+activeLigand+"/%s")%(fn + ".mono.pdb"))

# ---------------------
# Somehow pychimera cannot find chimera...
# And I have spent WAY too much time trying
# to point it towards chimera;
# therefore this is the solution:
# running this script as:




# that's it. no mas. we're barely using this anyway

# and use this:
#sourcePath = "~/heme-binding/pdb_source_data/0_raw_download/"
#resultPath = "~/heme-binding/pdb_source_data/1_monomers_processed/"

##for activeLigand in ligandList:
#    activeSourcePath = os.path.expanduser(sourcePath + activeLigand)


