set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Union
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# Intersection
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# Difference
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

# Symmetric Difference
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)

# Ejercicio 01
countries = {'MX', 'COL', 'ARG', 'USA'}
northAm = {'USA', 'CAN'}
centralAm = {'MX', 'GT', 'BZ'}
southAm = {'COL', 'ARG', 'BZ'}

# Union
print(countries.union(northAm, centralAm, southAm))

# Symmetric Difference
#new_set = countries.symmetric_difference(northAm, centralAm, southAm)
#print(new_set)
#print(countries ^ northAm ^ centralAm ^ southAm)