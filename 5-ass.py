logs = [200, 200, 404, 200, 301, 500, 200, 200, 503, 200]

last_five = logs[-5:]
critical_error = 500 in logs

print("Last 5:", last_five, "| Critical Error Found:", critical_error)
logs = [200, 200, 200, 200, 200, 200]

last_five = logs[-5:]
critical_error = 500 in logs

print("Last 5:", last_five, "| Critical Error Found:", critical_error)