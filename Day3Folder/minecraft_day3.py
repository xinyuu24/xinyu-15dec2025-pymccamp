# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def chop(height):
    for count in range(height):
        agent.destroy(UP)
        agent.destroy(FORWARD)
        agent.collect_all()
        agent.move(UP, 1)
    agent.move(DOWN, height)
player.on_chat("ch", chop)

def stone():
    for count in range(30):
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)
player.on_chat("mine", stone)

def stone2():
    for count in range(30):
        agent.destroy(UP)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)
player.on_chat("minef", stone2)

def build():
    for count in range(31):
        agent.place(FORWARD)
        agent.move(RIGHT, 1)
player.on_chat("build", build)
