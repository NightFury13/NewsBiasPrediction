import pickle as pkl

in_file = 'eco_data.pkl'

with open(in_file, 'r') as f:
    data = pkl.load(f)

# Printing only the first 5 entries.
for i in data[1:5]:
    print i
    for x in range(20):
        print "~",
    print "~"

print ""
print "Total Entries :", len(data)
