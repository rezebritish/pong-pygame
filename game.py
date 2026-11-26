import sys, random
from ball import*
from paddle import*
from settings import*



class Game:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("Consolas", int(WIDTH / 20))

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Paddle!")
        self.clock = pygame.time.Clock()
        self.ball = Ball()
        self.player_score = 0
        self.opponent_score = 0

        self.cc_img = pygame.image.load("CC.png").convert_alpha()
        self.cc_img = pygame.transform.scale(self.cc_img, (130, 128))
        self.cc_img_left = pygame.transform.flip(self.cc_img, True, False)

        self.player = Paddle(WIDTH - 140, player_speed, self.cc_img)
        self.opponent = Paddle(10, opponent_speed, self.cc_img_left)

        self.bg = pygame.Surface((WIDTH, HEIGHT))
        for y in range(HEIGHT):
            t = y / HEIGHT
            color = (int(15 + 25 * t), int(8 + 4 * t), int(30 + 40 * t))
            pygame.draw.line(self.bg, color, (0, y), (WIDTH, y))


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def update(self):
        keys_pressed = pygame.key.get_pressed()
        self.player.move_player(keys_pressed)
        self.opponent.move_opponent(self.ball.rect)
        self.ball.update()
        self.player_score = goal_player(self.ball, self.player_score)
        self.opponent_score = goal_opponent(self.ball, self.opponent_score)
        rebound_players_racket(self.player, self.ball)
        rebound_opponent_racket(self.opponent, self.ball)


    def draw(self):
        self.screen.blit(self.bg, (0, 0))

        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(self.screen, (65, 40, 95), (WIDTH // 2 - 2, y, 4, 20))

        self.player.draw(self.screen)
        self.opponent.draw(self.screen)
        self.ball.draw(self.screen)
        player_score_text = self.font.render(str(self.player_score), True, (160, 70, 230))
        opponent_score_text = self.font.render(str(self.opponent_score), True, (170, 235, 150))
        self.screen.blit(player_score_text, player_score_text.get_rect(center=(WIDTH / 2 + 50, 80)))
        self.screen.blit(opponent_score_text, opponent_score_text.get_rect(center=(WIDTH / 2 - 50, 80)))


    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)




def goal_player(ball, player_score):
    if ball.rect.x <= 0:
        player_score += 1
        ball.rect.center = (WIDTH / 2, HEIGHT / 2)
        ball.x_speed, ball.y_speed = random.choice([-3, 3]), random.choice([-3, 3])

    return player_score


def goal_opponent(ball, opponent_score):
    if ball.rect.x >= WIDTH:
        opponent_score += 1
        ball.rect.center = (WIDTH / 2, HEIGHT / 2)
        ball.x_speed, ball.y_speed = random.choice([-3, 3]), random.choice([-3, 3])

    return opponent_score






