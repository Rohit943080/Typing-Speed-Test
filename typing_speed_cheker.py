import time


def net_speed(sentence):

    print('Type the Sentence: \n')
    print(sentence)

    incorrect_word = 0

    start = time.time()
    input_word = input('\n Your attempt: ').strip()
    end = time.time()

    # Time in minutes
    total_time = (end - start) / 60

    typed_word = input_word.split()
    actual_word = sentence.strip().split()

    incorrect_word_list = []

    # compare words
    for tp_word, act_word in zip(typed_word, sentence.split()):
        if tp_word != act_word:
            incorrect_word_list.append(tp_word)
            incorrect_word += 1

    # Count extra typed words
    if len(typed_word) > len(actual_word):
        incorrect_word_list.extend(typed_word[len(actual_word):])
        incorrect_word += len(typed_word) - len(actual_word)

    # Speed
    gross_speed = len(typed_word) / total_time
    net_speed = (len(typed_word) - incorrect_word) / total_time

    # Accuracy
    accuracy = round(
        ((len(typed_word) - incorrect_word) / len(typed_word)) * 100, 2) if typed_word else 0

    result = f'''
   Total Time Taken {round(end - start, 2)} Seconds

   Your net speed is {round(net_speed, 2)} WPM

   Your gross speed  is {round(gross_speed, 2)} WPM

   Accuracy is {accuracy} %
   
   Total Wrong word - {incorrect_word_list}

'''
    return result


sentence = '''
    Typing speed is calculated by dividing the number of correctly typed words (net words) 
    
    by the time taken (in minutes) to get Net Words Per Minute (NWPM), or by dividing the total 
    
    number of words typed (gross words) by the time to get Gross Words Per Minute (GWPM)

'''

print(net_speed(sentence))
