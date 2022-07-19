import sys
import os
import logging
import pyrosetta.distributed.viewer as viewer
import pyrosetta.distributed
import pyrosetta
import pyrosetta
pyrosetta.init()
logging.basicConfig(level=logging.INFO)


interface = "A_X"  # :HEM will be renamed to X

# get the parameters file of heme, which
# will be PER heme
#HEM_params = os.path("~/project/HEM.params")
#pyrosetta.init("-extra_res_fa {}".format(HEM_params))

# pdb_filename = os.path("~/project/pdb_src/7C74.pdb")
# pose = pyrosetta.rosetta.core.pose.Pose()
# pyrosetta.io.pose_from_file(pose, pdb_filename)

pose = pyrosetta.io.pose_from_file("pdb_src/7C74.pdb")

ia = pyrosetta.rosetta.protocols.analysis.InterfaceAnalyzerMover(interface)
ia.apply(pose)
print({'complex_energy': ia.get_complex_energy(),
       'separated_interface_energy': ia.get_separated_interface_energy(),
       'complexed_sasa': ia.get_complexed_sasa(),
       'crossterm_interface_energy': ia.get_crossterm_interface_energy(),
       'interface_dG': ia.get_interface_dG(),
       'interface_delta_sasa': ia.get_interface_delta_sasa()})


# params_file = "HEM.params"
# flags = f"""
# -extra_res_fa {params_file}
# -s '{pdb_filename}'
# -mute all
# -ex1
# -ex2
# -no_optH false
# -flip_HNQ true
# -ignore_ligand_chi true
# -overwrite
# """
