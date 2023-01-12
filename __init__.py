from mycroft.messagebus import Message
from mycroft.skills import (
  MycroftSkill,
  intent_handler
)

class Aliases(MycroftSkill):
  def __init__(self, skill_id: str):
    super().__init__(skill_id=skill_id, name="AliasesSkill")

    @intent_handler('example.intent')
    def handle_alias_example(self, message):
      self.bus.emit(Message(
        "recognizer_loop:utterance",  
        {
          'utterances': ["What time is it"],
          'lang': 'en-us'
        }
      )) 
      dialog="Yo"
      return self.end_session(dialog=dialog, gui=None)

def create_skill(skill_id: str):
  return Aliases(skill_id=skill_id)
