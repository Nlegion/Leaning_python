def from_string_to_list(string, container):
    return container.extend(map(int, string.split()))