
"""
v1
def get_mood(day):
    if day == 'Monday':
        return 'Oh...'
    if day == 'Thursday':
        return 'Getting close!'
    if day == 'Friday':
        return 'Almost there!'
    if day == 'Saturday' or day == 'Sunday':
        return 'Weekend!!!'
    return 'Meh...'
    
"""    
    
    
def mood_get(day):
   match day:
     case 'Monday':
         return 'Oh...'
     case 'Thursday':
         return 'Getting close!'
     case 'Friday':
         return 'Almost there!'
     case 'Saturday' | 'Sunday':
         return 'Weekend!!!'
     case _:
            return 'Meh...'
            
"""
def get_mood(day):
   mappings={
      "Monday":"bloody...",
      "Thursday":"everything is just so vibrant",
      "Friday":"weeeeeeekend!!",
      "Saturday":"weeeeeeekend!!",
      "Sunday":"boored!!!"
   }
   
   try:
      return mappings[day]
   except KeyError:
      return 'Meeeh..'
"""

#print(get_mood("Sunday"))
print(mood_get("Saturday"))