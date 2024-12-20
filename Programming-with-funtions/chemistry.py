from formula import parse_formula

print("""A program that computes the molar mass of a substance and the number of 
moles of a sample of that substance.""")
print()


known_molecules_dict = {
    "Al2O3": "aluminum oxide",
    "CH3OH": "methanol",
    "C2H6O": "ethanol",
    "C2H5OH": "ethanol",
    "C3H8O": "isopropyl alcohol",
    "C3H8": "propane",
    "C4H10": "butane",
    "C6H6": "benzene",
    "C6H14": "hexane",
    "C8H18": "octane",
    "CH3(CH2)6CH3": "octane",
    "C13H18O2": "ibuprofen",
    "C13H16N2O2": "melatonin",
    "Fe2O3": "iron oxide",
    "FeS2": "iron pyrite",
    "H2O": "water",
	  "CO2": "Carbon Dioxide",
	  "NH3": "Ammonia",
	  "CH4": "Methane",
	  "C2H5OH": "Ethanol",
	  "CH3COOH": "Acetic Acid",
	  "NaCl": "Sodium Chloride",
	  "CaCO3": "Calcium Carbonate",
	  "C6H12O6": "Sugar",
	  "CO(NH2)2": "Urea",
	  "H2SO4": "Sulfuric Acid",
	  "HCl": "Hydrochloric Acid",
	  "HNO3": "Nitric Acid",
	  "C2H6O2": "Ethylene Glycol",
	  "C3H6O": "Acetone",
	  "C6H6": "Benzene",
	  "C6H5CH3": "Toluene",
	  "C6H5OH": "Phenol",
	  "C9H8O4": "Aspirin",
	  "C8H9NO2": "Paracetamol",
	  "C13H18O2": "Ibuprofen",
	  "C14H14O3": "Naproxen",
	  "Al2(SO4)3": "Aluminum Sulfate",
	  "NH4NO3": "Ammonium Nitrate",
	  "Ca(OH)2": "Calcium Hydroxide",
	  "CuSO4": "Copper Sulfate",
	  "NaOH": "Sodium Hydroxide",
	  "ZnO": "Zinc Oxide",
	  "Fe2O3": "Ferric Oxide",
	  "AgNO3": "Silver Nitrate",
	  "AuCl3": "Gold Chloride",
	  "PtCl4": "Platinum Chloride",
	  "RuO4": "Ruthenium Tetroxide",
	  "Li2CO3": "Lithium Carbonate",
	  "MnO2": "Manganese Dioxide",
	  "CrO3": "Chromium Trioxide",
	  "MoO3": "Molybdenum Trioxide",
	  "WO3": "Tungsten Trioxide",
	  "RhCl3": "Rhodium Chloride",
	  "IrCl3": "Iridium Chloride",
	  "OsO4": "Osmium Tetroxide",
	  "UO2": "Uranium Oxide",
	  "PuO2": "Plutonium Oxide",
	  "AmO2": "Americium Oxide",
	  "CmO2": "Curium Oxide",
	  "BkO2": "Berkelium Oxide",
	  "CfO2": "Californium Oxide",
	  "EsO2": "Einsteinium Oxide",
	  "FmO2": "Fermium Oxide",
	  "MdO2": "Mendelevium Oxide",
	  "NoO2": "Nobelium Oxide",
	  "LrO2": "Lawrencium Oxide",
	  "RfO2": "Rutherfordium Oxide"
    } 


def make_periodic_table():
    periodic_table_dict = {
    #chemical formula[key], Element, Atomic mass
    "Ac": ["Actinium", 227],
    "Ag": ["Silver", 107.8682],
    "Al": ["Aluminum", 26.9815386],
    "Ar": ["Argon", 39.948],
    "As": ["Arsenic",74.9216],
    "At": ["Astatine", 210],
    "Au": ["Gold", 196.966569],
    "B":  ["Boron", 10.811],
    "Ba": ["Barium", 137.327],
    "Be": ["Beryllium", 9.012182],
    "Bi": ["Bismuth",208.9804],
    "Br": ["Bromine",79.904],
    "C":  ["Carbon",12.0107],
    "Ca": ["Calcium",40.078],
    "Cd": ["Cadmium",112.411],
    "Ce": ["Cerium",140.116],
    "Cl": ["Chlorine",35.453],
    "Co": ["Cobalt",58.933195],
    "Cr": ["Chromium", 51.9961],
    "Cs": ["Cesium",132.9054519],
    "Cu": ["Copper",63.546],
    "Dy": ["Dysprosium",162.5],
    "Er": ["Erbium",167.259],
    "Eu": ["Europium", 151.964],
    "F" : ["Fluorine", 18.9984032],
    "Fe": ["Iron", 55.845],
    "Fr": ["Francium", 223],
    "Ga": ["Gallium",69.723],
    "Gd": ["Gadolinium", 157.25],
    "Ge": ["Germanium", 72.64],
    "H":  ["Hydrogen", 1.00794],
    "He": ["Helium",4.002602],
    "Hf": ["Hafnium",178.49],
    "Hg": ["Mercury",200.59],
    "Ho": ["Holmium",164.93032],
    "I":  ["Iodine",126.90447],
    "In": ["Indium",114.818],
    "Ir": ["Iridium",192.217],
    "K":  ["Potassium",39.0983],
    "Kr": ["Krypton",83.798],
    "La": ["Lanthanum",138.90547],
    "Li": ["Lithium",6.941],
    "Lu": ["Lutetium", 174.9668],
    "Mg": ["Magnesium", 24.305],
    "Mn": ["Manganese", 54.938045],
    "Mo": ["Molybdenum", 95.96],
    "N":  ["Nitrogen", 14.0067],
    "Na": ["Sodium",22.98976928],
    "Nb": ["Niobium",92.90638],
    "Nd": ["Neodymium", 144.242],
    "Ne": ["Neon", 20.1797],
    "Ni": ["Nickel", 58.6934],
    "Np": ["Neptunium", 237],
    "O":  ["Oxygen", 15.9994],
    "Os": ["Osmium", 190.23],
    "P":  ["Phosphorus",30.973762],
    "Pa": ["Protactinium", 231.03588],
    "Pb": ["Lead", 207.2],
    "Pd": ["Palladium", 106.42],
    "Pm": ["Promethium", 145],
    "Po": ["Polonium", 209],
    "Pr": ["Praseodymium", 140.90765],
    "Pt": ["Platinum", 195.084],
    "Pu": ["Plutonium", 244],
    "Ra": ["Radium",226],
    "Rb": ["Rubidium",85.4678],
    "Re": ["Rhenium",186.207],
    "Rh": ["Rhodium",102.9055],
    "Rn": ["Radon",222],
    "Ru": ["Ruthenium",101.07],
    "S":  ["Sulfur",32.065],
    "Sb": ["Antimony",121.76],
    "Sc": ["Scandium",44.955912],
    "Se": ["Selenium",78.96],
    "Si": ["Silicon",28.0855],
    "Sm": ["Samarium",150.36],
    "Sn": ["Tin",118.71],
    "Sr": ["Strontium",87.62],
    "Ta": ["Tantalum",180.94788],
    "Tb": ["Terbium",158.92535],
    "Tc": ["Technetium",98],
    "Te": ["Tellurium",127.6],
    "Th": ["Thorium",232.03806],
    "Ti": ["Titanium",47.867],
    "Tl": ["Thallium",204.3833],
    "Tm": ["Thulium",168.93421],
    "U":  ["Uranium",238.02891],
    "V":  ["Vanadium",50.9415],
    "W":  ["Tungsten",183.84],
    "Xe": ["Xenon",131.293],
    "Y":  ["Yttrium",88.90585],
    "Yb": ["Ytterbium", 173.054],
    "Zn": ["Zinc", 65.38],
    "Zr": ["Zirconium", 91.224],  
    }
    return periodic_table_dict


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
    symbol_quantity_list is a compound list returned
    from the parse_formula function. Each small
    list in symbol_quantity_list has this form:
    ["symbol", quantity].
    periodic_table_dict is the compound dictionary
    returned from make_periodic_table.
    Return: the total molar mass of all the elements in
    symbol_quantity_list.
    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
    # Separate the inner list into symbol and quantity.
    # Get the atomic mass for the symbol from the dictionary. 
    # Multiply the atomic mass by the quantity.
    # Add the product into the total molar mass.
    # Return the total molar mass.
    total_molar_mass = 0
    for inner_list in symbol_quantity_list:
        symbol = inner_list[SYMBOL_INDEX]
        quantity = inner_list[QUANTITY_INDEX]
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass



def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    Parameters
    formula is a string that contains a chemical formula
    known_molecules_dict is a dictionary that contains
    known chemical formulas and their names
    Return: the name of a chemical formula
    """
    if formula in known_molecules_dict:
      name_of_compound = known_molecules_dict[formula]
      return name_of_compound
    else:
      return "Unknown compound"
    
def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in
    all the elements listed in symbol_quantity_list.
    Parameters
    symbol_quantity_list is a compound list returned
    from the parse_formula function. Each small
    list in symbol_quantity_list has this form:
    ["symbol", quantity].
    periodic_table_dict is the compound dictionary
    returned from make_periodic_table.
    Return: the total number of protons of all
    the elements in symbol_quantity_list.
    """
    total_protons = 0
    for symbol, quantity in symbol_quantity_list:
        protons_per_atom = periodic_table_dict[symbol][ATOMIC_MASS_INDEX] 
        total_protons += int(protons_per_atom) * int(quantity)  
        return total_protons

       
    

def main():
  # Get a chemical formula for a molecule from the user.
  # Get the mass of a chemical sample in grams from the user.
  # Call the make_periodic_table function and
  # store the periodic table in a variable.
  # Call the parse_formula function to convert the
  # chemical formula given by the user to a compound
  # list that stores element symbols and the quantity
  # of atoms of each element in the molecule.
  # Call the compute_molar_mass function to compute the
  # molar mass of the molecule from the compound list.
  # Compute the number of moles in the sample.
  # Print the molar mass.
  # Print the number of moles
  formula = input('Enter a chemical formula for a molecule to proceed: ')
  mass_of_chemical = float(input ("Enter the mass of a chemical sample in grams: "))
  print()
  periodic_table_dict = make_periodic_table()

  # convert chemical formula to a compound
  symbol_quantity_list = parse_formula(formula, periodic_table_dict)
  molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
  moles = mass_of_chemical / molar_mass

  #GET THE NAME OF THE COMPOUND ASSOCIATED WITH THE CHEMICAL FORMULA INPUTED
  name_of_chemical = get_formula_name(formula, known_molecules_dict)

  #get the totak number of protons in the compound
  total_protons = sum_protons(symbol_quantity_list, periodic_table_dict)
  print(f"Molar mass: {round(molar_mass, 4)} g/mol")
  print(f"Number of moles: {round(moles, 4)} mol")
  print()

  print(f"The total number of protons in the compound is: {total_protons}")
  print(f"The name of the compound is: {name_of_chemical}")
  print()


if __name__ == "__main__":
  main()



