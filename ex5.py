name = 'Zed A. Shaw'
age = 35 # not a lie
height_inches = 74 # inches
height_cm = height_inches * 2.54
weight_lbs = 180 #lbs
weight_kg = weight_lbs / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall or %d cm tall." % (height_inches, height_cm)
print "He's %d pounds heavy or %d kg heavy." % (weight_lbs, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (
    age, height_inches, weight_lbs, age + height_inches + weight_lbs)
