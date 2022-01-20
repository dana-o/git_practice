class Nerds:
  def __init__(self, name, group_rank, intellect_power):
    self.name = name
    self.group_rank = group_rank
    self.intellect_power = intellect_power
    self.has_power = False

  def __repr__(self):
    return "{name} is a nerd and has a rank of {rank} within the nerds.".format(name=self.name, rank=self.group_rank)

class MeanGirls:
  def __init__(self, name, group_rank, popularity_power):
    self.name = name
    self.group_rank = group_rank
    self.popularity_power = popularity_power
    self.has_power = True

  def __repr__(self):
    return "{name} is a mean girl and has a rank of {rank} within the mean girls.".format(name=self.name, rank=self.group_rank)

nerd1 = Nerds("Jamie", 3, True)
nerd2 = Nerds("Janessa", 2, False)

meangirl1 = MeanGirls("Jared", 1, False)
meangirl2 = MeanGirls("Tess", 3, False)

#STARTING INTERACTIONS HERE
#creatingtheplayer
player_name = input("Hey! Welcome to Clique High! What's your name?")
player_group = input("What's up, " + player_name + "! Do you think you would describe yourself as a nerd or a mean girl?")
#make sure the player inputs a valid group
player_group_case = player_group.lower()
while player_group_case != "nerd" and player_group_case != "mean girl":
    player_group_case = input("That wasn't a choice.  Try again!  Mean girl or nerd?")

if player_group_case == "nerd":
    player = Nerds(player_name, 0, 10)
    print("Your new friends are Jamie and Janessa! You're new to the clan! Since you're new here, you rank at 0 and have intellect power of 10.")

if player_group_case == "mean girl":
   player = MeanGirls(player_name, 0, 10)
   print("Your new friends are Jared and Tess! Welcome to the gang! Since you're new here, you rank at 0 and have popularity power of 10.")

#group rank up checkpoint
def rank_up(player_power):
    if player_power > 10:
        player.group_rank = 1
        return "You are now rank 1 in {clique}!".format(clique=type(player))
    if player_power > 20:
        player.group_rank = 2
        return "You are now rank 2 in {clique}!".format(clique=type(player))

#done setting up character type. start interactions here
choice1 = input("You have English first with Mr. Yule. Who do you choose to sit with? Jamie or Jared?")
if choice1.lower() == "jamie":
    if type(player) == Nerds:
        player.intellect_power += 0
        print("Jamie says: Hey, " + player_name + ". We have a project today.  Glad we're working together.")
        print("You now have {intellect_power} intellect power points.".format(intellect_power=player.intellect_power))
        print(rank_up(player.intellect_power))
    if type(player) == MeanGirls:
        player.popularity_power += 10
        print("Jamie says: Oh, hey, " + player_name + ". Didn't think you'd want to work with us nerds. Guess that means you're kinda cool...")
        print("You now have {popularity_power} popularity points.".format(popularity_power=player.popularity_power))
        print(rank_up(player.popularity_power))

