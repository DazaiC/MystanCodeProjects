"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle_start_x = (window_width - paddle_width) / 2
        self.paddle_start_y = window_height - paddle_height - paddle_offset
        self.paddle.filled = True
        self.window.add(self.paddle, x=self.paddle_start_x, y=self.paddle_start_y)
        self.paddle_update_x = self.paddle_start_x
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball_start_x = (window_width - ball_radius*2)/2
        self.ball_start_y = (window_height - ball_radius*2)/2
        self.ball.filled = True
        self.window.add(self.ball, x=self.ball_start_x, y=self.ball_start_y)
        # Default initial velocity for the ball
        self.__ball_dx = 0
        self.__ball_dy = 0
        self.is_ball_drop = False
        self.is_set_ball_spawn_velocity = False
        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        onmousemoved(self.handle_move)
        # Draw bricks
        self.brick_count = brick_cols*brick_rows
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if i < 2: brick.fill_color = 'red'
                elif i < 4: brick.fill_color = 'orange'
                elif i < 6: brick.fill_color = 'yellow'
                elif i < 8: brick.fill_color = 'green'
                elif i < 10: brick.fill_color = 'blue'
                self.window.add(brick, x=j*(brick_spacing+brick_width), y=brick_offset+i*(brick_spacing+brick_height))



    def handle_click(self, mouse):
        if self.is_ball_drop is False: # Use is_ball_drop as a switch
            self.__ball_dy = INITIAL_Y_SPEED
            self.__ball_dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5: self.__ball_dx = -self.__ball_dx
            self.is_ball_drop = True


    def handle_move(self, mouse):
        mouse_offset_left_x = mouse.x - self.paddle.width/2
        mouse_offset_right_x = mouse.x + self.paddle.width/2
        if mouse_offset_left_x <= 0:
            self.paddle_update_x = 0
        elif mouse_offset_right_x >= self.window.width:
            self.paddle_update_x = self.window.width - self.paddle.width
        else:
            self.paddle_update_x = mouse_offset_left_x


    def reset_ball(self):
        # Reset the switch
        self.is_ball_drop = False
        self.is_set_ball_spawn_velocity = False
        # set ball velocity to 0
        self.__ball_dx = 0
        self.__ball_dy = 0
        # Reset ball position to start point
        self.ball.x = self.ball_start_x
        self.ball.y = self.ball_start_y


    def get_ball_x_velocity(self):
        return self.__ball_dx


    def get_ball_y_velocity(self):
        return self.__ball_dy


    def get_brick_count(self):
        return self.brick_count

