from ChutesAndLadders.Game import Game


if __name__ == '__main__':
    g = Game(2)

    sim_count = 10000
    p0_wins = 0

    for i in range(sim_count):
        g.reset()
        winner = g.play_game()
        if winner == 0:
            p0_wins += 1

    print(f'p0 won {p0_wins} times, {p0_wins / sim_count * 100}%')

