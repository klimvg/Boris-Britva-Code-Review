# ИСХОДНЫЕ ДАННЫЕ
# names of hurricanes
names = [
    "Cuba I",
    "San Felipe II Okeechobee",
    "Bahamas",
    "Cuba II",
    "CubaBrownsville",
    "Tampico",
    "Labor Day",
    "New England",
    "Carol",
    "Janet",
    "Carla",
    "Hattie",
    "Beulah",
    "Camille",
    "Edith",
    "Anita",
    "David",
    "Allen",
    "Gilbert",
    "Hugo",
    "Andrew",
    "Mitch",
    "Isabel",
    "Ivan",
    "Emily",
    "Katrina",
    "Rita",
    "Wilma",
    "Dean",
    "Felix",
    "Matthew",
    "Irma",
    "Maria",
    "Michael",
]

# months of hurricanes
months = [
    "October",
    "September",
    "September",
    "November",
    "August",
    "September",
    "September",
    "September",
    "September",
    "September",
    "September",
    "October",
    "September",
    "August",
    "September",
    "September",
    "August",
    "August",
    "September",
    "September",
    "August",
    "October",
    "September",
    "September",
    "July",
    "August",
    "September",
    "October",
    "August",
    "September",
    "October",
    "September",
    "September",
    "October",
]

# years of hurricanes
years = [
    1924,
    1928,
    1932,
    1932,
    1933,
    1933,
    1935,
    1938,
    1953,
    1955,
    1961,
    1961,
    1967,
    1969,
    1971,
    1977,
    1979,
    1980,
    1988,
    1989,
    1992,
    1998,
    2003,
    2004,
    2005,
    2005,
    2005,
    2005,
    2007,
    2007,
    2016,
    2017,
    2017,
    2018,
]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [
    165,
    160,
    160,
    175,
    160,
    160,
    185,
    160,
    160,
    175,
    175,
    160,
    160,
    175,
    160,
    175,
    175,
    190,
    185,
    160,
    175,
    180,
    165,
    165,
    160,
    175,
    180,
    185,
    175,
    175,
    165,
    180,
    175,
    160,
]

# areas affected by each hurricane
areas_affected = [
    ["Central America", "Mexico", "Cuba", "Florida", "The Bahamas"],
    ["Lesser Antilles", "The Bahamas", "United States East Coast", "Atlantic Canada"],
    ["The Bahamas", "Northeastern United States"],
    ["Lesser Antilles", "Jamaica", "Cayman Islands", "Cuba", "The Bahamas", "Bermuda"],
    ["The Bahamas", "Cuba", "Florida", "Texas", "Tamaulipas"],
    ["Jamaica", "Yucatn Peninsula"],
    ["The Bahamas", "Florida", "Georgia", "The Carolinas", "Virginia"],
    ["Southeastern United States", "Northeastern United States", "Southwestern Quebec"],
    ["Bermuda", "New England", "Atlantic Canada"],
    ["Lesser Antilles", "Central America"],
    ["Texas", "Louisiana", "Midwestern United States"],
    ["Central America"],
    ["The Caribbean", "Mexico", "Texas"],
    ["Cuba", "United States Gulf Coast"],
    ["The Caribbean", "Central America", "Mexico", "United States Gulf Coast"],
    ["Mexico"],
    ["The Caribbean", "United States East coast"],
    ["The Caribbean", "Yucatn Peninsula", "Mexico", "South Texas"],
    ["Jamaica", "Venezuela", "Central America", "Hispaniola", "Mexico"],
    ["The Caribbean", "United States East Coast"],
    ["The Bahamas", "Florida", "United States Gulf Coast"],
    ["Central America", "Yucatn Peninsula", "South Florida"],
    ["Greater Antilles", "Bahamas", "Eastern United States", "Ontario"],
    ["The Caribbean", "Venezuela", "United States Gulf Coast"],
    ["Windward Islands", "Jamaica", "Mexico", "Texas"],
    ["Bahamas", "United States Gulf Coast"],
    ["Cuba", "United States Gulf Coast"],
    ["Greater Antilles", "Central America", "Florida"],
    ["The Caribbean", "Central America"],
    ["Nicaragua", "Honduras"],
    [
        "Antilles",
        "Venezuela",
        "Colombia",
        "United States East Coast",
        "Atlantic Canada",
    ],
    [
        "Cape Verde",
        "The Caribbean",
        "British Virgin Islands",
        "U.S. Virgin Islands",
        "Cuba",
        "Florida",
    ],
    [
        "Lesser Antilles",
        "Virgin Islands",
        "Puerto Rico",
        "Dominican Republic",
        "Turks and Caicos Islands",
    ],
    ["Central America", "United States Gulf Coast (especially Florida Panhandle)"],
]

# damages (USD($)) of hurricanes
damages = [
    "Damages not recorded",
    "100M",
    "Damages not recorded",
    "40M",
    "27.9M",
    "5M",
    "Damages not recorded",
    "306M",
    "2M",
    "65.8M",
    "326M",
    "60.3M",
    "208M",
    "1.42B",
    "25.4M",
    "Damages not recorded",
    "1.54B",
    "1.24B",
    "7.1B",
    "10B",
    "26.5B",
    "6.2B",
    "5.37B",
    "23.3B",
    "1.01B",
    "125B",
    "12B",
    "29.4B",
    "1.76B",
    "720M",
    "15.1B",
    "64.8B",
    "91.6B",
    "25.1B",
]

# deaths for each hurricane
deaths = [
    90,
    4000,
    16,
    3103,
    179,
    184,
    408,
    682,
    5,
    1023,
    43,
    319,
    688,
    259,
    37,
    11,
    2068,
    269,
    318,
    107,
    65,
    19325,
    51,
    124,
    17,
    1836,
    125,
    87,
    45,
    133,
    603,
    138,
    3057,
    74,
]
# КОНЕЦ ИСХОДНЫХ ДАННЫХ


# НАДО B и M ПЕРЕВЕСТИ В ПОЛНЫЕ ЧИСЛА
# 1
# Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}

# МОЙ КОД, БЕРУ ВСЕ ЧТО ДО B и M, УМНОЖАЮ НА НУЖНОЕ ЧИСЛО, ДОБАВЛЯЮ В ЛИСТ


def newdamages(damage_list):
    fixed_damages = []
    for damage in damage_list:
        if "M" in damage:
            fixed_damages.append(float(damage[:-1]) * conversion["M"])
        elif "B" in damage:
            fixed_damages.append(float(damage[:-1]) * conversion["B"])
        elif "Damages not recorded" in damage:
            fixed_damages.append("Damages not recorded")
    return fixed_damages


# МОЙ КОД
# test function by updating damages
print(newdamages(damages))


# НАДО СОЕДИНИТЬ ИСХОДНИКИ В СЛОВАРЬ, ГДЕ КЛЮЧ - НАЗВАНИЕ УРАГАНА,
# А ВАЛЬЮ - СЛОВАРЬ С ИНФОЙ ПО УРАГАНУ
# 2
# Create a Table
# МОЙ КОД, СЧИТАЮ СКОЛЬКО УРАГАНОВ И ДЛЯ КАЖДОГО ДЕЛАЮ
def create_table(names, months, years, wind, areas, damage, deaths):
    values_fin = {}
    for i in range(len(names)):
        values = {}
        values["Name"] = names[i]
        values["Month"] = months[i]
        values["Year"] = years[i]
        values["Max Sustained Wind"] = wind[i]
        values["Areas"] = areas[i]
        values["Damage"] = damage[i]
        values["Deaths"] = deaths[i]
        values_fin[names[i]] = values
    return values_fin


# Create and view the hurricanes dictionary
# МОЙ КОД
hurricanes = create_table(
    names,
    months,
    years,
    max_sustained_winds,
    areas_affected,
    newdamages(damages),
    deaths,
)
# print(hurricanes)

# ПЕРЕВЕСТИ ПОЛУЧЕННЫЙ СЛОВАРЬ В СЛОВАРЬ ФОРМАТА {ГОД: ДАННЫЕ ПО УРАГАНУ}
# 3
# Organizing by Year
# МОЙ КОД ЧЕКАЮ ЕСТЬ ЛИ ГОД В СЛОВАРЕ, ЕСЛИ НЕТ - СОЗДАЮ, ЕСЛИ ЕСТЬ - ДОБАВЛЯЮ К СУЩЕСТВУЮЩЕМУ
def hurricane_by_year(hurricane_dict):
    years = {}
    for keys, values in hurricane_dict.items():
        if not values["Year"] in years:
            years[values["Year"]] = [values]
        else:
            years[values["Year"]] += [values]
    return years


# create a new dictionary of hurricanes with year and key
# МОЙ КОД
years = hurricane_by_year(hurricanes)
# print(years)

# 4 ПОСЧИТАТЬ СКОЛЬКО РАЗ УРАГАН ЕБАШИЛ ПО КАЖДОЙ ТЕРРИТОРИИ
# Counting Damaged Areas
# МОЙ КОД: ЧЕКАЮ, ЕСТЬ ЛИ В СЛОВАРЕ ТЕРРИТОРИЯ. ЕСЛИ НЕТ, СОЗДАЮ, А ЕСЛИ ЕСТЬ ДОБАВЛЯЮ К СУЩЕСТВУЮЩЕЙ
def area_count(hurricane_dict):
    area_counter = {}
    for keys, values in hurricane_dict.items():
        for area in values["Areas"]:
            if not area in area_counter.keys():
                area_counter[area] = 1
            else:
                area_counter[area] += 1
    return area_counter


# create dictionary of areas to store the number of hurricanes involved in
area_overall = area_count(hurricanes)
# print(area_overall)

# НАЙТИ ТЕРРИТОРИЮ, ПО КОТОРОЙ ЕБАШИЛО БОЛЬШЕ ВСЕГО И ВЫВЕСТИ, СКОЛЬКО РАЗ
# 5
# Calculating Maximum Hurricane Count
# МОЙ КОД: ПРОХОЖУСЬ ПО ПРЕДЫДУЩЕМУ СЛОВАРЮ, ЕСЛИ ВАЛЬЮ СЛЕДУЮЩЕГО БОЛЬШЕ ПРЕДЫДУЩЕГО, ПЕРЕЗАПИСЫВАЮ
def most_strikes(area_overall_dict):
    max_area = ""
    max_area_count = 0
    for key, value in area_overall_dict.items():
        if value > max_area_count:
            max_area = key
            max_area_count = value
    return print(
        max_area
        + " is affected by the most hurricanes. It was hit "
        + str(max_area_count)
        + " times."
    )


# find most frequently affected area and the number of hurricanes involved in
# most_strikes(area_overall)


# 6 НАЙТИ УРАГАН, КОТОРЫЙ УБИЛ БОЛЬШЕ ВСЕХ И ВЫВЕСТИ, СКОЛЬКО
# Calculating the Deadliest Hurricane
# МОЙ КОД: В ПРИНЦИПЕ КАК В ЗАДАЧЕ 5
def most_deaths(hurricane_dict):
    deadliest = ""
    deadliest_count = 0
    for key, value in hurricane_dict.items():
        if value["Deaths"] > deadliest_count:
            deadliest = key
            deadliest_count = value["Deaths"]
    return print(
        deadliest
        + " is the deadliest hurricane. It caused "
        + str(deadliest_count)
        + " deaths."
    )


# find highest mortality hurricane and the number of deaths
# most_deaths(hurricanes)


# СДЕЛАТЬ РЕЙТИНГ ПО СМЕРТНОСТИ
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}


# МОЙ КОД: ПРОСТО ДОХУЯ ЕСЛИ
def mortality_scaling(hurricane_dict):
    output_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, value in hurricane_dict.items():
        if value["Deaths"] <= mortality_scale[0]:
            output_mortality[0] += [value]
        elif value["Deaths"] <= mortality_scale[1]:
            output_mortality[1] += [value]
        elif value["Deaths"] <= mortality_scale[2]:
            output_mortality[2] += [value]
        elif value["Deaths"] <= mortality_scale[3]:
            output_mortality[3] += [value]
        elif value["Deaths"] <= mortality_scale[4]:
            output_mortality[4] += [value]
        else:
            output_mortality[5] += [value]
    return output_mortality


# categorize hurricanes in new dictionary with mortality severity as key
# print(mortality_scaling(hurricanes))


# ПОСЧИТАТЬ КАКОЙ УРАГАН ВЪЕБАЛ БОЛЬШЕ ДЕНЕГ
# 8 Calculating Hurricane Maximum Damage
# МОЙ КОД: В ПРИНЦИПЕ КАК 5 И 6
def most_costly(hurricane_dict):
    costliest = ""
    costliest_count = 0
    for key, value in hurricane_dict.items():
        if type(value["Damage"]) is float and value["Damage"] > costliest_count:
            costliest = key
            costliest_count = value["Damage"]
    print(
        "Hurricane "
        + costliest
        + " caused the most damage of "
        + str(costliest_count)
        + " USD."
    )


# find highest damage inducing hurricane and its total cost
# most_costly(hurricanes)


# СДЕЛАТЬ РЕЙТИНГ ПО УРОНУ БАБКАМ
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}

# МОЙ КОД: В ПРИНЦИПЕ КАК 7
def damage_scaling(hurricane_dict):
    output_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, value in hurricane_dict.items():
        if value["Damage"] == "Damages not recorded":
            output_damage[0] += [value]
        elif value["Damage"] <= damage_scale[1]:
            output_damage[1] += [value]
        elif value["Damage"] <= damage_scale[2]:
            output_damage[2] += [value]
        elif value["Damage"] <= damage_scale[3]:
            output_damage[3] += [value]
        elif value["Damage"] <= damage_scale[4]:
            output_damage[4] += [value]
        else:
            output_damage[5] += [value]
    return output_damage


# categorize hurricanes in new dictionary with damage severity as key
scaled_damage = damage_scaling(hurricanes)
print(scaled_damage)
