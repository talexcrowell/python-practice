class Musician(object):
  def __init__(self, sounds):
    self.sounds = sounds
  
  def solo(self, length):
    for i in range(length):
      print(self.sounds[i % len(self.sounds)], end=' ')
    print()


class Bassist(Musician):
  def __init__(self):
    super().__init__(["Twang", "Thrumb", "Bling"])


class Guitarist(Musician):
  def __init__(self):
    super().__init__(["Boink", "Bam", "Boom"])

  def tune(self):
    print("Be with you in a moment")
    print("*Twoning, sproing, splang*")


class Drummer(Musician):
    def __init__(self):
      super().__init__(['Whack', 'Smack', 'Crash'])
    
    def count(self):
      print('One! Two! Three! Four!')
    
    def boom(self):
      print('The drummer spontaneously explodes into a fiery vortex of pure agony on stage... \n...\nTHE CROWD GOES NUTS!')


class Band(Musician):
  def __init__(self, member):
    self.members = [member]
  
  def hire(self, member):
    self.members.append(member)
  
  def fire(self, member):
    self.members.remove(member)
  
  def lineup(self):
    print('Our lineup is...')
    for i in range(len(self.members)):
      print(self.members[i])

  def show(self):
    for i in range(len(self.members)):
      if self.members[i] == roger:
        roger.count()
    for i in range(len(self.members)):
      print(self.members[i].solo(6))
    
    print('Our bassist sucks, fire him')


david = Guitarist()
michael = Bassist()
roger = Drummer()

primal_rage = Band(david)
primal_rage.hire(michael)
primal_rage.hire(roger)

primal_rage.lineup()
primal_rage.show()
primal_rage.fire(michael)
primal_rage.lineup()

        
    
    