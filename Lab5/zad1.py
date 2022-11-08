from simpful import *

FS = FuzzySystem()

TLV = AutoTriangle(3, terms=['poor', 'average', 'good'], universe_of_discourse=[0,10])
FS.add_linguistic_variable("service", TLV)
FS.add_linguistic_variable("quality", TLV)

O1 = TriangleFuzzySet(0,0,16,   term="low")
O2 = TriangleFuzzySet(0,16,30,  term="medium")
O3 = TriangleFuzzySet(16,30,30, term="high")
FS.add_linguistic_variable("tip", LinguisticVariable([O1, O2, O3], universe_of_discourse=[0,30]))

FS.add_rules([
	"IF (quality IS poor) OR (service IS poor) THEN (tip IS low)",
	"IF (service IS average) THEN (tip IS medium)",
	"IF (quality IS good) OR (quality IS good) THEN (tip IS high)"
	])

FS.set_variable("quality", 3)
FS.set_variable("service", 8)

tipMamdani = FS.Mamdani_inference()


print(tipMamdani)
FS.plot_variable("quality")
FS.plot_variable("service")
FS.plot_variable("tip")
