def validate_dict (rules, d):
    for key, prefix, middle, suffix in rules:
        if key not in d:
            return False
        value = d[key]
        if not value.startswith(prefix) or not value.endswith(suffix):
            return False
        if middle not in value[1:-1]:
            return False
    return True


input_rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d1 = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
d2 = {
    "key1": "come inside, it's too cold out",
    "key2": "starting in the middle of winter",
}

print(validate_dict(input_rules, d1))
print(validate_dict(input_rules, d2))
