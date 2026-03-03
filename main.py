def get_average_grade(scores):
    set_scores = (('A+',79,100),('A',93,96),('A-',90,92),('B+',87,89),('B',83,86),('B-',80,82),('C+',77,79),('C',73,76),('C-',70,72),('D+',67,69),('D',63,66),('D-',60,62),('F',0,59))
    prom = sum(scores)/len(scores)
    print(prom)
    for i in range(len(set_scores)):
        #print(i)
        #print(prom in range(set_scores[i][1],set_scores[i][2]))
        if (prom in range(set_scores[i][1],set_scores[i][2])): return set_scores[i][0]
    return prom

if __name__ == '__main__':
    print(get_average_grade([92, 91, 90, 94, 89, 93]))
    print('-----')
    print(get_average_grade([84, 89, 85, 100, 91, 88, 79]))
    print('-----')
    print(get_average_grade([63, 69, 65, 66, 71, 64, 65]))
    print('-----')
    print(get_average_grade([97, 98, 99, 100, 96, 97, 98, 99, 100]))
    print('-----')
    print(get_average_grade([75, 100, 88, 79, 80, 78, 64, 60]))
    print('-----')
    print(get_average_grade([45, 48, 50, 52, 100, 54, 56, 58, 59]))