import random

prob = [0.1, 0.16, 0.21, 0.3, 0.1, 0.13]
sum_prob = [prob[0]] * 6


def index_dice(prob, sum_prob):
    for i in range(1, 6):
        sum_prob[i] = sum_prob[i-1] + prob[i]
    print(sum_prob, sum(prob))


def show_index(sum_prob):
    tmp = random.random()
    for i in range(6):
        if tmp <= sum_prob[i]:
            #print(tmp, "  index is : ", i + 1)
            return i


def moto(sum_prob, prob):
    times = 1000
    dice = [0] * 6

    for i in range(times):
        dice[show_index(sum_prob)] += 1.0

    sum_dice = sum(dice)

    for i in range(6):
        dice[i] = dice[i] / sum_dice

    print(prob, "  ----   ", dice)


index_dice(prob, sum_prob)
moto(sum_prob, prob)
