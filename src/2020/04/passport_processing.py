from pathlib import Path

valid_chars = set('abcdef0123456789')
valid_eye = set(('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))


def byr(value: str):
    return 1920 <= int(value) <= 2002


def iyr(value: str):
    return 2010 <= int(value) <= 2020


def eyr(value: str):
    return 2020 <= int(value) <= 2030


def hgt(value: str):
    if 'cm' in value:
        return 150 <= int(value.split('cm')[0]) <= 193
    elif 'in' in value:
        return 59 <= int(value.split('in')[0]) <= 76
    return False


def hcl(value: str):
    if '#' in value:
        for char in value[1:]:
            if char not in valid_chars:
                return False
        return True
    return False


def ecl(value: str):
    return value in valid_eye


def pid(value: str):
    return len(value) == 9 and value.isdigit()


validate = {'byr': byr, 'iyr': iyr, 'eyr': eyr,
            'hgt': hgt, 'hcl': hcl, 'ecl': ecl, 'pid': pid}


def main(filename: str):
    with open(Path(__file__).absolute().parent / filename) as f:
        data = [line.strip().split() for line in f.readlines()]
        data.append([])
    count, container, passports, passport = 0, set(), [], {}
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for fields in data:
        if not fields:
            if container == required:
                passports.append(passport)
            passport, container = {}, set()
        else:
            for field in fields:
                key, value = field.split(":")
                if key in required:
                    container.add(key)
                    passport[key] = value
    print(f"Part 1: {len(passports)}")

    for passport in passports:
        valid = True
        for key, value in passport.items():
            if not validate[key](value):
                valid = False
                break
        count += valid
    print(f"Part 2: {count}")


if __name__ == "__main__":
    for filename in ["test.txt", "input.txt"]:
        main(filename)
