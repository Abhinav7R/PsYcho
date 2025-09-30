import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1700, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stroop Test - Instructions")

# Colors
background_color = (0, 0, 0)  # Black background
text_color = (255, 255, 255)  # White text
highlight_color = (255, 255, 0)  # Yellow for emphasis

# Font settings
FONT = pygame.font.Font(None, 80)
SMALL_FONT = pygame.font.Font(None, 60)

# Colors for examples
RED_COLOR = (255, 0, 0)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
YELLOW_COLOR = (255, 255, 0)

# Color mapping for tags
COLOR_MAP = {
    'red': RED_COLOR,
    'blue': BLUE_COLOR,
    'green': GREEN_COLOR,
    'yellow': YELLOW_COLOR,
    'white': text_color,
    'highlight': highlight_color
}

def parse_colored_text(text):
    """Parse text with color tags like <blue>word</blue> and return list of (text, color) tuples"""
    import re
    
    # Find all color tags
    pattern = r'<(\w+)>(.*?)</\1>'
    
    segments = []
    last_end = 0
    
    for match in re.finditer(pattern, text):
        # Add text before the tag (if any)
        if match.start() > last_end:
            plain_text = text[last_end:match.start()]
            if plain_text:
                segments.append((plain_text, text_color))
        
        # Add the colored text
        color_name = match.group(1).lower()
        colored_text = match.group(2)
        color = COLOR_MAP.get(color_name, text_color)
        segments.append((colored_text, color))
        
        last_end = match.end()
    
    # Add remaining text after last tag
    if last_end < len(text):
        remaining_text = text[last_end:]
        if remaining_text:
            segments.append((remaining_text, text_color))
    
    return segments if segments else [(text, text_color)]

def display_colored_text_until_space(text, default_color=None, font=None):
    """Display text with color tags until space key is pressed"""
    if font is None:
        font = FONT
    if default_color is None:
        default_color = text_color
    
    screen.fill(background_color)
    
    # Split text into lines
    lines = text.split('\n')
    total_height = len(lines) * font.get_height()
    start_y = (HEIGHT - total_height) // 2
    
    for line_idx, line in enumerate(lines):
        line_y = start_y + line_idx * font.get_height()
        
        # Parse the line for color tags
        segments = parse_colored_text(line)
        
        # Calculate total width to center the line
        total_width = sum(font.size(segment[0])[0] for segment in segments)
        start_x = (WIDTH - total_width) // 2
        
        # Render each segment
        current_x = start_x
        for text_segment, color in segments:
            if text_segment.strip():  # Only render non-empty segments
                text_surface = font.render(text_segment, True, color)
                screen.blit(text_surface, (current_x, line_y))
                current_x += text_surface.get_width()
    
    # Add instruction at bottom
    instruction_text = "Press SPACE to continue"
    instruction_surface = SMALL_FONT.render(instruction_text, True, (128, 128, 128))
    instruction_rect = instruction_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(instruction_surface, instruction_rect)
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
    """Display text with a specific word in a different color"""
    screen.fill(background_color)
    
    # Calculate total lines and starting position
    all_lines = lines_before + [word] + lines_after
    total_height = len(all_lines) * FONT.get_height()
    start_y = (HEIGHT - total_height) // 2
    
    # Display lines before the colored word
    for i, line in enumerate(lines_before):
        text_surface = FONT.render(line, True, main_color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * FONT.get_height()))
        screen.blit(text_surface, text_rect)
    
    # Display the colored word
    word_y = start_y + len(lines_before) * FONT.get_height()
    word_surface = FONT.render(word, True, word_color)
    word_rect = word_surface.get_rect(center=(WIDTH // 2, word_y))
    screen.blit(word_surface, word_rect)
    
    # Display lines after the colored word
    for i, line in enumerate(lines_after):
        line_y = word_y + (i + 1) * FONT.get_height()
        text_surface = FONT.render(line, True, main_color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, line_y))
        screen.blit(text_surface, text_rect)
    
    # Add instruction at bottom
    instruction_text = "Press SPACE to continue"
    instruction_surface = SMALL_FONT.render(instruction_text, True, (128, 128, 128))
    instruction_rect = instruction_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(instruction_surface, instruction_rect)
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

def display_text_until_space(text, color, font=None):
    """Display text until space key is pressed"""
    if font is None:
        font = FONT
    
    screen.fill(background_color)
    
    # Handle multi-line text
    lines = text.split('\n')
    total_height = len(lines) * font.get_height()
    start_y = (HEIGHT - total_height) // 2
    
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * font.get_height()))
        screen.blit(text_surface, text_rect)
    
    # Add instruction at bottom
    instruction_text = "Press SPACE to continue"
    instruction_surface = SMALL_FONT.render(instruction_text, True, (128, 128, 128))
    instruction_rect = instruction_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(instruction_surface, instruction_rect)
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
    """Display text until space key is pressed"""
    if font is None:
        font = FONT
    
    screen.fill(background_color)
    
    # Handle multi-line text
    lines = text.split('\n')
    total_height = len(lines) * font.get_height()
    start_y = (HEIGHT - total_height) // 2
    
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, start_y + i * font.get_height()))
        screen.blit(text_surface, text_rect)
    
    # Add instruction at bottom
    instruction_text = "Press SPACE to continue"
    instruction_surface = SMALL_FONT.render(instruction_text, True, (128, 128, 128))
    instruction_rect = instruction_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(instruction_surface, instruction_rect)
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

def welcome_screen():
    """Display welcome screen"""
    welcome_text = """Welcome to the Stroop Test!
    Just follow the instructions and enjoy the game.
"""
    
    display_text_until_space(welcome_text, text_color)

def instruction_slide_1():
    """First instruction slide - Overview"""
    instruction_text = """How the Test Works:
    
You will see words displayed on the screen.
but they may appear in different colors.
"""
    
    display_text_until_space(instruction_text, text_color)

def instruction_slide_2():
    """Second instruction slide - Word Task"""
    instruction_text = """Word Task:
    
When you see "Say the WORD"
you should say the WORD you see,
regardless of what color it appears in.

For example:
If you see the word <blue>RED</blue> (in blue color),
you should say "RED"."""
    
    display_colored_text_until_space(instruction_text, text_color)


def instruction_slide_3():
    """Third instruction slide - Color Task"""
    instruction_text = """Color Task:
    
When you see "Say the COLOR"
you should say the COLOR the word appears in,
regardless of what the word says.

For example:
If you see the word <blue>RED</blue> in blue color,
you should say "BLUE"."""
    
    display_colored_text_until_space(instruction_text, text_color)


def run_instructions():
    """Run all instruction slides in sequence"""
    welcome_screen()
    instruction_slide_1()
    instruction_slide_2()
    instruction_slide_3()
    
    # Final confirmation
    final_text = "Press SPACE to start the experiment!"
    display_text_until_space(final_text, highlight_color)

def main():
    """Main function to test the instruction slides"""
    try:
        run_instructions()
        
        # Show completion message
        completion_text = """Instructions Complete!
        
This is where the actual experiment
would begin in the main program."""
        display_text_until_space(completion_text, text_color)
        
    except KeyboardInterrupt:
        print("Test interrupted by user")
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()