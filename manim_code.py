from manim import *
from manim_rubikscube import *
import magiccube

def update_state_file(state):
    with open("state.txt", "w") as text_file:
        text_file.write(state)

def get_state_from_file():
    with open("state.txt","r") as f:
        state = f.read()
    if not state:
        return 'YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW' # The standard setup
    return state

def get_state(magic_cube):
    cleaned_data = str(magic_cube).replace(" ", "").replace("\n", "")

    # Face order: Top (W), Front (R), Right (B), Back (O), Left (G), Bottom (Y)
    top = cleaned_data[:9]
    middle = cleaned_data[9:45]
    bottom = cleaned_data[45:]

    front_index = [0, 1, 2, 12, 13, 14, 24, 25, 26]
    front = ''
    right = ''
    back = ''
    left = ''
    for index in front_index:
        front += middle[index]  # Front face
        right += middle[index+3]
        back += middle[index+6]
        left += middle[index+9]

    result = top + front + right + back + left + bottom
    return result

def convert_state(before_state):
    # magiccube and manim rubikscube use different notation, this converts the magic one into the manim one
    # manim rubiks cube also uses an order of U R F D L B which is different from the U L F R B D that magic uses
    print(before_state)
    after_state = ''
    for notation in before_state:
        if notation == 'Y':
            after_state += 'U'
        elif notation == 'G':
            after_state += 'F'
        elif notation == 'O':
            after_state += 'R'
        elif notation == 'B':
            after_state += 'B'
        elif notation == 'R':
            after_state += 'L'
        elif notation == 'W':
            after_state += 'D'
    
    after_state = after_state[:9] + after_state[27:36] + after_state[18:27] + after_state[45:] + after_state[9:18] + after_state[36:45]
    return after_state

def get_camera_orientation():
    with open('camera_orientation.txt', "r") as file:
        content = file.read().strip()

    values = content.split(",")

    tuple_values = tuple(int(val.strip()) for val in values)

    before_camera_change = (
        tuple_values[0] * DEGREES,
        tuple_values[1] * DEGREES,
        tuple_values[2] * DEGREES
    )

    after_camera_change = (
        tuple_values[3] * DEGREES,
        tuple_values[4] * DEGREES,
        tuple_values[5] * DEGREES
    )

    return before_camera_change, after_camera_change

class Turn(ThreeDScene):
    def construct(self):
        cube = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6).move_to(ORIGIN)
        state_from_file = get_state_from_file()
        cube.set_state(convert_state(state_from_file))
        magic_cube = magiccube.Cube(3, state_from_file)
        self.add(cube)

        with open("move.txt","r") as f:
            move = f.read()
        before_camera_change, after_camera_change = get_camera_orientation()
        self.set_camera_orientation(phi=after_camera_change[0], theta=after_camera_change[1], gamma=after_camera_change[2], distance=8)

        self.play(CubeMove(cube, move))
        magic_cube.rotate(move)

        state = get_state(magic_cube)
        update_state_file(state)
        self.wait(8)

class Show(ThreeDScene):
    def construct(self):
        cube = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6).move_to(ORIGIN)
        state_from_file = get_state_from_file()
        cube.set_state(convert_state(state_from_file))
        self.add(cube)
        
        before_camera_change, after_camera_change = get_camera_orientation()
        self.set_camera_orientation(phi=after_camera_change[0], theta=after_camera_change[1], gamma=after_camera_change[2], distance=8)

class Rotate(ThreeDScene):
    def construct(self):
        cube = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6).move_to(ORIGIN)
        state_from_file = get_state_from_file()
        cube.set_state(convert_state(state_from_file))
        self.add(cube)
        self.renderer.camera.frame_center = cube.get_center()
        before_camera_change, after_camera_change = get_camera_orientation()
        self.set_camera_orientation(phi=before_camera_change[0], theta=before_camera_change[1], gamma=before_camera_change[2], distance=8)
        self.move_camera(phi=after_camera_change[0], theta=after_camera_change[1], gamma=after_camera_change[2], distance=8)

        self.wait(8)
        