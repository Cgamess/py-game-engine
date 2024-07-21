import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1275, 650
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 24
LINE_SPACING = 5  # Spacing between lines
TEXT_COLOR = BLACK
BG_COLOR = WHITE

# Sample text strings
texts = [
"""
To the Jaiden haters,
""",
"""
About the mrbeast video:
""",
"""
With the controversy,
Its kinda like the  marshmellow story
And with a bit of statistics, i can say jaiden did nothing wrong
the winner of the last tordement is less likly to win twice, and less likly to be IN the next challenge,
the people closest to winning but failed are more likly to win next and be in the next game
and the next game with them could have a higher chance of a higher profit
the chance of not jaiden is not more likely then jaiden due to a bit of statistics,
and due to jaiden winning next time her scores will likly be lower in the tordement, 
increasing the odds of someone else winning
and next time has a probable chance for a larger amount of profit
so, jaiden winning now increases the chance of in the future others winning
and jaiden is less likly to contribute to the next challence bc of this
giving nick or anyone else an increased chance of winning
""",
]

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Message to the haters")

# Font initialization
font = pygame.font.SysFont("Milford Black", FONT_SIZE)

# Function to render multi-line text
def render_text(text):
    lines = text.strip().splitlines()

    # Render lines
    rendered_lines = []
    for i, line in enumerate(lines):
        rendered_line = font.render(line.strip(), True, TEXT_COLOR)
        rendered_lines.append(rendered_line)

    return rendered_lines

# Initial text index
text_index = 0

# Main loop
running = True
while running:
    screen.fill(BG_COLOR)

    # Render current text
    rendered_text = render_text(texts[text_index])
    text_height = 0
    for i, line in enumerate(rendered_text):
        screen.blit(line, (10, 10 + i * (FONT_SIZE + LINE_SPACING)))
        text_height = i * (FONT_SIZE + LINE_SPACING) + FONT_SIZE
    
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Move to the next text
                text_index = (text_index + 1) % len(texts)

# Quit Pygame
pygame.quit()
sys.exit()
