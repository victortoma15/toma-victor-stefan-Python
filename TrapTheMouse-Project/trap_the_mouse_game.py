import random
from collections import deque

import pygame as pg


class Hexagon:
    def __init__ (self, hex_type: int, row: int, col: int) -> None:
        """
        Constructor for the Hexagon class.
        """
        self.hex_type = hex_type
        self.row = row
        self.col = col

    def setup_surface (self, position: tuple, margin: int, texture: pg.Surface, display: pg.Surface) -> None:
        """
        Sets up the surface of the hexagon.
        """
        self.display = display
        if texture is not None:
            self.texture = texture
            texture_width = texture.get_width()
            texture_height = texture.get_height()
            self.rect = pg.Rect((position[0] + margin, position[1] + margin),
                                (texture_width - margin * 2, texture_height - margin * 2))
        else:
            self.texture = None
            self.rect = pg.Rect(0, 0, 0, 0)

    def render (self) -> None:
        """
        Draws the hexagon.
        """
        self.display.blit(self.texture, self.rect.topleft)

    def update_type (self, new_type, new_texture) -> None:
        """
        Updates the type of the hexagon.
        """
        if self.hex_type != 1:
            self.hex_type = new_type
            self.texture = pg.transform.scale(new_texture,
                                              (new_texture.get_width() * 1.2, new_texture.get_height() * 1.2))
            self.render()


class GameButton:
    def __init__ (self, x: int, y: int, scale: float, image: pg.Surface, display: pg.Surface) -> None:
        """
        Constructor for the GameButton class.
        """
        self.display = display
        scaled_width = int(image.get_width() * scale)
        scaled_height = int(image.get_height() * scale)
        self.texture = pg.transform.scale(image, (scaled_width, scaled_height))
        self.rect = self.texture.get_rect(topleft=(x, y))

    def render (self) -> None:
        """
        Draws the button.
        """
        if self.texture is not None and self.rect is not None:
            self.display.blit(self.texture, self.rect.topleft)


def spawn_blocks (matrix: list, count: int) -> list:
    """
    Places a specified number of blocks randomly on the board.
    """
    for _ in range(count):
        x, y = random.randint(1, 10), random.randint(1, 10)
        while matrix[x][y] == 3 or (x == 6 and y == 6):
            x, y = random.randint(1, 10), random.randint(1, 10)
        matrix[x][y] = 3

    return matrix


class TrapTheMouse:
    def __init__ (self) -> None:
        """
        Constructor for the TrapTheMouse class.
        """
        self.victory_message = None
        pg.init()
        self.setup_colors()
        self.configure_display()
        self.create_buttons()
        self.block_hex = pg.image.load("img/obstacle.png").convert_alpha()
        self.free_hex = pg.image.load("img/table_hex.png").convert_alpha()
        self.mouse_hex = pg.image.load("img/mouse.png").convert_alpha()
        self.exit_hex = pg.image.load("img/obstacle.png").convert_alpha()
        self.board_size = 13
        self.setup_game_board()
        self.background_img = pg.image.load("img/background.png").convert_alpha()
        self.back_button = GameButton(330, 650, 0.4, pg.image.load("img/menu.png").convert_alpha(), self.screen)
        self.game_state = 'menu'
        self.victory = None
        self.pvp_mode = False
        self.current_player = 1

    def setup_colors (self) -> None:
        """
        Sets up the colors for the game.
        """
        self.background_color = (255, 201, 13)
        self.text_color = (15, 15, 15)

    def configure_display (self) -> None:
        """
        Configures the display for the game.
        """
        pg.display.set_caption('Trap the Mouse')
        pg.display.set_caption('Trap the Mouse')
        self.screen = pg.display.set_mode((900, 900))
        self.screen.fill(self.background_color)
        pg.display.update()

    def create_buttons (self) -> None:
        """
        Creates the buttons for the game.
        """
        self.start_button = GameButton(280, 290, 0.7, pg.image.load("img/play.png").convert_alpha(),
                                       self.screen)
        self.quit_button = GameButton(360, 780, 0.3, pg.image.load("img/exit.png").convert_alpha(),
                                      self.screen)
        self.easy_button = GameButton(135, 350, 0.8, pg.image.load("img/easy.png").convert_alpha(),
                                      self.screen)
        self.medium_button = GameButton(370, 355, 0.8, pg.image.load("img/medium.png").convert_alpha(),
                                        self.screen)
        self.hard_button = GameButton(600, 355, 0.8, pg.image.load("img/hard.png").convert_alpha(),
                                      self.screen)
        self.pvp_button = GameButton(355, 530, 0.4, pg.image.load("img/pvp.png").convert_alpha(),
                                     self.screen)

    def setup_game_board (self) -> None:
        """
        Sets up the game board with hex cells and initializes their positions.
        """
        self.board = []
        matrix = self.create_initial_matrix()

        for i, row in enumerate(matrix):
            board_row = [Hexagon(cell_type, i, j) for j, cell_type in enumerate(row)]
            self.board.append(board_row)

        y_offset = 300
        for i, row in enumerate(self.board):
            x_offset = 155 if i % 2 == 0 else 130
            for hex_cell in row:
                image = self.determine_image(hex_cell.hex_type)
                if image is not None:
                    image = pg.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2))
                hex_cell.setup_surface((x_offset, y_offset), 5, image, self.screen)
                x_offset += 38 * 1.2
            y_offset += 34 * 1.2

    def create_initial_matrix (self) -> list:
        """
        Creates the initial matrix for the game board.
        """
        size = 13
        matrix = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            matrix[0][i] = matrix[size - 1][i] = matrix[i][0] = matrix[i][size - 1] = 1
        matrix = spawn_blocks(matrix, 5)
        matrix[size // 2][size // 2] = 2
        self.mouse = [size // 2, size // 2]
        return matrix

    def determine_image (self, hex_type: int) -> pg.Surface:
        """
        Determines the image to use based on the hex type.
        """
        if hex_type == 0:
            return self.free_hex
        elif hex_type == 3:
            return self.block_hex
        elif hex_type == 2:
            return self.mouse_hex
        elif hex_type == 1:
            return self.exit_hex
        else:
            print(f'Unknown hex type: {hex_type}')

        exit()

    def render_main_menu (self) -> None:
        """
        Generates the main menu screen.
        """
        self.screen.fill(self.background_color)
        self.screen.blit(self.background_img, (10, 10))
        self.start_button.render()
        self.quit_button.render()

    def render_difficulty_screen (self) -> None:
        """
        Draws the difficulty selection screen.
        """
        self.screen.fill(self.background_color)
        self.screen.blit(self.background_img, (10, 10))
        self.easy_button.render()
        self.medium_button.render()
        self.hard_button.render()
        self.pvp_button.render()

    def render_game_board (self) -> None:
        """
        Renders the game board.
        """
        self.screen.fill(self.background_color)
        self.screen.blit(self.background_img, (10, 10))
        for row in self.board:
            for hex_cell in row:
                hex_cell.render()

    def clear_and_setup_board (self) -> None:
        """
        Clears the game board and sets it up again for a new game.
        """
        self.board = []
        self.setup_game_board()

    def find_available_moves (self) -> list:
        """
        Finds the available moves for the mouse.
        """
        row, col = self.mouse
        directions = [(row - 1, col), (row - 1, col - 1), (row, col + 1),
                      (row + 1, col - 1), (row + 1, col), (row, col - 1)]
        available_moves = []
        for index, (r, c) in enumerate(directions):
            if 0 <= r < len(self.board) and 0 <= c < len(self.board[0]):
                if self.board[r][c].hex_type != 3:
                    available_moves.append(index + 1)
        return available_moves

    def move_mouse_easy_mode (self, available_moves: list) -> None:
        """
        Moves the mouse in an easy mode, choosing from available moves randomly.
        """
        row, col = self.mouse
        self.board[row][col].update_type(0, self.free_hex)

        if not available_moves:
            self.game_state = 'game_over'
            return

        move = random.choice(available_moves)
        move_mapping = {1: (-1, 0), 2: (-1, -1), 3: (0, 1), 4: (1, -1), 5: (1, 0), 6: (0, -1)}
        move_row, move_col = move_mapping[move]

        new_row, new_col = row + move_row, col + move_col
        self.mouse = [new_row, new_col]
        self.board[new_row][new_col].update_type(2, self.mouse_hex)

    def move_mouse_medium_mode (self, available_moves: list) -> None:
        """
        Moves the mouse in a medium mode, choosing from available moves randomly but with a higher probability to move towards the edge.
        """
        row, col = self.mouse
        self.board[row][col].update_type(0, self.free_hex)

        if not available_moves:
            self.game_state = 'game_over'
            return

        move_mapping = {1: (-1, 0), 2: (-1, -1), 3: (0, 1), 4: (1, -1), 5: (1, 0), 6: (0, -1)}
        edge_moves = []

        for move in available_moves:
            move_row, move_col = move_mapping[move]
            new_row, new_col = row + move_row, col + move_col
            if new_row == 0 or new_row == len(self.board) - 1 or new_col == 0 or new_col == len(self.board[0]) - 1:
                edge_moves.append(move)

        if edge_moves:
            move = random.choice(edge_moves)
        else:
            move = random.choice(available_moves)

        move_row, move_col = move_mapping[move]
        new_row, new_col = row + move_row, col + move_col
        self.mouse = [new_row, new_col]
        self.board[new_row][new_col].update_type(2, self.mouse_hex)

    def bfs_pathfinding (self, matrix: list, start: tuple) -> tuple:
        """
        Finds the shortest path to the edge using the BFS algorithm.
        """
        queue = deque([start])
        visited = {start}

        while queue:
            current = queue.popleft()
            x, y = current

            for dx, dy in [(-1, 0), (-1, -1), (0, -1), (0, 1), (1, 0), (1, -1)]:
                next_x, next_y = x + dx, y + dy
                if (0 <= next_x < len(matrix) and 0 <= next_y < len(matrix) and
                        matrix[next_x][next_y] != '3' and (next_x, next_y) not in visited):
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))

        return start

    def move_mouse_difficult_mode (self) -> None:
        """
        Moves the mouse in a difficult mode, using the BFS algorithm to find the shortest path to the edge.
        """
        board_state = [''.join([str(hex_cell.hex_type) for hex_cell in row]) for row in self.board]
        new_position = self.bfs_pathfinding(board_state, tuple(self.mouse))

        if new_position != tuple(self.mouse):
            self.update_mouse_position(new_position)
        else:
            self.try_alternative_move()

    def try_alternative_move (self):
        """
        Tries to move the mouse in a random direction if the BFS algorithm fails to find a path.
        """
        available_moves = self.find_available_moves()
        if not available_moves:
            self.game_state = 'win_screen'
            return

        move_mapping = {1: (-1, 0), 2: (-1, -1), 3: (0, 1), 4: (1, -1), 5: (1, 0), 6: (0, -1)}
        shuffled_moves = available_moves[:]
        random.shuffle(shuffled_moves)

        for move in shuffled_moves:
            move_row, move_col = move_mapping[move]
            new_row, new_col = self.mouse[0] + move_row, self.mouse[1] + move_col
            if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size and self.board[new_row][
                new_col].hex_type != 3:
                self.update_mouse_position((new_row, new_col))
                return

    def is_adjacent (self, x: int, y: int) -> bool:
        """
        Checks if the given position is adjacent to the mouse.
        """
        row, col = self.mouse
        return abs(row - x) <= 1 and abs(col - y) <= 1

    def update_mouse_position (self, new_position: tuple) -> None:
        """
        Updates the position of the mouse.
        """
        old_x, old_y = self.mouse
        new_x, new_y = new_position

        if 0 <= new_x < self.board_size and 0 <= new_y < self.board_size and self.board[new_x][new_y].hex_type != 3:
            self.board[old_x][old_y].update_type(0, self.free_hex)
            self.board[new_x][new_y].update_type(2, self.mouse_hex)
            self.mouse = [new_x, new_y]

    def is_mouse_victorious (self) -> bool:
        """
        Checks if the mouse has reached an edge hexagon and won the game.
        """

        row, col = self.mouse
        return row == 0 or row == len(self.board) - 1 or col == 0 or col == len(self.board[0]) - 1

    def render_victory_screen (self, message: str) -> None:
        """
        Renders the victory screen with the provided message.
        """
        self.screen.fill(self.background_color)
        self.screen.blit(self.background_img, (10, 10))

        font = pg.font.Font(None, 70)
        message_surface = font.render(message, True, self.text_color)
        message_position = message_surface.get_rect(centerx=self.screen.get_width() // 2,
                                                    centery=self.screen.get_height() // 2)
        self.screen.blit(message_surface, message_position)
        self.back_button.render()

    def run_game_loop (self) -> None:
        """
        Runs the main game loop with modified structure and logic.
        """
        self.render_main_menu()
        game_clock = pg.time.Clock()
        game_state = 'menu'
        update_screen = False
        game_difficulty = 'easy'
        current_player = 1

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    game_state, update_screen, game_difficulty, current_player = self.handle_events(
                        event, game_state, game_difficulty, current_player)

            available_moves = self.find_available_moves()
            if not available_moves:
                if self.is_mouse_victorious():
                    game_state = 'game_over'
                else:
                    game_state = 'win_screen'
                update_screen = True
            if game_state == 'playing':
                row, col = self.mouse
                if row == 0 or row == len(self.board) - 1 or col == 0 or col == len(self.board[0]) - 1:
                    game_state = 'game_over'
                    update_screen = True
                elif not self.find_available_moves():
                    if self.is_mouse_victorious():
                        game_state = 'game_over'
            if update_screen:
                self.update_game_screen(game_state)
                update_screen = False

            pg.display.update()
            game_clock.tick(60)

    def handle_events (self, event, game_state, game_difficulty, current_player):
        """
        Handles events based on the game state.
        """
        if game_state == 'menu':
            if self.quit_button.rect.collidepoint(event.pos):
                exit()
            elif self.start_button.rect.collidepoint(event.pos):
                return 'difficulty_selection', True, game_difficulty, current_player

        elif game_state == 'difficulty_selection':
            if self.easy_button.rect.collidepoint(event.pos):
                return 'playing', True, 'easy', 1
            elif self.medium_button.rect.collidepoint(event.pos):
                return 'playing', True, 'medium', 1
            elif self.hard_button.rect.collidepoint(event.pos):
                return 'playing', True, 'hard', 1
            elif self.pvp_button.rect.collidepoint(event.pos):
                self.pvp_mode = True
                return 'playing', True, 'pvp', 1

        elif game_state == 'playing':
            hex_found = False

            for i, row in enumerate(self.board):
                for j, hex_cell in enumerate(row):
                    if hex_cell.rect.collidepoint(event.pos):
                        if self.pvp_mode:
                            if self.current_player == 1 and hex_cell.hex_type == 0:
                                hex_cell.update_type(3, self.block_hex)
                                hex_found = True
                            elif self.current_player == 2 and (
                                    hex_cell.hex_type == 0 or hex_cell.hex_type == 1) and self.is_adjacent(i, j):
                                self.update_mouse_position((i, j))
                                hex_found = True
                                if hex_cell.hex_type == 1:
                                    self.game_state = 'game_over'
                                    self.victory_message = "The mouse player won!"
                                    return game_state, True, game_difficulty, current_player
                        else:
                            if hex_cell.hex_type == 0:
                                hex_cell.update_type(3, self.block_hex)
                                hex_found = True
                        break
                if hex_found:
                    break
            if not self.find_available_moves():
                self.game_state = 'game_over'
                self.victory_message = "The mouse-trapper won!"
                return game_state, True, game_difficulty, current_player
            if hex_found:
                if self.pvp_mode:
                    self.current_player = 1 if self.current_player == 2 else 2
                else:
                    available_moves = self.find_available_moves()
                    if game_difficulty == 'easy':
                        self.move_mouse_easy_mode(available_moves)
                    elif game_difficulty == 'medium':
                        self.move_mouse_medium_mode(available_moves)
                    elif game_difficulty == 'hard':
                        self.move_mouse_difficult_mode()

            if not self.find_available_moves():
                if self.is_mouse_victorious():
                    return 'game_over', True, game_difficulty, current_player
                else:
                    return 'win_screen', True, game_difficulty, current_player

        elif game_state == 'win_screen':
            if self.back_button.rect.collidepoint(event.pos):
                self.reset_game()
                return 'menu', True, game_difficulty, current_player

        elif game_state == 'game_over':
            if self.back_button.rect.collidepoint(event.pos):
                self.reset_game()
                return 'menu', True, game_difficulty, current_player

        return game_state, False, game_difficulty, current_player

    def update_game_screen (self, game_state):
        """
        Updates the game screen based on the current state.
        """
        if game_state == 'menu':
            self.render_main_menu()
        elif game_state == 'difficulty_selection':
            self.render_difficulty_screen()
        elif game_state == 'playing':
            self.render_game_board()
        elif game_state == 'game_over':
            self.render_game_over_screen("You lost! The mouse escaped!")
        elif game_state == 'win_screen':
            self.render_victory_screen("You won! You trapped the mouse!")

    def reset_game (self):
        """
        Resets the game state.
        """
        self.clear_and_setup_board()
        self.game_state = 'menu'
        self.victory = None
        self.pvp_mode = False

    def render_game_over_screen (self, message):
        """
        Renders the game over screen with the provided message.
        """
        self.screen.fill(self.background_color)
        self.screen.blit(self.background_img, (10, 10))

        font = pg.font.Font(None, 70)
        message_surface = font.render(message, True, self.text_color)
        message_position = message_surface.get_rect(centerx=self.screen.get_width() // 2,
                                                    centery=self.screen.get_height() // 2)
        self.screen.blit(message_surface, message_position)
        self.back_button.render()


if __name__ == '__main__':
    game_instance = TrapTheMouse()
    game_instance.run_game_loop()
