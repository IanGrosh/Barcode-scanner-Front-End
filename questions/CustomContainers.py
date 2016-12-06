from questions.models import Location,Device,Question,Choice


class Modleiter(object):
    def __getitem__(self, item):
        if item >= len(self.things):
            raise IndexError("CustomRange index out of range")
        return self.things[item]

    def __len__(self):
        return len(self.things)
    @property
    def yes(self):
        count = 0
        for i in self.things:
            if  i.__nonzero__():
                count+=1
        return count
    @property
    def no(self):
        count = 0
        for i in self.things:
            if not i.__nonzero__():
                count+=1
        return count

class UserFactory(Modleiter):
    def __init__(self,supervisor=None):
        self.meow = 0
        self.locations = Location.objects.all()
        print(self.locations)
        self.names = set([loc.user_assigned for loc in self.locations])
        self.things = []
        for name in sorted(self.names):
        	self.things.append(User(name))


class User(Modleiter):
    def __init__(self,name):
        self.name=name
        self.things = Location.objects.filter(user_assigned=name)


class StatDeviceFactory(Modleiter):
    def __init__(self,locID):
        self.location = Location.objects.get(id=locID)
        self.ansers = Choice.objects.filter(location=self.location)
        self.things = []
        for dev in self.location.devices:
            self.things.append(StatDevice(dev,self.ansers))
    def __nonzero__(self):
        out = True
        for i in self.things:
            out &= i.__nonzero__()
        return out        

class StatDevice(Modleiter):
    def __init__(self,device,ansers):
        self.device = device
        self.questions = self.device.questions
        self.things = []
        for q in self.questions:
            c = Choice.objects.filter(question=q).order_by('-time_scanned')
            thing = Responce(q,c)
            self.things.append(thing)
    def __nonzero__(self):
        out = True
        for i in self.things:
            out &= i.__nonzero__()
        return out

class Responce(Modleiter):
    def __init__(self,question,ansers):
        self.question = question
        self.ansers = ansers
    def __nonzero__(self):
        try:
            if self.ansers[0].choice_text == "yes":
                return True
            else:
                return False
        except IndexError:
            return False
