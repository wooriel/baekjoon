
def sub45(hr, min):
    alarm_min = min - 45
    # print(alarm_min)
    if alarm_min >= 0:
        return hr, alarm_min
    else:
        alarm_min += 60
        alarm_hr = hr - 1
        if alarm_hr < 0:
            alarm_hr += 24
        return alarm_hr, alarm_min

if __name__ == "__main__":
    waketime = input()
    tlst = waketime.split(" ")
    nhr, nmin = sub45(int(tlst[0]), int(tlst[1]))
    print(nhr, nmin)
    