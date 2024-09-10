from turtle import Turtle


class Block(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=4, stretch_wid=1)  # Block size: 5x1 units (50x10 pixels)
        self.goto(position)

    # Check if a point (x, y) collides with this block
    def check_collision(self, x, y):
        block_x, block_y = self.position()
        block_width = 40  # Width of block (since stretch_len=a, and each unit is 10 pixels)
        block_height = 20  # Height of block (stretch_wid=1, 10 pixels)

        # Check if the (x, y) falls within the block's bounding box
        if (block_x - block_width / 2 <= x <= block_x + block_width / 2 and
                block_y - block_height / 2 <= y <= block_y + block_height / 2):
            return True
        return False


def create_blocks_uniform(num_blocks_per_row, num_rows):
    blocks = []

    screen_width = 600  # Total width of the screen
    block_width = 50  # Each block's width (stretch_len=5, so 50 pixels)
    row_spacing = 40

    # Calculate spacing and starting x position
    total_block_width = num_blocks_per_row * block_width
    space_between = (screen_width - total_block_width) / (num_blocks_per_row + 1)
    start_x = -screen_width / 2 + space_between + block_width / 2  # Start just after the left edge

    # Place blocks evenly spaced
    for row in range(num_rows):
        y_position = 380 - row * row_spacing  # Adjust y-position for each row
        for i in range(num_blocks_per_row):
            x_position = start_x + i * (block_width + space_between)
            block = Block((x_position, y_position))
            blocks.append(block)

    return blocks
