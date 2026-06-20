try:
    result = 1 / 0
except Exception:
    return 'Stop'

finally:
    print('stop in error')
    