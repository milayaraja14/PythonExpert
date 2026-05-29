    import datetime
    
    # --- 1. Getting Current Date and Time ---
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now}")
    print(f"Current Year: {now.year}")
    print(f"Current Month: {now.month}")
    
    # --- 2. Creating a Specific Date ---
    # Syntax: datetime.datetime(year, month, day, hour, minute, second)
    target_date = datetime.datetime(2025, 1, 1, 12, 0, 0)
    print(f"Target Date: {target_date}")
    
    # --- 3. Formatting Dates (strftime) ---
    # %Y = Year, %m = Month, %d = Day, %H = Hour, %M = Minute
    readable_date = now.strftime("%B %d, %Y")
    print(f"Formated Date: {readable_date}")
    
    # --- 4. Converting String to Date (strptime) ---
    date_string = "25 December, 2023"
    parsed_date = datetime.datetime.strptime(date_string, "%d %B, %Y")
    print(f"Parsed Object: {parsed_date}")
    
    # --- 5. Using Timedelta for Calculations ---
    # Let's find out what the date will be in 10 days
    today = datetime.date.today()
    ten_days_later = today + datetime.timedelta(days=10)
    print(f"Date in 10 days: {ten_days_later}")
    
    # Calculate difference between two dates
    diff = target_date - now
    print(f"Days until target: {diff.days} days")
