def get_date_from_str(date_str):
    month2mm = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
        }

    dd, month, yyyy = date_str.split()

    mm = month2mm[month]
    return int(yyyy), int(dd.strip(',')), mm

date_str = raw_input('Enter a date string? ')
print get_date_from_str(date_str)
