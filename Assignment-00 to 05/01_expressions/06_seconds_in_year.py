DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():

    # Get the number of seconds in a year
    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Print the result
    print(f"There are {total_seconds} seconds in a year.")

# Ensuring the script runs when executed directly
if __name__ == '__main__':
    main()


# answer: There are 31536000 seconds in a year.
