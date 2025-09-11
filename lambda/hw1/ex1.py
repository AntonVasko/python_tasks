ls = ['манг', 'корабль', "йод", "аршин", "цапляя"]
print('До:', ls)
sort = sorted(ls, key = lambda x: len(x))
print('После:', sort)