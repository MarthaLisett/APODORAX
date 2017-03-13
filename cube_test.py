from semantic_cube import semantic_cube

cs = semantic_cube()

print cs.verify_type_match("falso", "verdadero","&&")
print cs.verify_type_match("falso", "hola","&&")
print cs.verify_type_match("falso", "a","&&")
print cs.verify_type_match("falso",  3,"&&")

print('---------')

print cs.verify_type_match(3, 4, "+")
print cs.verify_type_match(3, 4, "-")
print cs.verify_type_match(3, 4.4, "*")
print cs.verify_type_match(3.1, 4, "/")