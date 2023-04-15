from pymol import cmd


def hydrophobicity(selection='all', palette = "red_blue"):
    """
    The function uses the spectrum function of pymol api to
    colour the protein structure according to the Kyte-Doolittle scale
    by using the B-Factors

    Arguments:
    s :: current selection (default value is all)
    palette :: it is the palate type (default value is red_blue)
    """
    s = str(selection)
    p = str(palette)
    cmd.spectrum("b", palette, selection=s)
    
cmd.extend('hydrophobicity',hydrophobicity)










