import tools

print(tools.transcribe("ACGT"))
print(tools.revcomp("AAAACGT"))


s = 'ACGTGGGGGGCATATG'
print(tools.gc_comp(s))
print(tools.gc_skew(s), tools.gc_skew(tools.revcomp(s)))

list = []
for nt in s:
	list.append(nt)
print(list)
list[3] = "hello"
print(list)