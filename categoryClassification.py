__author__ = 'panindra'
import math
import operator

HomeDirectory = "/home/tvsamartha/Pycharm_Projects/Email-spam-classification/"
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

k = 100
v = 8

def compute_probabilities():
     global v
     for word in space_dict:
        val = space_dict.get(word)
        p_space_dict.update({word: (math.log( ((val + k) * 1.0)/(total_space_counter + k * v) )) })

     for word in hardware_dict:
        val = hardware_dict.get(word)
        p_hardware_dict.update({word: (math.log( ((val + k) * 1.0)/(total_hardware_counter + k * v) )) })

     for word in baseball_dict:
        val = baseball_dict.get(word)
        p_baseball_dict.update({word: (math.log( ((val + k) * 1.0)/(total_baseball_counter + k * v)) ) })

     for word in windows_dict:
        val = windows_dict.get(word)
        p_windows_dict.update({word: (math.log( ((val + k) * 1.0)/(total_windows_counter + k * v)) ) })

     for word in politics_dict:
        val = politics_dict.get(word)
        p_politics_dict.update({word: (math.log( ((val + k) * 1.0)/(total_politics_counter + k * v)) ) })

     for word in forsale_dict:
        val = forsale_dict.get(word)
        p_forsale_dict.update({word: (math.log( ((val + k) * 1.0)/(total_forsale_counter + k * v)) ) })

     for word in hockey_dict:
        val = hockey_dict.get(word)
        p_hockey_dict.update({word: (math.log( ((val + k) * 1.0)/(total_hockey_counter + k * v)) ) })

     for word in graphics_dict:
        val = graphics_dict.get(word)
        p_graphics_dict.update({word: (math.log( ((val + k) * 1.0)/(total_graphics_counter + k * v) )) })

     global p_space, p_hardware, p_baseball, p_windows, p_politics, p_forsale, p_hockey, p_graphics
     p_space = math.log((space_counter *1.0)/ total_counter)
     p_hardware = math.log((hardware_counter *1.0)/ total_counter)
     p_baseball = math.log((baseball_counter *1.0)/ total_counter)
     p_windows = math.log((windows_counter *1.0)/ total_counter)
     p_politics = math.log((politics_counter *1.0)/ total_counter)
     p_forsale = math.log((forsale_counter *1.0)/ total_counter)
     p_hockey = math.log((hockey_counter *1.0)/ total_counter)
     p_graphics = math.log((graphics_counter *1.0)/ total_counter)

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

    Matrix = [[0 for x in range(8)] for x in range(8)]
    confusion_matrix = [[0 for x in range(8)] for x in range(8)]

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
              frequency = int(split_word[1]) * 1.0

              if(p_space_dict.has_key(keyword)):
                  val_space += p_space_dict.get(keyword) * frequency

              if(p_hardware_dict.has_key(keyword)):
                  val_hardware += p_hardware_dict.get(keyword) * frequency

              if(p_baseball_dict.has_key(keyword)):
                  val_baseball += p_baseball_dict.get(keyword) * frequency

              if(p_windows_dict.has_key(keyword)):
                  val_windows += p_windows_dict.get(keyword) * frequency

              if(p_politics_dict.has_key(keyword)):
                  val_politics += p_politics_dict.get(keyword) * frequency

              if(p_forsale_dict.has_key(keyword)):
                  val_forsale += p_forsale_dict.get(keyword) * frequency

              if(p_hockey_dict.has_key(keyword)):
                  val_hockey += p_hockey_dict.get(keyword) * frequency

              if(p_graphics_dict.has_key(keyword)):
                  val_graphics += p_graphics_dict.get(keyword) * frequency


          val_space += p_space
          val_hardware += p_hardware
          val_baseball += p_baseball
          val_windows += p_windows
          val_politics += p_politics
          val_forsale += p_forsale
          val_hockey += p_hockey
          val_graphics += p_graphics

          high_class_values = [val_space, val_hardware, val_baseball, val_windows, val_politics, val_forsale, val_hockey, val_graphics]
          classifed_class = give_class_val(high_class_values)
          if(class_val == classifed_class):
            predicted_class = give_class_val(high_class_values)

          if(class_val == predicted_class):
              correct_class += 1
          confusion_matrix[class_val][predicted_class]+=1

        print("Confusion matrix ")

        for rows in xrange(0, len(confusion_matrix)):
            print(confusion_matrix[rows])


        #print(correct_class)

        Matrix[class_val][classifed_class] += 1

        print(correct_class)
        print((correct_class * 1.0)/ total_rows)
        for line in Matrix:
            print(line)
        print("\nAccuracy = " + str((correct_class * 1.0)/ total_rows))

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

def print_words_for_tag_cloud():
    temp_space_dict = sorted(space_dict.items(), key=operator.itemgetter(1), reverse=True)
    line_counter = 0
    spam_output_file = open("space_output.txt", "w")
    for tup in temp_space_dict:
        if(line_counter < 300):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            spam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break


    temp_hardware_dict = sorted(hardware_dict.items(), key=operator.itemgetter(1), reverse=True)
    line_counter = 0
    notspam_output_file = open("hardware_output.txt", "w")
    for tup in temp_hardware_dict:
        if(line_counter < 300):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            notspam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break


    temp_baseball_dict = sorted(baseball_dict.items(), key=operator.itemgetter(1), reverse=True)
    line_counter = 0
    notspam_output_file = open("baseball_output.txt", "w")
    for tup in temp_baseball_dict:
        if(line_counter < 300):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            notspam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break


    temp_windows_dict = sorted(windows_dict.items(), key=operator.itemgetter(1), reverse=True)
    line_counter = 0
    notspam_output_file = open("windows_output.txt", "w")
    for tup in temp_windows_dict:
        if(line_counter < 300):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            notspam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break


    temp_politics_dict = sorted(politics_dict.items(), key=operator.itemgetter(1), reverse=True)
    line_counter = 0
    notspam_output_file = open("politics_output.txt", "w")
    for tup in temp_politics_dict:
        if(line_counter < 300):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            notspam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break

    temp_forsale_dict = sorted(forsale_dict.items(), key=operator.itemgetter(1), reverse=True)
    line_counter = 0
    notspam_output_file = open("forsale_output.txt", "w")
    for tup in temp_forsale_dict:
        if(line_counter < 300):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            notspam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break

    temp_hockey_dict = sorted(hockey_dict.items(), key=operator.itemgetter(1), reverse=True)
    line_counter = 0
    notspam_output_file = open("hockey_output.txt", "w")
    for tup in temp_hockey_dict:
        if(line_counter < 300):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            notspam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break

    temp_graphics_dict = sorted(graphics_dict.items(), key=operator.itemgetter(1), reverse=True)
    line_counter = 0
    notspam_output_file = open("graphics_output.txt", "w")
    for tup in temp_graphics_dict:
        if(line_counter < 300):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            notspam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break


if __name__ == "__main__":
    with open(HomeDirectory+ "8category.training.txt")as f:
      training_data = f.readlines()
      for line in training_data:
          total_counter += 1
          class_val = int(line[0])
          if(class_val == 0):
              space_counter += 1
          elif(class_val == 1):
              hardware_counter += 1
          elif(class_val == 2):
              baseball_counter += 1
          elif(class_val == 3):
              windows_counter += 1
          elif(class_val == 4):
              politics_counter += 1
          elif(class_val == 5):
              forsale_counter += 1
          elif(class_val == 6):
              hockey_counter += 1
          elif(class_val == 7):
              graphics_counter += 1

          words = line[2:].split(" ")
          for word in words:
              split_word = word.split(":")
              current_word = split_word[0]
              frequency = int(split_word[1])
              val = 0

              if(class_val == 0):
                  total_space_counter += frequency
                  if space_dict.has_key(current_word):
                    val = space_dict.get(current_word)
                    val += frequency
                    space_dict.update({current_word: val})
                  else:
                    space_dict.update({current_word: frequency})

              elif(class_val == 1):
                  total_hardware_counter += frequency
                  if hardware_dict.has_key(current_word):
                    val = hardware_dict.get(current_word)
                    val += frequency
                    hardware_dict.update({current_word: val})
                  else:
                    hardware_dict.update({current_word: frequency})

              elif(class_val == 2):
                  total_baseball_counter += frequency
                  if baseball_dict.has_key(current_word):
                    val = baseball_dict.get(current_word)
                    val += frequency
                    baseball_dict.update({current_word: val})
                  else:
                    baseball_dict.update({current_word: frequency})

              elif(class_val == 3):
                  total_windows_counter += frequency
                  if windows_dict.has_key(current_word):
                    val = windows_dict.get(current_word)
                    val += frequency
                    windows_dict.update({current_word: val})
                  else:
                    windows_dict.update({current_word: frequency})

              elif(class_val == 4):
                  total_politics_counter += frequency
                  if politics_dict.has_key(current_word):
                    val = politics_dict.get(current_word)
                    val += frequency
                    politics_dict.update({current_word: val})
                  else:
                    politics_dict.update({current_word: frequency})

              elif(class_val == 5):
                  total_forsale_counter += frequency
                  if forsale_dict.has_key(current_word):
                    val = forsale_dict.get(current_word)
                    val += frequency
                    forsale_dict.update({current_word: val})
                  else:
                    forsale_dict.update({current_word: frequency})

              elif(class_val == 6):
                  total_hockey_counter += frequency
                  if hockey_dict.has_key(current_word):
                    val = hockey_dict.get(current_word)
                    val += frequency
                    hockey_dict.update({current_word: val})
                  else:
                    hockey_dict.update({current_word: frequency})

              elif(class_val == 7):
                  total_graphics_counter += frequency
                  if graphics_dict.has_key(current_word):
                    val = graphics_dict.get(current_word)
                    val += frequency
                    graphics_dict.update({current_word: val})
                  else:
                    graphics_dict.update({current_word: frequency})


    space_keys = set(space_dict.keys())
    hardware_keys = set(hardware_dict.keys())
    baseball_keys = set(baseball_dict.keys())
    windows_keys = set(windows_dict.keys())
    politics_keys = set(politics_dict.keys())
    forsale_keys = set(forsale_dict.keys())
    hockey_keys = set(hockey_dict.keys())
    graphics_keys = set(graphics_dict.keys())

    s = set.intersection(space_keys, hardware_keys, baseball_keys, windows_keys, politics_keys, forsale_keys, hockey_keys, graphics_keys)
    v = len(space_keys) + len(hardware_keys) + len(baseball_keys) + len(windows_keys) + len(politics_keys) + len(forsale_keys) + len(hockey_keys) + len(graphics_keys) - len(s)

    main()
    compute_odds_ratio(p_space_dict, p_politics_dict)
    compute_odds_ratio(p_windows_dict, p_graphics_dict)
    compute_odds_ratio(p_hardware_dict, p_graphics_dict)
    compute_odds_ratio(p_hardware_dict, p_windows_dict)
    print_words_for_tag_cloud()
