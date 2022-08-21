class FindBuyingMoment:
    Minutes = [1, 3, 5, 15, 30]
    Hours = [1, 3, 5, 10, 15, 20]
    Days = [1, 2, 3, 4, 5]
    Num = 1
    Interval = 0
    Dataframe_Change = 0

    def condition(self):
        if self.Dataframe_Change == 0:
            if FindBuyingMoment.Num > len(FindBuyingMoment.Days):
                FindBuyingMoment.Dataframe_Change = 1
                FindBuyingMoment.Num = 1
            else:
                FindBuyingMoment.Interval = FindBuyingMoment.Days[len(FindBuyingMoment.Days) - FindBuyingMoment.Num]
                FindBuyingMoment.Num = FindBuyingMoment.Num + 1
        if self.Dataframe_Change == 1:
            # print(FindBuyingMoment.Num)
            # print(len(FindBuyingMoment.Minutes))
            # print(input("--"))
            if FindBuyingMoment.Num > len(FindBuyingMoment.Minutes):
                self.Dataframe_Change = 1
            else:
                print(f"Num:{FindBuyingMoment.Num}")
                FindBuyingMoment.Interval = FindBuyingMoment.Minutes[len(FindBuyingMoment.Minutes) - FindBuyingMoment.Num]
                print(FindBuyingMoment.Interval)
                FindBuyingMoment.Num = FindBuyingMoment.Num + 1

fb = FindBuyingMoment()
print(fb.Interval)
fb.condition()
print(fb.Interval)
fb.condition()
print(fb.Interval)
fb.condition()
print(fb.Interval)
fb.condition()
print(fb.Interval)
print(fb.Num)
fb.condition()
print(fb.Interval)
print(fb.Num)
fb.condition()
print(fb.Interval)
fb.condition()
print(fb.Interval)