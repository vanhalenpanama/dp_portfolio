class Scheme:
    def __init__(self, Round_Number=None, Date=None, Location=None, Home_Team=None, Away_Team=None, Result=None):
        self.Round_Number = Round_Number
        self.Date = Date
        self.Location = Location
        self.Home_Team = Home_Team
        self.Away_Team = Away_Team
        self.Result = Result


class backup_table:
    def __init__(self,Date=None,Time=None,Comp=None,Round=None,Day=None,Venue=None,Result=None,GF=None,GA=None,Opponent=None,indexes=None):
        self.Date = Date
        self.Time = Time
        self.Comp = Comp
        self.Round = Round
        self.Day = Day
        self.Venue = Venue
        self.Result = Result
        self.GF = GF
        self.GA = GA
        self.Opponent = Opponent
        self.indexes = indexes

