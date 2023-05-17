from Strategy_1 import Strategy1
from Strategy_2 import Strategy2
from Strategy_3 import Strategy3
from Strategy_4 import Strategy4
from Strategy_5 import Strategy5
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import random
import math

def find_percentage(num, lst):
    count = lst.count(num)
    percentage = count / len(lst) * 100
    return percentage


def single(player, num : int = -1):
    count = 6
    simulation = []
    if num == -1:
        person1 = player()
    else: 
        person1 = player(num)
    while len(person1._keep) < 6:
        for i in range(count):
            num = random.randint(1, 6)
            simulation.append(num)
        # print(simulation)
        person1.choose(simulation)
        count = 6-len(person1._keep)
        simulation = []
    return person1.score()




def compare(player1, player2):
    score1 = single(player1)
    # print(person1._keep)
    # print(person1.score())
    if player2 == Strategy4 or player2 == Strategy5:
        score2 = single(player2, score1)
    else:
        score2 = single(player2)
    
    if score2 > score1:
        return 2
    elif score2 == score1:
        return 0
    else:
        return 1


def probability(num, player1, player2):
    l = []
    for i in range(num):
        l.append(compare(player1, player2))
    return [find_percentage(1,l), find_percentage(2,l)]





def find_range(input):
    return (max(input), min(input))






def plot_distribution(lst, title):
    freq_dict = {}
    for i in lst:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    x = freq_dict.keys()
    y = freq_dict.values()

    plt.bar(x, y)

    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


def plot_multiple_lines(lists):
    x = range(len(lists[0]))
    for i, lst in enumerate(lists):
        plt.plot(x, lst, label=f"Line {i+1}")
    plt.title('Multiple Line Plot')
    plt.xlabel('Index')
    plt.ylabel('Percentage')
    plt.legend()
    plt.show()




# #1
# count = 6
# simulation = []
# person1 = Strategy1()
# while len(person1._keep) < 6:
#     for i in range(count):
#         num = random.randint(1, 6)
#         simulation.append(num)
#     print(simulation)
#     person1.choose(simulation)
#     count = 6-len(person1._keep)
#     simulation = []

# print(person1._keep)
# print(person1.score())




# #2
# count = 6
# simulation = []
# person2 = Strategy2()
# while len(person2._keep) < 6:
#     for i in range(count):
#         num = random.randint(1, 6)
#         simulation.append(num)
#     print(simulation)
#     person2.choose(simulation)
#     count = 6-len(person2._keep)
#     simulation = []

# print(person2._keep)
# print(person2.score())




# #3
# count = 6
# simulation = []
# person3 = Strategy3()
# while len(person3._keep) < 6:
#     for i in range(count):
#         num = random.randint(1, 6)
#         simulation.append(num)
#     print(simulation)
#     person3.choose(simulation)
#     count = 6-len(person3._keep)
#     simulation = []

# print(person3._keep)
# print(person3.score())












# #4
# score = 20
# count = 6
# simulation = []
# person4 = Strategy5()
# while len(person4._keep) < 6:
#     for i in range(count):
#         num = random.randint(1, 6)
#         simulation.append(num)
#     print(simulation)
#     person4.choose(simulation)
#     count = 6-len(person4._keep)
#     simulation = []

# print(person4._keep)
# print(person4.score())











file = open("10thousands", "w")





strategy = [Strategy2, Strategy4]
for i in range(len(strategy)):
    for j in range(len(strategy)):
        if j > i:
            # pre = []
            post = []
            postline = []
            for k in range(10):
                l = []
                each = []
                for i in range(100000):
                    l.append(compare(strategy[0], strategy[1]))
                    each.append(find_percentage(2,l))
                postline.append(each)
                print(each,file = file)
                print(each[99999])
                temp = [find_percentage(1,l), find_percentage(2,l)]
                # pre.append(temp[0])
                post.append(temp[1])
                # print(str(temp[1])+ ",",file = file)
            # print(pre)
            # print(post)
            # title = "Strategy"+str(2)+" vs Strategy"+str(4)+ ", Strategy"+str(2)+" Win"
            # plot_distribution(pre,title)
            # title = "Strategy"+str(2)+" vs Strategy"+str(4)+ ", Strategy"+str(4)+" Win"
            # plot_distribution(post,title)
            # plot_multiple_lines(postline)




























# strategy = [Strategy1, Strategy2, Strategy3, Strategy4, Strategy5]
# hundredpre = []
# hundredpost = []
# strategy_result = []

# for i in range(len(strategy)):
#     for j in range(len(strategy)):
#         if j > i:
#             pre = []
#             post = []
#             for k in range(10):
#                 temp = probability(1000000, strategy[i], strategy[j])
#                 pre.append(temp[0])
#                 post.append(temp[1])
#                 # print(temp)
#                 # print(temp[0])
#                 # print(temp[1])
#             # title = "Strategy"+str(i+1)+" vs Strategy"+str(j+1)+ ", Strategy"+str(i+1)+" Win"
#             # plot_distribution(pre,title)
#             # title = "Strategy"+str(i+1)+" vs Strategy"+str(j+1)+ ", Strategy"+str(j+1)+" Win"
#             # plot_distribution(post,title)
#             hundredpre.append(find_range(pre))
#             hundredpost.append(find_range(post))

# n1 = 0
# n2 = 0
# for i in range(len(strategy)):
#     for j in range(len(strategy)):
#         if j > i:
#             strategy_result.append(hundredpost[n1])
#             n1 +=1
#         if j < i:
#             strategy_result.append(hundredpre[n2])
#             n2 += 1
# # print(hundredpost)
# # print(hundredpre)
# # print(strategy_result)


# player1 = Strategy2()
# player2 = Strategy3()
# l = []
# for j in range(1):
#     post = []
#     for i in range(20):
#         d = i+1
#         temp = probability(d,Strategy2,Strategy3)
#         post.append(temp[1])
#     l.append(post)

# plot_multiple_lines(l)
    












# table = PrettyTable()
# table.field_names = ['', 'strategy1', 'strategy2', 'strategy3', 'strategy4', 'strategy5']



# n = 0
# for i in range(len(strategy)):
#     temp = []
#     class_ = strategy[i]()
#     class_name = type(class_).__name__
#     temp.append(class_name)
#     for j in range(1,len(strategy)+1):
#         if i == j-1:
#             temp.append(None)
#         else:
#             temp.append(strategy_result[n])
#             n+=1
#     table.add_row(temp)

# print(table)
file.close()