import mbuild as mb
from foyer import Forcefield
from foyer.tests.utils import get_fn
from ilforcefields import utils
#load all mol2 files and name them
bmim = mb.load('bmim.mol2')
bmim.name = 'bmim'
tf2n = mb.load('tf2n.mol2')
tf2n.name ='tf2n'

#fill box with IL's and solvent 
system = mb.fill_box(compound=[bmim, tf2n],
        n_compounds=[173,173], box = [7,7,7])

#forloop to add IL's or solvents to respective compounds
lopes = Forcefield('/Users/arjunbansal/Documents/GitHub/ilforcefields/ilforcefields/kpl/kpl.xml')
#print(foyer.__file__)

systemPM = lopes.apply(system, residues=['bmim','tf2n'], assert_bond_params = False,  assert_angle_params=False, assert_dihedral_params=False)  #apply forcefield to IL's


#Save system to .gro and .top files
systemPM.save('init.gro', overwrite=True)
systemPM.save('init.top', overwrite=True)
