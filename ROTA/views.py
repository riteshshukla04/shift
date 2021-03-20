from django.shortcuts import render,HttpResponse

from django.shortcuts import render, HttpResponse


def index(request):
    if request.method == "POST":

        date_time_str = request.POST['query']

        try:
            import datetime
            import calendar
            s = datetime.date(day=1, year=2020, month=1)

            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
            a = (date_time_obj.date())
            c = 0
            l = ["Morning", "Evening", "Night", "OFF", "General", "Morning", ]
            part = ["Morning", "Evening", "Night", "OFF", "Morning", "Evening", "Night"]
            group = request.POST['group']

            type = request.POST['type']
            main = []
            delta = a - s
            deltadays = delta.days

            if type == "Executive":

                d = {
                    s - datetime.timedelta(days=1): "Evening"
                }

                for i in range(deltadays):
                    m = d[s - datetime.timedelta(days=1)]
                    k = l[l.index(m) + 1]
                    d[s] = k
                    main += [k]
                    s += datetime.timedelta(days=1)

                    if k == "OFF":

                        d[s] = "General"
                        main += ["General"]
                        s += datetime.timedelta(days=1)
                    else:
                        d[s] = k
                        main += [k]
                        s += datetime.timedelta(days=1)
                k = d[a]
                pop = False
                if k == "General":
                    k = "OFF"
                    pop = True
                if group == "A":
                    s = k
                    if pop:
                        s = "General"
                if group == "B":
                    s = part[part.index(k) + 1]
                if group == "C":
                    s = part[part.index(k) + 2]
                if group == "D":
                    s = part[part.index(k) + 3]

            else:

                d = {
                    s - datetime.timedelta(days=1): "General"
                }

                for i in range(deltadays):
                    if calendar.day_name[s.weekday()] == "Sunday":
                        m = d[s - datetime.timedelta(days=1)]
                        k = l[l.index(m) + 1]
                        d[s] = k
                        main += [k]

                        s += datetime.timedelta(days=1)

                        d[s] = k
                        main += [k]
                        s += datetime.timedelta(days=1)
                        if k == "OFF":

                            d[s] = "General"
                            main += ["General"]
                            s += datetime.timedelta(days=1)
                        else:
                            d[s] = k
                            main += [k]
                            s += datetime.timedelta(days=1)

                    else:
                        m = d[s - datetime.timedelta(days=1)]
                        k = l[l.index(m) + 1]
                        d[s] = k
                        main += [k]
                        s += datetime.timedelta(days=1)

                        if k == "OFF":

                            d[s] = "General"
                            main += ["General"]
                            s += datetime.timedelta(days=1)
                        else:
                            d[s] = k
                            main += [k]
                            s += datetime.timedelta(days=1)

                k = d[a]
                if k == "General":
                    k = "OFF"
                    pop = True
                if group == "A":
                    s = k

                if group == "B":
                    s = part[part.index(k) + 1]
                if group == "C":
                    s = part[part.index(k) + 2]
                if group == "D":
                    s = part[part.index(k) + 3]
                
                if s=="OFF" and date_time_obj.weekday()%2!=0:
                    s="General"
                print(date_time_str)
                u=date_time_str
                return (render(request, "home.html", {"s": s,"Hello":u}))
        except:
            s="Please Enter Date after 1st Jan 2020"
        print(date_time_str)
        u=date_time_str
        return render(request, "home.html", {"s": s,"Hello":u})


    return (render(request, "home.html"))