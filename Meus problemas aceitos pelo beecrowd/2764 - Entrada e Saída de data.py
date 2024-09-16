while True:
    try:
        data = input().split("/")
        day, month, year = map(int, data)
        print(f"{month:02d}/{day:02d}/{year:02d}")
        print(f"{year:02d}/{month:02d}/{day:02d}")
        print(f"{day:02d}-{month:02d}-{year:02d}")
    except EOFError:
        break
