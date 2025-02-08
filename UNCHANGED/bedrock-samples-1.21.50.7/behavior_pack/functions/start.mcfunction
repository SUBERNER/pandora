execute as @a[tag=STARTED] at @s run tag @a add STARTED
execute as @a[tag=!STARTED] at @s run function random_functions
tag @a add STARTED

