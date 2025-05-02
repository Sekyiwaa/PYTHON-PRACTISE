def count_friends(user_ids):
    friend_count = {}
    for row in user_ids:
        for user_id in row:
            if user_id not in friend_count:
                friend_count[user_id] = 0
            friend_count[user_id] += 1
    return friend_count