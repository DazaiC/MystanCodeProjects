"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Dazai Chen
First, init basic conditions and values for the game
Second, get into loop to update animation and check condition
Finally, break the loop
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    brick_count = graphics.get_brick_count()
    ball_x_velocity = 0
    ball_y_velocity = 0
    # Add the animation loop here!
    while True:
        # Break loop condition
        if brick_count == 0: break
        if lives == 0: break

        # Pause animation
        pause(FRAME_RATE)

        # Update paddle position
        graphics.window.add(graphics.paddle, x=graphics.paddle_update_x, y=graphics.paddle_start_y)

        # Move ball
        if ball_x_velocity != 0 and ball_y_velocity != 0:
            graphics.ball.move(ball_x_velocity, ball_y_velocity)

        if graphics.is_ball_drop:
            if not graphics.is_set_ball_spawn_velocity:
                # Set ball spawn velocity when it drops
                ball_x_velocity = graphics.get_ball_x_velocity()
                ball_y_velocity = graphics.get_ball_y_velocity()
                graphics.is_set_ball_spawn_velocity = True
                continue
            else:
                # Reverse ball's direction when it hits the edges
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width: # left/right
                    ball_x_velocity = -ball_x_velocity
                    continue
                elif graphics.ball.y <= 0 and ball_y_velocity < 0: # top
                    ball_y_velocity = -ball_y_velocity
                    continue
                elif graphics.ball.y + graphics.ball.height >= graphics.window.height: # bottom
                    graphics.reset_ball()
                    ball_x_velocity = 0
                    ball_y_velocity = 0
                    lives -= 1
                    continue

            # Reverse ball's direction when ball hits bricks or paddle
            # Use ball's corners to detect hit event
            obj_1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            if obj_1 is not None:
                if obj_1 is not graphics.paddle: # brick
                    graphics.window.remove(obj_1)
                    ball_y_velocity = -ball_y_velocity
                    brick_count -= 1
                continue

            obj_2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
            if obj_2 is not None:
                if obj_2 is not graphics.paddle: # brick
                    graphics.window.remove(obj_2)
                    ball_y_velocity = -ball_y_velocity
                    brick_count -= 1
                continue

            obj_3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
            if obj_3 is not None:
                if obj_3 is not graphics.paddle: # brick
                    graphics.window.remove(obj_3)
                    ball_y_velocity = -ball_y_velocity
                    brick_count -= 1
                else: # paddle
                    if ball_y_velocity > 0: # check ball's direction
                        ball_y_velocity = -ball_y_velocity
                continue

            obj_4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height)
            if obj_4 is not None:
                if obj_4 is not graphics.paddle: # brick
                    graphics.window.remove(obj_4)
                    ball_y_velocity = -ball_y_velocity
                    brick_count -= 1
                else: # paddle
                    if ball_y_velocity > 0: # check ball's direction
                        ball_y_velocity = -ball_y_velocity
                continue



if __name__ == '__main__':
    main()
