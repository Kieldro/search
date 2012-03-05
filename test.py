

def name(a):
	print a
	tup = (1, 2, 3)
	t2 = tup + (4,)

n = name

actions = ['sit', 'stand']
action = 'jump'
n(actions + [action])
actions = actions + [action]
print actions
