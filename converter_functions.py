def feet_inches_to_meters(feet, inches):

    m_in_i = 0.0254
    total_inches = float(inches) + float(feet*12)

    return total_inches*m_in_i


def km_to_miles(km):
    return float(km) / 1.6


if __name__ == "__main__":
    print(km_to_miles(10))
