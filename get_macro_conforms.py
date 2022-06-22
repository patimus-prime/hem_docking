
from meeko import MoleculePreparation
from rdkit import Chem
import os #necessary to define file path
import os.path #this is necessary to overcome python not recognizing ~
import sys

# when this is called "python" in command is ignored
input_molecule_file = sys.argv[1]
print("This is it:" + sys.argv[1])
mol = Chem.MolFromMol2File(input_molecule_file)

preparator = MoleculePreparation(hydrate=True) # macrocycles flexible by default since v0.3.0
preparator.prepare(mol)
preparator.show_setup()

output_pdbqt_file = "test_macrocycle_hydrate.pdbqt"
preparator.write_pdbqt_file(output_pdbqt_file)