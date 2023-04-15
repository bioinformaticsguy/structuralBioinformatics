from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='_Template_101m', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='101mA', atom_files='_Template_101m.pdb')
aln.append(file='_Taget_rcsb_pdb_101M.ali', align_codes='101M_1')
aln.align2d(max_gap_length=50)
aln.write(file='Taget_rcsb_pdb_101M_Template_101m.ali', alignment_format='PIR')
aln.write(file='Taget_rcsb_pdb_101M_Template_101m.pap', alignment_format='PAP')
