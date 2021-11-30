import random

list1 = ["AH","AD","AC","AS",
         "2H","2D","2C","2S",
         "3H","3D","3C","3S",
         "4H","4D","4C","4S",
         "5H","5D","5C","5S",
         "6H","6D","6C","6S",
         "7H","7D","7C","7S",
         "8H","8D","8C","8S",
         "9H","9D","9C","9S",
         "10H","10D","10C","10S",
         "JH","JD","JC","JS",
         "QH","QD","QC","QS",
         "KH","KD","KC","KS"]



random.shuffle(list1)


player_hand = list1[0:2]
print(player_hand)

del list1[0:2]

dealer_hand = list1[0:2]
print(dealer_hand)

del list1[0:2]

del list1[0:1]

first_table_hand = list1[0:3]

print(first_table_hand)

del list1[0:3]

del list1[0:1]

second_table_hand = first_table_hand + list1[0:1]

del list1[0]

full_table_hand = second_table_hand + list1[0:1]

print(full_table_hand)

useful_cards = full_table_hand + player_hand

print(useful_cards)

number_list = []

for i in useful_cards:
    number = i[0]
    number_list.append(number)
  
print(number_list)
  
for w in number_list:
    
    del number_list[0]
    print(number_list)
    print(w)
    if w in number_list:
        continue
