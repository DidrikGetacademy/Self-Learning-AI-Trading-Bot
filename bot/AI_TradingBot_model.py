#Håndter logikken for AI-delen, som inkluderer modellopplæring, beslutningsprosesser, og reinforcement learning (hvis aktuelt).


def simple_trading_strategy(current_price, sma_short, sma_long):
    if sma_short > sma_long: #buy signal
        return "buy"
    elif sma_short < sma_long: #sell signal
        return "sell"
    return "hold"