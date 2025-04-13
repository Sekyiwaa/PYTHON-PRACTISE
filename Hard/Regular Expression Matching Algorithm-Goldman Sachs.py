def is_match(input):
    S = input["S"]
    E = input["E"]
    
    dp = [[False]*(len(E)+1) for _ in range(len(S)+1)]
    
    dp[0][0] = True  # An empty string matches another empty string
    # An empty string can match a regular expression if it's composed of '*' patterns
    for j in range(1, len(E)+1):
        if E[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, len(S)+1):
        for j in range(1, len(E)+1):
            if E[j-1] == S[i-1] or E[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif E[j-1] == '*':
                if E[j-2] != S[i-1] and E[j-2] != '.':
                    dp[i][j] = dp[i][j-2]  # '*' acts as zero occurrence
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-2]  # '*' acts as multiple or zero occurrence

    return dp[len(S)][len(E)]