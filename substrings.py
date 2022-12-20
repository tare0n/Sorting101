def unique_subs_find(string):
    uniques = [""]
    uniques += list(set(string))
    for i in range(2, len(string)+1):
        uniques += list(set([string[g:g+i] for g in range(0, len(string)-i+1)]))
    print(f"Количество уникальных подстрок: {len(uniques)}")
    print(f"Уникальные подстроки: {uniques}")


unique_subs_find("gfg")

