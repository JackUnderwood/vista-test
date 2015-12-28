import tool.generators.state_codes as sc

__author__ = 'jounderwood'

# from tool.generators.generator import gen_ssn

# ssn = gen_ssn()
# print(ssn)

state = sc.get_random_state_iso_code()
print(state)
print(sc.get_random_area_code(state))
print(sc.get_state_names())
print(sc.get_states())

print(sc.get_state_name('ca'))
