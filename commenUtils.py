def get_input_data(input_file_name: str) -> list[list[str]]:
    f = open(input_file_name, "r")
    anwers_per_group_per_person: list[list[str]] = []
    current_group: list[str] = []
    for line in f:
        if line.strip() == "":
            anwers_per_group_per_person.append(current_group)
            current_group = []
            continue
        current_group.append(line.strip())
    anwers_per_group_per_person.append(current_group)
    f.close()
    return anwers_per_group_per_person
