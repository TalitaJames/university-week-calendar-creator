from datetime import date, datetime, timedelta

semesterDates = () # start, end

def generate_weeks(semesterDates, stuvacDates=(), appendStr=""):
    """
    Return a list of all weeks (M-F) between the start and end date,
    excluding stuvac, break weeks

    Output format follows google csv requirements (in readme)
    """
    startDate = datetime.strptime(semesterDates[0], "%A %d %B %Y").date()
    # adding one day means it "ends" on the saturday (google counts end day as the end not as last day)
    endDate = datetime.strptime(semesterDates[1], "%A %d %B %Y").date() + timedelta(days=1)
    stuvacStartDate, stuvacEndDate = None, None

    if (len(stuvacDates)!= 0):
        stuvacStartDate = datetime.strptime(stuvacDates[0], "%A %d %B %Y").date()
        stuvacEndDate = datetime.strptime(stuvacDates[1], "%A %d %B %Y").date()

    tmpDate = startDate + timedelta(days=5)

    weeks = []
    weekCount = 1
    name = ""
    formatOut = "%m/%d/%Y"

    while tmpDate <= endDate:
        if startDate != stuvacStartDate:
            name = f"Week {weekCount}"
            weekCount += 1
        else:
            name = "Stuvac"


        weeks.append([name+" "+appendStr, startDate.strftime(formatOut), "",  tmpDate.strftime(formatOut)])

        startDate +=  timedelta(days=7)
        tmpDate = startDate + timedelta(days=5)
    return weeks


def two_dimension_array_to_csv(array, headers=[]):
    array.insert(0, headers)
    tmp = [",".join(x) for x in array]
    csvString = "\n".join(tmp)
    return csvString


if __name__ == "__main__":
    weeksAUT = generate_weeks(("Monday 16 February 2026","Friday 15 May 2026"), ("Monday 6 April 2026", "Friday 10 April 2026"), appendStr="Autumn")
    weeksSPR = generate_weeks(("Monday 27 July 2026","Friday 23 October 2026"), ("Monday 21 September 2026", "Friday 25 September 2026"), appendStr="Spring")
    weeksSUM = generate_weeks(("Monday 30 November 2026","Friday 12 February 2027"), ("Monday 28 December 2026", "Friday 1 January 2027"), appendStr="Summer")

    weeks = weeksAUT + weeksSPR + weeksSUM
    headers = ["Subject", "Start Date", "Start Time", "End Date", "End Time"]
    csv = two_dimension_array_to_csv(weeks, headers)

    with open('output.csv', 'w') as f:
        f.write(csv)