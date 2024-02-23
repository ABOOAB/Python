import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # exp = '((0?[1-9]|1[0-2])(\:([0-5][0-9]))?( AM| PM)|((0?[0-9]|1[0-9]|2[0-3])\:([0-5][0-9])))'
    try:
        if matches := re.search(
            r"^(0?[1-9]|1[0-2])(\:([0-5][0-9]))?( AM| PM) to (0?[1-9]|1[0-2])(\:([0-5][0-9]))?( AM| PM)$",
            s,
            re.IGNORECASE,
        ):
            # assign the begging time

            st_h = matches.group(1)
            st_m = matches.group(3)

            # assign the end time

            en_h = matches.group(5)
            en_m = matches.group(7)

            # standraized the mintues
            if st_m == None:
                st_m = "00"
            else:
                st_m = f"{int(st_m):02}"
            if en_m == None:
                en_m = "00"
            else:
                en_m = f"{int(en_m):02}"
            # f"{int(hr):02}
            # standarized the hours'
            if matches.group(4) == " AM" and st_h == "12":
                st_h = "00"
            else:
                st_h = f"{int(st_h):02}"
            if matches.group(4) == " PM" and st_h != "12":
                st_h = int(st_h) + 12

            if matches.group(8) == " AM" and en_h == "12":
                en_h = "00"
            else:
                en_h = f"{int(en_h):02}"
            if matches.group(8) == " PM" and en_h != "12":
                en_h = int(en_h) + 12

            return f"{st_h}:{st_m} to {en_h}:{en_m}"

        else:
            raise ValueError
    except ValueError:
        raise


if __name__ == "__main__":
    main()
