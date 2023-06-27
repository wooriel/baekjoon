def one_friend(p_num, f_str):
    """_summary_

    Args:
        p_num (_type_): number of people
        f_str (_type_): string denoting friend

    Return:
        f_set: set of friends
    """
    f_set = set()
    for i in range(p_num):
        if f_str[i] == 'Y':
            f_set.add(i)
        # else pass
    return f_set


def two_friend(f_list):
    two_friends = []
    for i in range(len(f_list)):
        one_friends = list(f_list[i])
        two_friend = set()
        for j in range(len(one_friends)):
            friend_friend = f_list[one_friends[j]]
            two_friend = two_friend.union(friend_friend) 
        two_friends.append(two_friend)

    return two_friends
    

if __name__ == "__main__":
    people = int(input())

    friends = []

    for i in range(people):
        friend_string = input() 
        friends.append(one_friend(people, friend_string))
    two_friends = two_friend(friends)

    max = 0
    for j in range(people):
        two_num = friends[j].union(two_friends[j]) - set([j])
        two_num_len = len(two_num)
        if max < two_num_len:
            max = two_num_len
    # print(friends)
    print(max)