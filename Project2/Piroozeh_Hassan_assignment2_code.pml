## Fetching the molecule
fetch 1A6M

## Removing Water
remove resn hoh



##Selecting and renaming the selections for Lignads
select HEM, ( resn HEM )
select OXY, ( resn OXY )
select SO4, ( resn SO4 )



## Colouring everything Red
color red



### colour binding sites (residues within 5 angstroms of the ligands) white

## Selecting the residues
select HEM_A5, byres all within 5 of HEM
select OXY_A5, byres all within 5 of OXY
select SO4_A5, byres all within 5 of SO4


##Colouring the binding sites white
color white, HEM_A5
color white, OXY_A5
color white, SO4_A5



## Hiding the cartoons of the Ligands
hide everything, HEM
hide everything, OXY
hide everything, SO4


## Hiding the cartoons of the Binding Sites
hide everything, HEM_A5
hide everything, OXY_A5
hide everything, SO4_A5

#Colouring the Ligands Grey
color grey40, HEM
color grey40, OXY
color grey40, SO4

## Showing Ligands as sticks
show sticks, HEM
show sticks, OXY
show sticks, SO4


## Showing Binding Sites as sticks
show sticks, HEM_A5
show sticks, OXY_A5
show sticks, SO4_A5





set ray_opaque_background, 100
png test.png, width=10cm, dpi=300, ray=2
