import datetime

class Trial(object):
    """ Represents a scheduled trial and the users who have signed up for it. """

    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time
        self.mt = mt
        self.ot = ot
        self.h1 = h1
        self.h2 = h2
        self.dps = []

    def post_trial(self):
        trial_no_dps = """
        {name} on {day} at {time}
        MT: {mt}
        OT: {ot}
        H1: {h1}
        H2: {h2}
        """.format(name=self.name,
                   day=self.day,
                   time=self.time,
                   mt=self.mt,
                   ot=self.ot,
                   h1=self.h1,
                   h2=self.h2)
