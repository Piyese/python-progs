import pickle
import sys,time,random

story={
   1:{
      "Text":[
         "hello there...",
         "sure you didn't expect yo hear from me too soon",
         "do you even remember me"
         ],
      "Options":[
         ("yea of course",2),
         ("im sorry.. No!!",3)
         ]
   }
}

with open("chapter1.ch",'wb') as chapter:
   pickle.dump(story,chapter)

def slow_type(t:str):
   typing_speed=100#wpm
   for letter in t:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(random.random()*10/typing_speed)
      
def display_text(lines:list):
   for line in lines:
      slow_type(line)
      get_input([''])
      
def get_input(valid_inputs:list):
   while True:
      entered_input=input()
      if entered_input not in valid_inputs:
         print("invalid input, use one of the following")
         print(valid_inputs)
         entered_input=None
         
      else:
         return entered_input
         
def get_response(options:list):
   for index,option in enumerate(options):
      print(f'{index}. {options[0]}')
      
      valid_inputs=[str(num) for num in range(len(options)) ]
      options_index=int(get_input(valid_inputs))
      return options[options_index][1]
      
def story_flow(story:dict):
   current_page=1
   while current_page!=None:
      page=story.get(current_page, None)
      
      if page==None:
         current_page=None
         break
      
      display_text(page['Text'])
      
      if len(page['Options'])==0:
         current_page=None
         break
      
      current_page=get_response(page['Options'])
 """     
import pickle
if __name__ == "__main__":
   
   story= {}
   with open('chapter1.ch', 'rb') as file:
        story = pickle.load(file)
        story_flow(story)    
"""