from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
player.position = (10,10,10)

sky = Sky()

boxes = []

for i in range(20):
    for j in range(20):
        box = Button(
            color=color.green,
            texture='grass.png',
            model='cube',
            position=(j,-1,i),
            parent=scene,
            origin_y=0.5,
            collider='box'
        )
        boxes.append(box)

def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(
                    color=color.green,
                    model='cube',
                    texture='grass.png',
                    position=box.position + mouse.normal,
                    parent=scene,
                    origin_y=0.5,
                    collider='box'
                )
                boxes.append(new)

            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)

            break

app.run()
