from contextlib import contextmanager

@contextmanager
def generic(card_type, sender_name, recipient):
  #print('Opening File')
  read_card = open(card_type, 'r')
  write_card = open(f"{sender_name}_generic.txt", 'w')

  try: 
    write_card.write(f"Dear {recipient}, \n")
    write_card.write(read_card.read())
    write_card.write(f"Sincerely, {sender_name} \n")
    yield write_card

  finally:
    #print('Closing File')
    read_card.close()
    write_card.close()

with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as new_card:
 #print('Card Generated! \n')
  with open('Mwenda_generic.txt', 'r') as card_new:
    print(card_new.read())  

class Personalized:
  def __init__(self, sender_name, reciever_name):
    self.file = open(f"{sender_name}_personalized.txt", 'w')
    self.sender_name = sender_name
    self.reciever_name = reciever_name

  def __enter__(self):
    self.file.write(f"Dear {self.reciever_name}, \n \n")
    return self.file

  def __exit__(self, *exc):
    self.file.write(f"Sincerely {self.sender_name}")
    self.file.close()

with Personalized('John', 'Michael') as card_first:
  card_first.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with generic('happy_bday.txt', 'Josiah', 'Remy') as bday_card:
  with Personalized('Josiah', 'Esther') as esther_card:
    esther_card.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")
    #print(bday_card, esther_card)
