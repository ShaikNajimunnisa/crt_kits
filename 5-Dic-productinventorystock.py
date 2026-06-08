def update_stock(stock, txns):
    for pid, qty, typ in txns:
        stock[pid] = stock.get(pid, 0) + (qty if typ == 'IN' else -qty)
        if typ == 'OUT' and stock[pid] < 0:
            stock[pid], msg = stock[pid] + qty, f"Insufficient Stock for {pid}"
    return stock