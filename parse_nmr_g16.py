import sys
import re
import csv
from math import exp

try:
    import typer
except ImportError:
    sys.exit("typer not installed, install it with 'pip install typer[all]")

# constants
BOLTZMANN = 0.0019872041


def open_file(file_name):
    with open(file_name) as f:
        opened_file = f.readlines()
    return opened_file


def get_nmr_ranges(file):
    line_ranges = []
    for line in range(0, len(file)):
        if "Total nuclear spin-spin coupling J" in file[line]:
            for i in range(line, len(file)):
                if "End of Minotr F.D" in file[i]:
                    break
            line_ranges.append((line + 2, i))

    # check if coupling data was found
    if len(line_ranges) == 0:
        sys.exit("No coupling data found in the NMR file provided, exiting...")
    else:
        print("Found {} conformers in the NMR file.".format(len(line_ranges)))

    return line_ranges


def parse_tables(file):
    nmr_file = open_file(file)
    line_ranges = get_nmr_ranges(nmr_file)
    tables = []
    for line_range in line_ranges:  # line_range is a tuple (start,end)
        table = {}
        formatted_lines = []

        for line in nmr_file[line_range[0]:line_range[1]]:
            if line.startswith("               "):
                continue
            else:
                nline = re.sub("D", "E", re.sub("  ", " ", line.strip()))
                formatted_lines.append([float(a) for a in nline.split(" ")])

        for formatted_line in formatted_lines:
            if formatted_line[0] in table.keys():
                table[formatted_line[0]] = table[formatted_line[0]] + \
                    formatted_line[1::]
            else:
                table[formatted_line[0]] = formatted_line[1::]
        tables.append(table)
    return tables


def write_conformers(tables, filename):
    """
    From a dict to a .csv file with all the conformers
    """
    # first save all the conformers
    with open("conformers.csv", "w") as f:
        write = csv.writer(f)
        for table in tables:
            atom_nrs = list(table.keys())
            write.writerow(["atom nr"] + [int(a) for a in atom_nrs])
            for row in atom_nrs:
                write.writerow([int(row)] + table[row])
    print("Conformer data saved to conformers.csv")


def get_energies(energy_file):
    energies = []
    for line in energy_file:
        if "Sum of electronic and thermal Free Energies" in line:
            energy = line.split("=")[1].lstrip().rstrip()
            energies.append(float(energy))

    # check if freq data was found
    if len(energies) == 0:
        sys.exit("No freq data found in the energy file provided, exiting...")
    else:
        print("Found {} conformers in the energy file.".format(len(energies)))

    return energies


def get_populations(energy_file, temperature=298.15):
    energy_lines = open_file(energy_file)
    populations = []
    energies = get_energies(energy_lines)
    minima = min(energies)

    for i in range(0, len(energies)):
        energies[i] = (energies[i] - minima) * 627.503

    for energy in energies:
        pop = exp(-energy/(BOLTZMANN*temperature))
        populations.append(pop)

    total_sum = sum(populations)
    for i in range(0, len(populations)):
        populations[i] = populations[i]/total_sum
    return populations


def average_coupling(tables, populations, save=True):
    final_table = {}
    print(len(populations), len(tables))
    if len(populations) != len(tables):
        sys.exit(
            "Number of conformers in energy file is different from NMR file, exiting...")

    for i in range(0, len(tables)):
        keys = tables[i].keys()
        if i == 0:
            for line in keys:
                final_table[line] = [coupling*populations[i]
                                     for coupling in tables[i][line]]
        else:
            for line in keys:
                final_table[line] = [final_table[line][j] +
                                     tables[i][line][j]*populations[i]
                                     for j in range(len(final_table[line]))]

    if save:
        with open("averaged.csv", "w") as f:
            write = csv.writer(f)
            atom_nrs = list(final_table.keys())
            write.writerow(["atom nr"] + [int(a) for a in atom_nrs])
            for row in atom_nrs:
                write.writerow([int(row)] + final_table[row])


def main(
        nmr_file: str,
        energy_file: str,
        temperature: float = 298.15,
        save_conformers: bool = True
):
    populations = get_populations(energy_file)
    tables = parse_tables(nmr_file)
    average_coupling(tables, populations)

    if save_conformers:
        write_conformers(tables, nmr_file)


if __name__ == "__main__":
    typer.run(main)
