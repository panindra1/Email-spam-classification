import math
import operator

HomeDirectory = "/home/tvsamartha/Pycharm_Projects/Email-spam-classification/"

training_data = []
test_data = []
spam_dict = {}
not_spam_dict = {}
total_spam = 0
total_not_spam = 0
spam_counter = 0
not_spam_counter = 0
p_spam_dict = {}
p_not_spam_dict = {}
p_spam = 0.0
p_not_spam = 0.0
k = 80
v = 2


def computeProbabilities():
    for word in spam_dict:
        val = spam_dict.get(word)

        p_spam_dict.update({word: (math.log( ((val + k) * 1.0)/(total_spam + k * v))) })

    for word in not_spam_dict:
        val = not_spam_dict.get(word)
        p_not_spam_dict.update({word: (math.log( ((val + k) * 1.0)/(total_not_spam + k * v))) })

    p_spam = math.log(((total_spam *1.0)/ (total_spam + total_not_spam)))
    p_not_spam = math.log(((total_not_spam *1.0) / (total_spam + total_not_spam)))

   # print(p_spam_dict)

def calc_accuracy():
    correct_class = 0
    total_rows = 0

    with open(HomeDirectory+ "test_email.txt")as f:
        test_data = f.readlines()
        for line in test_data:
          total_rows = total_rows + 1
          class_val = int(line[0])
          words = line[2:].split(" ")

          val_spam = 0
          val_not_spam = 0

          for word in words:
              split_word = word.split(":")
              keyword = split_word[0]
              if(p_spam_dict.has_key(keyword)):
                  val_spam += p_spam_dict.get(keyword)

              if(p_not_spam_dict.has_key(keyword)):
                  val_not_spam += p_not_spam_dict.get(keyword)

          val_spam += (p_spam)
          val_not_spam += (p_not_spam)

          test_classes = 1 if(val_spam < val_not_spam) else 0
          if(class_val == test_classes):
              correct_class += 1

    print(correct_class)
    print((correct_class * 1.0)/ total_rows)

def main():

    temp_spam_dict = sorted(spam_dict.items(), key=operator.itemgetter(1), reverse=True)

    line_counter = 0
    spam_output_file = open("spam_output.txt", "w")
    for tup in temp_spam_dict:
        if(line_counter < 400):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            spam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break

    temp_notspam_dict = sorted(not_spam_dict.items(), key=operator.itemgetter(1), reverse=True)

    line_counter = 0
    notspam_output_file = open("notspam_output.txt", "w")
    for tup in temp_notspam_dict:
        if(line_counter < 400):
            final_str = ""
            for i in xrange(0, tup[1]):
                final_str += tup[0] + " "
            notspam_output_file.write(final_str + "\n")
            line_counter+=1
        else :
            break

    #print(not_spam_dict)
    computeProbabilities()
    calc_accuracy()
    sorted_spam = sorted(p_spam_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_not_spam = sorted(p_not_spam_dict.items(), key=operator.itemgetter(1), reverse=True)

    print("TOP 20 SPAM")
    i = 0
    for key in sorted_spam:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break
    print("TOP 20 NOT SPAM")
    i = 0
    for key in sorted_not_spam:
        print(key[0] +" : " +str(key[1]))
        i += 1
        if(i == 20):
            break

if __name__ == "__main__":
    with open(HomeDirectory+ "train_email.txt")as f:
      training_data = f.readlines()

      for line in training_data:
          class_val = int(line[0])
          words = line[2:].split(" ")
          for word in words:
              split_word = word.split(":")
              current_word = split_word[0]
              frequency = int(split_word[1])

              if(class_val == 1):
                spam_counter += 1
                total_spam += frequency
                if spam_dict.has_key(current_word):
                    val = spam_dict.get(current_word)
                    val += frequency
                    spam_dict.update({current_word: val})
                else:
                    spam_dict.update({current_word: frequency})
              else:
                  not_spam_counter += 1
                  total_not_spam += frequency
                  if not_spam_dict.has_key(current_word):
                    val = not_spam_dict.get(current_word)
                    val += frequency
                    not_spam_dict.update({current_word: val})
                  else:
                    not_spam_dict.update({current_word: frequency})

    main()