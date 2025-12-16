# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def forward(count):
    agent.move(FORWARD,count)
player.on_chat("f", forward)
def backward(count):
    agent.move(BACK,count)
player.on_chat("b", backward)
def up(count):
    agent.move(UP,count)
player.on_chat("u", up)
def down(count):
    agent.move(DOWN,count)
player.on_chat("d", down)

def move():
    agent.move(FORWARD,4)
    agent.turn(LEFT)
    agent.move(FORWARD,4)
    agent.turn(RIGHT)
    agent.move(FORWARD,3)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(FORWARD,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
player.on_chat("move", move)

def moveback():
    agent.turn(LEFT)
    agent.turn(LEFT)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(FORWARD,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,3)
    agent.turn(LEFT)
    agent.move(FORWARD,4)
    agent.turn(RIGHT)
    agent.move(FORWARD,4)
player.on_chat("mb",moveback)

player.on_chat


def chop():
    for count in range(10):
        agent.destroy(FORWARD)
        agent.collect_all()
        agent.move(UP, 1)
    agent.move(DOWN, 10)
player.on_chat("ch", chop)