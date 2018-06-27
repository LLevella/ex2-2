
punct = ',.!?:;'
ltxt = [w.rstrip(punct).lower() for w in txt.split() if len(w.rstrip(punct)) > 1]
print(*sorted(set(ltxt), key=ltxt.count, reverse=True)[:10], sep='\n')
