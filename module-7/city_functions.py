# ---------------------------------------------------------------
# Author:       Zak Nizam
# Date:         02/05/2026
# Course:       CSD325 - Advanced Python
# Assignment:   Module 7.2 – Test Cases
#
# Purpose:
#   Defines the city_country function, which formats city and
#   country information with optional population and language
#   values. Also demonstrates function usage with sample calls.
# ---------------------------------------------------------------


def city_country(city, country, population=None, language=None):
    """Return City, Country with optional population and language."""
    city = str(city).strip()
    country = str(country).strip()

    result = f"{city.title()}, {country.title()}"

    if population is not None:
        result += f" - population {int(population)}"

    if language is not None:
        result += f", {str(language).strip().title()}"

    return result


if __name__ == "__main__":
    # One with City, Country
    print(city_country("santiago", "chile"))

    # One with City, Country, Population
    print(city_country("tokyo", "japan", 13960000))

    # One with City, Country, Population, Language
    print(city_country("mexico city", "mexico", 9200000, "spanish"))