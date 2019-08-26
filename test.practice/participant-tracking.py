import predCode

class BeliefID:  # this is a class object

    def __init__(self, id, first, last, diagnosis):  # method initment
        self.id = id  # instance variables, aka attributes
        self.first = first  # instance variables, aka attributes
        self.last = last  # take instance as 1st argument SELF.etc
        self.diagnosis = diagnosis
        # self.dob = dob
        # self.handedness = handedness
        # self.gender = gender
        # self.phone = phone
        # self.voicemail = voicemail
        # self.text = text
        # self.email = email
        # self.diagnosis = diagnosis
        # self.onset = onset
        # self.drugs = drugs
        # self.screendate = screendate

    def fullname(self):  # this is a method
        return '{} {}'.format(self.first, self.last)

    @property
    def diagnosis(self):
        return '{}'.format(self.diagnosis)

    # @diagnosis.setter
    # def diagnosis(self, diagnosis):
    #     self.diagnosis = diagnosis

# class PredictiveCoding(BeliefID):
#
#     def __init__(self):
#
#         super().__init__(id, first, last)
#         self.predcodeid = predcodeid







M042300 = BeliefID('000001', 'None', 'None')

M042300.diagnosis("Psychic")

# print(M042300.fullname())
