# sallie = name_subst("Sallie", "My friend, ZZZ, won an award.")
# if sallie == "ZZZ":
# print(sallie)

def name_subst(name: str, text: str) -> str:
    return text.replace("ZZZ",name)
# sallie = name_subst("Sallie", "My friend, ZZZ, won an award.")
print(name_subst("Sallie", "My friend, ZZZ, won an award"))
