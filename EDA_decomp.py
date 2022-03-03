#!/home/vport/.pyenv/shims/python

import sys
import re


def format_tables(
    table: list[str], filename: str, output: list[list[str]]
) -> list[list[str]]:
    for line in table:
        line = re.sub("\n", "", re.sub(" +", " ", line))[1::]
        line = line.split(": ")
        formatted = (line[0], line[1].split(" ")[2])  # valores em kcal/mol

        # adiciona o nome do arquivo como uma nova coluna
        if filename not in output[0]:
            output[0].append(filename)
            for row in output[1:]:
                row.append("")

        # encontra a posição da coluna correspondente ao arquivo atual
        idx = output[0].index(filename)

        # adiciona o valor formatado na coluna correspondente
        for row in output[1:]:
            if row[0] == formatted[0]:
                row[idx] = formatted[1]
                break
        else:
            output.append([formatted[0]] + [""] * (len(output[0]) - 1))
            output[-1][idx] = formatted[1]

    return output


def main():
    if len(sys.argv) < 2:
        print("At least one file is required as argument.")
        sys.exit(1)

    # cria a tabela de saída
    output = [[""]]  # cabeçalho da tabela

    for i in range(1, len(sys.argv)):
        try:
            with open(sys.argv[i]) as file:
                full_file = file.readlines()
        except UnicodeDecodeError:
            print(
                f"Byte not allowed in file {sys.argv[i]}, check if there are no accents in the log.")
        except FileNotFoundError:
            print(f"File {sys.argv[i]} not found, check if file exists.")
            continue

        found_file = False

        for j in range(0, len(full_file)):
            if "Summary of Bonding Energy" in full_file[j]:
                table: list[str] = (
                    [full_file[j + 9]]
                    + [full_file[j - 32]]
                    + [full_file[j + 3]]
                    + [full_file[j + 7]]
                    + [full_file[j - 15]]
                )
                output = format_tables(table, sys.argv[i], output)
                found_file = True

        if not found_file:
            print(
                f"Could not find summary of bonding energy in file {sys.argv[i]}.")

    # imprime a tabela formatada
    for row in output:
        print(",".join(row))


if __name__ == "__main__":
    main()
