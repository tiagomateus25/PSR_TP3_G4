# PSR_TP3_G4
Trabalho prático 3 do grupo 4

#worlds

#arenas

roslaunch p_g4_bringup gazebo.launch

#pista

roslaunch p_g4_bringup track.launch

#jogo da apanhada

roslaunch p_g4_bringup game_bringup.launch

#condução manual

roslaunch p_g4_bringup bringup.launch && roslaunch p_g4_bringup teleop.launch

#arbitro

rosrun th_referee th_referee
