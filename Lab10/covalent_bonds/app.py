def main():
    query = input(
        "Which bond would you like to search within the database (|,||,|||): "
    )
    try:
        filename = "/home/mohan/CS2526/Lab10/covalent_bonds/bond_data.txt"
        with open(filename, "r") as file:
            single = "|"
            double = "||"
            triple = "|||"
            for line in file:
                line = line.strip()
                parts = line.split()
                bond_type = parts[0]
                bond_energy = parts[1]
                bond_length = parts[2]
                if (
                    query.lower() == "|"
                    and single in parts[0]
                    and not double in parts[0]
                ):
                    print(
                        f"{bond_type}: {bond_energy} kJ/mole, bond length: {bond_length}"
                    )
                if (
                    query.lower() == "||"
                    and double in parts[0]
                    and not triple in parts[0]
                ):
                    print(
                        f"{bond_type}: {bond_energy} kJ/mole, bond length: {bond_length}"
                    )
                if query.lower() == "|||" and triple in parts[0]:
                    print(
                        f"{bond_type}: {bond_energy} kJ/mole, bond length: {bond_length}"
                    )
    except FileNotFoundError:
        print("The input file does not exist.")


main()
