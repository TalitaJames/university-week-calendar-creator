from datetime import date, datetime, timedelta

semesterDates = () # start, end

def generate_weeks(semesterDates, stuvacDates=(), appendStr=""):
    """
    Return a list of all weeks (M-F) between the start and end date,
    excluding stuvac, break weeks

    Output format follows google csv requirements (in readme)
    """
    startDate = datetime.strptime(semesterDates[0], "%A %d %B %Y").date()
    endDate = datetime.strptime(semesterDates[1], "%A %d %B %Y").date()
    stuvacStartDate, stuvacEndDate = None, None

    if (len(stuvacDates)!= 0):
        stuvacStartDate = datetime.strptime(stuvacDates[0], "%A %d %B %Y").date()
        stuvacEndDate = datetime.strptime(stuvacDates[1], "%A %d %B %Y").date()

    tmpDate = startDate + timedelta(days=4)

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
        tmpDate = startDate + timedelta(days=4)
    return weeks

def two_dimension_array_to_csv(array, headers=[]):
    array.insert(0, headers)
    print(array)
    tmp = [",".join(x) for x in array]
    csvString = "\n".join(tmp)
    return csvString


if __name__ == "__main__":
    weeks = generate_weeks(("Monday 27 July 2026","Friday 23 October 2026"), ("Monday 21 September 2026", "Friday 25 September 2026"), appendStr="Spring")

    headers = ["Subject", "Start Date", "Start Time", "End Date", "End Time"]
    csv = two_dimension_array_to_csv(weeks, headers)

    print(csv)
    with open('output.csv', 'w') as f:
        f.write(csv)