def namelist(names):
    answer = ''
    if len(names)>2:
        for item in names[:-2]:
            answer += item['name'] + ', '
        else:
            for item in names[-2:-1]:
                answer += item['name'] + ' & '
            else:
                answer += names[-1]['name']
    elif len(names) == 2:
        answer = names[0]['name'] + ' & ' + names[1]['name']

    elif len(names) == 1:
        answer = names[0]['name']
    
    else:
        answer = ''

    return answer

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])