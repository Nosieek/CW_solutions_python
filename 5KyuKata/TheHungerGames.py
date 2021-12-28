def who_eats_who(zoo):
    who_eats_what ={
    'antelope':('grass'),
    'cow':('grass'),
    'sheep':('grass'),
    'giraffe':('leaves'),
    'panda':('leaves'),
    'bug':('leaves'),
    'chicken':('bug'),
    'big-fish':('little-fish'),
    'bear':('big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'),
    'fox':('chicken', 'sheep'),
    'lion':('antelope', 'cow')
    }
    eat = []
    survived = zoo.split(',')
    in_zoo = zoo.split(",")
    for animal in who_eats_what:
        for eats in in_zoo:
            if eats in who_eats_what[animal]:
                eat.append(animal + ' eats ' + eats)
                survived.remove(eats)
    eat = eat + survived
    zoo = zoo.split("'") + eat
    return zoo

print(who_eats_who("fox,bug,chicken,grass,sheep"))