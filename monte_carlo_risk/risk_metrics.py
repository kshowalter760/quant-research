def max_drawdown(equity):

    peak = equity[0]
    max_dd = 0

    for value in equity:

        if value > peak:
            peak = value

        drawdown = (peak - value) / peak

        if drawdown > max_dd:
            max_dd = drawdown

    return max_dd
