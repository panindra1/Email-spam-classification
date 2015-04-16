__author__ = 'panindra'
import math
import operator

HomeDirectory = "/home/panindra/PycharmProjects/NaiveBayes/"
training_data = []
test_data = []
class_dict = {}

space_dict = {}
hardware_dict = {}
baseball_dict = {}
windows_dict = {}
politics_dict = {}
forsale_dict = {}
hockey_dict = {}
graphics_dict = {}

p_space_dict = {}
p_hardware_dict = {}
p_baseball_dict = {}
p_windows_dict = {}
p_politics_dict = {}
p_forsale_dict = {}
p_hockey_dict = {}
p_graphics_dict = {}

p_space = 0.0
p_hardware = 0.0
p_baseball = 0.0
p_windows = 0.0
p_politics = 0.0
p_forsale = 0.0
p_hockey = 0.0
p_graphics = 0.0


total_space_counter = 0
total_hardware_counter = 0
total_baseball_counter = 0
total_windows_counter = 0
total_politics_counter = 0
total_forsale_counter = 0
total_hockey_counter = 0
total_graphics_counter = 0

space_counter = 0
hardware_counter = 0
baseball_counter = 0
windows_counter = 0
politics_counter = 0
forsale_counter = 0
hockey_counter = 0
graphics_counter = 0

total_counter = 0

k = 1
v = 8

def compute_probabilities():
     for word in space_dict:
        val = space_dict.get(word)
        p_space_dict.update({word: (math.log( ((val + k) * 1.0)/(total_space_counter + (k * v)) )) })

     for word in hardware_dict:
        val = hardware_dict.get(word)
        p_hardware_dict.update({word: (math.log( ((val + k) * 1.0)/(total_hardware_counter + (k * v)) )) })

     for word in baseball_dict:
        val = baseball_dict.get(word)
        p_baseball_dict.update({word: (math.log( ((val + k) * 1.0)/(total_baseball_counter + (k * v))) ) })

     for word in windows_dict:
        val = windows_dict.get(word)
        p_windows_dict.update({word: (math.log( ((val + k) * 1.0)/(total_windows_counter + (k * v))) ) })

     for word in politics_dict:
        val = politics_dict.get(word)
        p_politics_dict.update({word: (math.log( ((val + k) * 1.0)/(total_politics_counter + (k * v))) ) })

     for word in forsale_dict:
        val = forsale_dict.get(word)
        p_forsale_dict.update({word: (math.log( ((val + k) * 1.0)/(total_forsale_counter + (k * v))) ) })

     for word in hockey_dict:
        val = hockey_dict.get(word)
        p_hockey_dict.update({word: (math.log( ((val + k) * 1.0)/(total_hockey_counter + (k * v))) ) })

     for word in graphics_dict:
        val = graphics_dict.get(word)
        p_graphics_dict.update({word: (math.log( ((val + k) * 1.0)/(total_graphics_counter + (k * v)) )) })

     p_space = math.log((total_space_counter *1.0)/ total_counter)
     p_hardware = math.log((total_hardware_counter *1.0)/ total_counter)
     p_baseball = math.log((total_baseball_counter *1.0)/ total_counter)
     p_windows = math.log((total_windows_counter *1.0)/ total_counter)
     p_politics = math.log((total_politics_counter *1.0)/ total_counter)
     p_forsale = math.log((total_forsale_counter *1.0)/ total_counter)
     p_hockey = math.log((total_hockey_counter *1.0)/ total_counter)
     p_graphics = math.log((total_graphics_counter *1.0)/ total_counter)

def compute_odds_ratio(class1, class2):
    odds_ratio_dict = {}
    for word,val in class1.items():
        if(word in class2):
            not_spam_val = class2.get(word)
            odds_ratio_dict[word] = val * 1.0/not_spam_val

    sorted_odds_ratio = sorted(odds_ratio_dict.items(), key=operator.itemgetter(1), reverse=True)
    print("**************************************************")
    i = 0
    for key in sorted_odds_ratio:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break

def calc_accuracy():
    correct_class = 0
    total_rows = 0

    with open(HomeDirectory+ "8category.testing.txt")as f:
        test_data = f.readlines()
        for line in test_data:
          total_rows = total_rows + 1
          class_val = int(line[0])
          words = line[2:].split(" ")

          val_space = 0
          val_hardware = 0
          val_baseball = 0
          val_windows = 0
          val_politics = 0
          val_forsale = 0
          val_hockey = 0
          val_graphics = 0

          for word in words:
              split_word = word.split(":")
              keyword = split_word[0]

              if(p_space_dict.has_key(keyword)):
                  val_space += p_space_dict.get(keyword)

              if(p_hardware_dict.has_key(keyword)):
                  val_hardware += p_hardware_dict.get(keyword)

              if(p_baseball_dict.has_key(keyword)):
                  val_baseball += p_baseball_dict.get(keyword)

              if(p_windows_dict.has_key(keyword)):
                  val_windows += p_windows_dict.get(keyword)

              if(p_politics_dict.has_key(keyword)):
                  val_politics += p_politics_dict.get(keyword)

              if(p_forsale_dict.has_key(keyword)):
                  val_forsale += p_forsale_dict.get(keyword)

              if(p_hockey_dict.has_key(keyword)):
                  val_hockey += p_hockey_dict.get(keyword)

              if(p_graphics_dict.has_key(keyword)):
                  val_graphics += p_graphics_dict.get(keyword)


          val_space += p_space
          val_hardware += p_hardware
          val_baseball += p_baseball
          val_windows += p_windows
          val_politics += p_politics
          val_forsale += p_forsale
          val_hockey += p_hockey
          val_graphics += p_graphics

          high_class_values = [val_space, val_hardware, val_baseball, val_windows, val_politics, val_forsale, val_hockey, val_graphics]
          if(class_val == give_class_val(high_class_values)):
              correct_class += 1

        print(correct_class)
        print((correct_class * 1.0)/ total_rows)

def give_class_val(class_values):
    index = 0
    value = 0
    i = 0
    for val in class_values:
        if(value > val):
            value = val
            index = i
        i += 1

    return index


def main():
    compute_probabilities()
    calc_accuracy()

    sorted_space_dict = sorted(p_space_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_hardware_dict = sorted(p_hardware_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_baseball_dict = sorted(p_baseball_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_windows_dict = sorted(p_windows_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_politics_dict = sorted(p_politics_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_forsale_dict = sorted(p_forsale_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_hockey_dict = sorted(p_hockey_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_graphics_dict = sorted(p_graphics_dict.items(), key=operator.itemgetter(1), reverse=True)



    print("TOP 20 SPACE")
    i = 0
    for key in sorted_space_dict:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break

    print("TOP 20 HARDWARE")
    i = 0
    for key in sorted_hardware_dict:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break

    print("TOP 20 BASEBALL")
    i = 0
    for key in sorted_baseball_dict:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break

    print("TOP 20 WINDOWS")
    i = 0
    for key in sorted_windows_dict:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break

    print("TOP 20 POLITICS")
    i = 0
    for key in sorted_politics_dict:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break

    print("TOP 20 FORSALE")
    i = 0
    for key in sorted_forsale_dict:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break

    print("TOP 20 HOCKEY")
    i = 0
    for key in sorted_hockey_dict:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break

    print("TOP 20 GRAPHICS")
    i = 0
    for key in sorted_graphics_dict:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break


if __name__ == "__main__":
    with open(HomeDirectory+ "8category.training.txt")as f:
      training_data = f.readlines()
      for line in training_data:
          total_counter += 1
          class_val = int(line[0])

          words = line[2:].split(" ")
          for word in words:
              split_word = word.split(":")
              current_word = split_word[0]
              frequency = int(split_word[1])
              val = 0

              if(class_val == 0):
                  space_counter += 1
                  total_space_counter += frequency
                  if space_dict.has_key(current_word):
                    val = space_dict.get(current_word)
                    val += frequency
                    space_dict.update({current_word: val})
                  else:
                    space_dict.update({current_word: frequency})

              elif(class_val == 1):
                  hardware_counter += 1
                  total_hardware_counter += frequency
                  if hardware_dict.has_key(current_word):
                    val = hardware_dict.get(current_word)
                    val += frequency
                    hardware_dict.update({current_word: val})
                  else:
                    hardware_dict.update({current_word: frequency})

              elif(class_val == 2):
                  baseball_counter += 1
                  total_baseball_counter += frequency
                  if baseball_dict.has_key(current_word):
                    val = baseball_dict.get(current_word)
                    val += frequency
                    baseball_dict.update({current_word: val})
                  else:
                    baseball_dict.update({current_word: frequency})

              elif(class_val == 3):
                  windows_counter += 1
                  total_windows_counter += frequency
                  if windows_dict.has_key(current_word):
                    val = windows_dict.get(current_word)
                    val += frequency
                    windows_dict.update({current_word: val})
                  else:
                    windows_dict.update({current_word: frequency})

              elif(class_val == 4):
                  politics_counter += 1
                  total_politics_counter += frequency
                  if politics_dict.has_key(current_word):
                    val = politics_dict.get(current_word)
                    val += frequency
                    politics_dict.update({current_word: val})
                  else:
                    politics_dict.update({current_word: frequency})

              elif(class_val == 5):
                  forsale_counter += 1
                  total_forsale_counter += frequency
                  if forsale_dict.has_key(current_word):
                    val = forsale_dict.get(current_word)
                    val += frequency
                    forsale_dict.update({current_word: val})
                  else:
                    forsale_dict.update({current_word: frequency})

              elif(class_val == 6):
                  hockey_counter += 1
                  total_hockey_counter += frequency
                  if hockey_dict.has_key(current_word):
                    val = hockey_dict.get(current_word)
                    val += frequency
                    hockey_dict.update({current_word: val})
                  else:
                    hockey_dict.update({current_word: frequency})

              elif(class_val == 7):
                  graphics_counter += 1
                  total_graphics_counter += frequency
                  if graphics_dict.has_key(current_word):
                    val = graphics_dict.get(current_word)
                    val += frequency
                    graphics_dict.update({current_word: val})
                  else:
                    graphics_dict.update({current_word: frequency})

    main()
    compute_odds_ratio(p_space_dict, p_hardware_dict)
    compute_odds_ratio(p_graphics_dict, p_baseball_dict)
    compute_odds_ratio(p_hockey_dict, p_baseball_dict)
    compute_odds_ratio(p_forsale_dict, p_politics_dict)