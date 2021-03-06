#!/usr/bin/env python3

import rospy

def configurarEquipa(player_name):

    equipa={'red': rospy.get_param('/red_players'),
            'blue': rospy.get_param('/blue_players'),
            'green': rospy.get_param('/green_players')}

    # print (equipa['red'])

    if player_name in equipa['red']:
        equipa['minhaquipa'], equipa['presas'], equipa['cacador'] = 'red','green','blue'
    elif player_name in equipa['green']:
            equipa['minhaquipa'], equipa['presas'], equipa['cacador'] = 'green', 'blue', 'red'
    elif player_name in equipa['blue']:
        equipa['minhaquipa'], equipa['presas'], equipa['cacador'] = 'blue', 'red', 'green'
    else:
        rospy.loginfo('o jogador '+player_name+' nao tem equipa')
        return equipa

    equipa['colegas']=equipa[equipa['minhaquipa']]
    equipa['m_presas'] = equipa[equipa['presas']]
    equipa['m_cacador'] = equipa[equipa['cacador']]

    rospy.loginfo('OK Equipas definidas ::' + player_name + '  tem equipa')

    return equipa

def configurarEstrategia(player_team, player_name):

    print(player_team + "  Equpa e jogador "+ player_name + "   parameter::" + player_team + player_name)

    estrategia = {player_name: rospy.get_param('/' + player_team + player_name)}

    temp =  estrategia[player_name]
   # print("Utilitario ::" + str(temp))

    if temp == 4:
        estrategia[player_name] = 3
    if abs(rospy.get_param('/positive_score') ) > abs(rospy.get_param('/negative_score')):
        estrategia[player_name] = 1
    if abs(rospy.get_param('/positive_score') ) < abs(rospy.get_param('/negative_score')):
        estrategia[player_name] = 2

    return estrategia
