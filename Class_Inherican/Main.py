from Class_Animal import Animal
from Class_Pig import Pig
from Class_Fish import Fish
from Class_Horse import Horse

pig = Pig()
horse = Horse()
fish = Fish()

print(f"Животното pig живо ли е: {pig.alive}")
horse.eat()
fish.sleep()

pig.Run()
horse.Galop()
fish.Swim()