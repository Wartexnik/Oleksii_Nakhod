def sort_names(names):
    names_upper = names.upper()
    split_people = names_upper.split(";")
    split_names = list(map(lambda person: person.split(":"), split_people))
    swapped_last_first_name = list(
        map(lambda person: [person[1], person[0]], split_names))
    sorted_names = sorted(swapped_last_first_name)
    string_sorted_names = list(
        map(lambda person: f'({", ".join(person)})', sorted_names))
    string_sorted_people = "".join(string_sorted_names)
    return string_sorted_people

