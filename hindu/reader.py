import pickle as pkl

in_file = 'hindu_data.pkl'

with open(in_file, 'r') as f:
    data = pkl.load(f)

# Printing only the first 10 entries.
for i in data[1:10]:
    print i

