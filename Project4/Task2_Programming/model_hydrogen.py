# Comparative modeling with ligand transfer from the template
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Read in HETATM records from template PDBs
env.io.hetatm = True

a = automodel(env,
              alnfile  = 'Taget_rcsb_pdb_101M_Template_101m.ali',  # alignment filename
              knowns   = '101mA',              # codes of the templates
              sequence = '101M_1',              # code of the target
              assess_methods=(assess.DOPE,
                              #soap_protein_od.Scorer(),
                              assess.GA341))
a.starting_model= 1                 # index of the first model
a.ending_model  = 5                 # index of the last model
                                    # (determines how many models to calculate)
a.make()     
