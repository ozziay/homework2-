class Besiktas:
    def __init__(self, player_name, player_position):
        self.player_name = player_name
        self.player_position = player_position
        
    def player_info(self):
        print("Hi my nanme is " + self.player_name + " and my position is " + self.player_position)

    def player_stats(self, goals, assists):
        self.goals = goals
        self.assists = assists
        print(f"{self.player_name} Stats - Goals: {goals}, Assists: {assists}")



class Besiktas_Esports(Besiktas):
        
   def esport_info_1(self):
        print("Hi my nanme is " + self.player_name + " and my position is " + self.player_position )

   def record_kda(self, kills, deaths, assists):
        self.kills = kills
        self.deaths = deaths
        self.assists = assists 
        kda = (kills + assists) / max(1, deaths)
        print(f"{self.player_name} K/D/A: {kills}/{deaths}/{assists}  ->  KDA: {kda:.2f}")




class Besiktas_Volleyball(Besiktas):
        
   def volleyball_info_2(self):
        print("Hi my nanme is " + self.player_name + " and my position is " + self.player_position )

   def record_stats(self, attacks, blocks, serves):
       self.attacks = attacks 
       self.blocks = blocks
       self.serves = serves
       print(f"{self.player_name} Stats - Attacks: {attacks}, Blocks: {blocks}, Serves: {serves}")
    
   


x1 = Besiktas("Abraham", "Forward")
x2 = Besiktas("Rafa Silva", "Attacking Midfielder")
y1 = Besiktas_Esports("Can", "Midlaner")   
y2 = Besiktas_Esports("Berke", "IGL")
z1 = Besiktas_Volleyball("Ebrar", "Middle Blocker")
z2 = Besiktas_Volleyball("Merve", "Outside Hitter")

print(x1, type(x1))
print(x2, type(x2))
print(y1, type(y1))
print(y2, type(y2))
print(z1, type(z1))
print(z2, type(z2))

x1.player_info()
x1.player_stats(7, 2)
x2.player_info()
x2.player_stats(5, 2)
y1.esport_info_1()
y1.record_kda(12, 2, 6)
y2.esport_info_1()
y2.record_kda(8, 5, 10)
z1.volleyball_info_2()
z1.record_stats(15, 5, 8)
z2.volleyball_info_2() 
z2.record_stats(18, 4, 7)


