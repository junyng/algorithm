from itertools import combinations

def solution(orders, course):
    course_menu_candidates = []
    
    for cuisine_count in course:
        menus = dict()
        for order in orders:
            comb_list = list(combinations(order, cuisine_count))
            for comb in comb_list:
                menu = ''.join(sorted(comb))
                if menu in menus:
                    menus[menu] += 1
                else:
                    menus[menu] = 1
        if menus:
            max_count = max(menus.values())
            if max_count >= 2:
                for key, value in menus.items():
                    if value == max_count:
                        course_menu_candidates.append(key)
    course_menu_candidates.sort()
    return course_menu_candidates
