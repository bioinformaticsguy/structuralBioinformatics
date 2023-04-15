########  The # values for the colours were taken from the following website:
###       http://www.jalview.org/help/html/colourSchemes/hydrophobic.html


####<td bgcolor="#ff0000">I</td>    Ile	I	Isoleucine
####<td bgcolor="#f60009">V</td>    Val	V	Valine
####<td bgcolor="#ea0015">L</td>    Leu	L	Leucine
####<td bgcolor="#cb0034">F</td>    Phe	F	Phenylalanine
####<td bgcolor="#c2003d">C</td>    Cys	C	Cysteine
####<td bgcolor="#b0004f">M</td>    Met	M	Methionine
####<td bgcolor="#ad0052">A</td>    Ala	A	Alanine
####<td bgcolor="#6a0095">G</td>    Gly	G	Glycine
####<td bgcolor="#680097">X</td>    Xaa	X	Any amino acid
####<td bgcolor="#61009e">T</td>    Thr	T	Threonine
####<td bgcolor="#5e00al">S</td>    Ser	S	Serine
####<td bgcolor="#5b00a4">W</td>    Trp	W	Tryptophan
####<td bgcolor="#4f00b0">Y</td>    Tyr	Y	Tyrosine
####<td bgcolor="#4600b9">P</td>    Pro	P	Proline
####<td bgcolor="#1500ea">H</td>    His	H	Histidine
####<td bgcolor="#0c00f3">E</td>    Glu	E	Glutamic acid
####<td bgcolor="#0c00f3">Z</td>    Glx	Z	Glutamic acid or Glutamine
####<td bgcolor="#0c00f3">Q</td>    Gln	Q	Glutamine
####<td bgcolor="#0c00f3">D</td>    Asp	D	Aspartic acid
####<td bgcolor="#0c00f3">B</td>    Asx	B	Aspartic acid or Asparagine
####<td bgcolor="#0c00f3">N</td>    Asn	N	Asparagine
####<td bgcolor="#0000ff">K</td>    Lys	K	Lysine
####<td bgcolor="#0000ff">R</td>    Arg	R	Arginine



from pymol import cmd


def hashtoRGBList(hashcode):
    hashcode = hashcode.lstrip('#')
    RGBList = []
    for i in (0, 2, 4):
        RGBList.append((int(hashcode[i:i+2],16)))
    return RGBList


def hydrophobicity(selection='all'):
        s = str(selection)
        print(s)        
        cmd.set_color('color_phe',hashtoRGBList("#cb0034"))
        cmd.set_color('color_val',hashtoRGBList("#f60009"))
        cmd.set_color('color_leu',hashtoRGBList("#ea0015"))
        cmd.set_color('color_trp',hashtoRGBList("#5b00a4"))
        cmd.set_color('color_met',hashtoRGBList("#b0004f"))
        cmd.set_color('color_ala',hashtoRGBList("#ad0052"))
        cmd.set_color('color_gly',hashtoRGBList("#6a0095"))
        cmd.set_color('color_cys',hashtoRGBList("#c2003d"))
        cmd.set_color('color_tyr',hashtoRGBList("#4f00b0"))
        cmd.set_color('color_pro',hashtoRGBList("#4600b9"))
        cmd.set_color('color_thr',hashtoRGBList("#4f00b0"))
        cmd.set_color('color_ser',hashtoRGBList("#5e00a1"))
        cmd.set_color('color_his',hashtoRGBList("#1500ea"))
        cmd.set_color('color_glu',hashtoRGBList("#0c00f3"))
        cmd.set_color('color_asn',hashtoRGBList("#0c00f3"))
        cmd.set_color('color_gln',hashtoRGBList("#0c00f3"))
        cmd.set_color('color_asp',hashtoRGBList("#0c00f3"))
        cmd.set_color('color_lys',hashtoRGBList("#0000ff"))
        cmd.set_color('color_arg',hashtoRGBList("#0000ff"))
        cmd.set_color('color_ile',hashtoRGBList("#ff0000"))

        cmd.color("color_ile","("+s+" and resn ile)")
        cmd.color("color_phe","("+s+" and resn phe)")
        cmd.color("color_val","("+s+" and resn val)")
        cmd.color("color_leu","("+s+" and resn leu)")
        cmd.color("color_trp","("+s+" and resn trp)")
        cmd.color("color_met","("+s+" and resn met)")
        cmd.color("color_ala","("+s+" and resn ala)")
        cmd.color("color_gly","("+s+" and resn gly)")
        cmd.color("color_cys","("+s+" and resn cys)")
        cmd.color("color_tyr","("+s+" and resn tyr)")
        cmd.color("color_pro","("+s+" and resn pro)")
        cmd.color("color_thr","("+s+" and resn thr)")
        cmd.color("color_ser","("+s+" and resn ser)")
        cmd.color("color_his","("+s+" and resn his)")
        cmd.color("color_glu","("+s+" and resn glu)")
        cmd.color("color_asn","("+s+" and resn asn)")
        cmd.color("color_gln","("+s+" and resn gln)")
        cmd.color("color_asp","("+s+" and resn asp)")
        cmd.color("color_lys","("+s+" and resn lys)")
        cmd.color("color_arg","("+s+" and resn arg)")
cmd.extend('hydrophobicity',hydrophobicity)
