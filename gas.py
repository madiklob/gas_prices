import sqlite3

conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute(
    """CREATE TABLE gas (
        zip_code integer,
        street text,
        station text,
        price_per_gallon float,
        date_recorded date
    )"""
)


def insert_gas(conn, zip_code, street, station, price_per_gallon, date):
    with conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO gas VALUES (:zip_code, :street, :station, :price_per_gallon, :date)",
            {
                "zip_code": zip_code,
                "street": street,
                "station": station,
                "price_per_gallon": price_per_gallon,
                "date": date,
            },
        )


def get_price_by_zip_and_name(zip_code, station, street):
    # Might need to add date as an arg because there will be multiple records for each station
    c.execute(
        "SELECT price_per_gallon FROM gas WHERE zip_code=:zip_code and station=:station and street=street",
        {"zip_code": zip_code, "station": station, "street": street},
    )
    result = c.fetchone()  # Fetch a single row since only one price

    if result:
        return result[0]  # Return the first column value of the result
    else:
        return None  # Return None if no result is found


# ____________________________________________________________________________________________

# The following code is from another SQL project to use as an example


# def update_level(lecture, new_level):
#     with conn:
#         c.execute(
#             """UPDATE lectures SET level=:level WHERE
# 			abbr=:abbr AND hour=:hour""",
#             {"level": new_level, "abbr": lecture.abbr, "hour": lecture.hour},
#         )


# def remove_lecture(lecture):
#     with conn:
#         c.execute(
#             """DELETE FROM lectures WHERE abbr = :abbr AND
# 			level=:level AND hour=:hour""",
#             {"abbr": lecture.abbr, "level": lecture.level, "hour": lecture.hour},
#         )


# def format_list_as_lecture(lectures: list[tuple]):
#     for lect in lectures:
#         print(f"{lect[0]} {lect[1]} is at {lect[2]}:00")


# crse_1 = Lecture("CS", 210, 11)
# crse_2 = Lecture("LING", 110, 13)

# print(crse_2)

# insert_crse(crse_1)
# insert_crse(crse_2)

# courses = get_lecture_by_hour(11)
# format_list_as_lecture(courses)


# Example usage
insert_gas(conn, 92127, "Carmel Mountain Road", "Costco", 4.99, "2023-08-30")
print(get_price_by_zip_and_name(92127, "Costco", "Carmel Mountain Road"))
