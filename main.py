import pygame

pygame.init()
window = pygame.display.set_mode([1000, 900])
pygame.display.set_caption("Chess for 2")

font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)

timer = pygame.time.Clock()
fps = 60

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

selection = 100
turn = 0
valid_moves = []

black_bishop = pygame.image.load("Pieces/black-bishop.png")
black_bishop = pygame.image.scale(black_bishop, (70, 70))
black_king = pygame.image.load("Pieces/black-king.png")
black_king = pygame.image.scale(black_king, (70, 70))
black_knight = pygame.image.load("Pieces/black-knight.png")
black_knight = pygame.image.scale(black_knight, (70, 70))