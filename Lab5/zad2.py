from simpful import *

FS = FuzzySystem()

speed1 = TrapezoidFuzzySet(0, 0, 20, 65, term="low")
speed2 = TriangleFuzzySet(15, 65, 115, term="medium")
speed3 = TriangleFuzzySet(65, 115, 115, term="high")
FS.add_linguistic_variable("speed", LinguisticVariable([speed1, speed2, speed3], universe_of_discourse=[0, 120]))

distance1 = TrapezoidFuzzySet(0, 0, 25, 45, term="low")
distance2 = TrapezoidFuzzySet(20, 45, 105, 130, term="medium")
distance3 = TriangleFuzzySet(105, 130, 130, term="high")
FS.add_linguistic_variable("distance",
                           LinguisticVariable([distance1, distance2, distance3],
                                              universe_of_discourse=[0, 140]))

acceleration1 = TrapezoidFuzzySet(-1, -1, -0.4, 0, term="highM")
acceleration2 = TriangleFuzzySet(-0.4, 0, 0.1, term="lowM")
acceleration3 = TriangleFuzzySet(-0.1, 0, 0.4, term="lowP")
acceleration4 = TriangleFuzzySet(0, 0.4, 0.4, term="highP")
FS.add_linguistic_variable("acceleration",
                           LinguisticVariable([acceleration1, acceleration2, acceleration3, acceleration4],
                                              universe_of_discourse=[-1, 1]))

# FS.plot_variable("distance")
# FS.plot_variable("speed")
# FS.plot_variable("acceleration")


FS.add_rules([
    "IF (distance IS low) AND (speed IS low) THEN (acceleration IS highM)",
    "IF (distance IS medium) AND (speed IS low) THEN (acceleration IS lowM)",
    "IF (distance IS high) AND (speed IS low) THEN (acceleration IS lowM)",
    "IF (distance IS low) AND (speed IS medium) THEN (acceleration IS highP)",
    "IF (distance IS medium) AND (speed IS medium) THEN (acceleration IS lowM)",
    "IF (distance IS high) AND (speed IS medium) THEN (acceleration IS lowM)",
    "IF (distance IS low) AND (speed IS high) THEN (acceleration IS lowP)",
    "IF (distance IS medium) AND (speed IS high) THEN (acceleration IS highM)",
    "IF (distance IS high) AND (speed IS high) THEN (acceleration IS lowM)",
])


FS.set_variable("distance", 20)
FS.set_variable("speed", 65)

result = FS.inference()

print(result)
