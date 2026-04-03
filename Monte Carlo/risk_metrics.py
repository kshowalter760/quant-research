def max_drawdown(equity):

    peak = equity[0]
    max_dd = 0

    for value in equity:

        if value > peak:
            peak = value

        dd = (peak - value) / peak

        if dd > max_dd:
            max_dd = dd

    return max_dd

def longest_losing_streak(trades):

    longest = 0
    current = 0

    for t in trades:

        if t == -1:
            current += 1
            longest = max(longest, current)

        else:
            current = 0

    return longest

