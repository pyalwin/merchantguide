roman_values = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000
}


def convert_to_numbers(inp_roman_string):
    result = 0
    prev_value = 0

    for char in inp_roman_string[::-1]:
        char_value = roman_values[char]
        if char_value >= prev_value:
            result += char_value
            prev_value = char_value
        else:
            result -= char_value
    
    return result

def translate_to_codes(vals, codes):
    inp_string = ''
    metal = None
    for item in vals.split():
      if item in codes.keys():
        inp_string += codes[item]
      else:
        metal = item
    inp_value = convert_to_numbers(inp_string)
    return (inp_value, codes, metal)

def merchant_code(inputs):
  codes = {}
  metals = {}
  answers = []
  for sentence in inputs:
    split_sentence = sentence.split()
    if split_sentence[-1] in roman_values.keys():
      codes[split_sentence[0]] = split_sentence[-1]
    elif split_sentence[-1] == 'Credits':
      if codes:
        vals = sentence.split(' is ')[0]
        credit_value = split_sentence[::-1][1]
        (inp_value, codes, metal) = translate_to_codes(vals, codes)
        metals[metal] = int(credit_value) / inp_value
    else:
      try:
        question = sentence.split(' is ')[1]
        question = question.split(' ?')[0]
        (inp_value, codes, metal) = translate_to_codes(question,codes) 
        if metal:
          final_value = int(inp_value * metals[metal])
          answers.append(question + ' is ' + str(final_value) + ' Credits') 
        else:
          answers.append(question + ' is ' + str(inp_value)) 
      except Exception as e:
        answers.append('I have no idea what you are talking about')

  print (codes, answers)


merchant_code(['glob is I', 'prok is V', 'pish is X','tegj is L', 'hnga is C','glob glob Silver is 34 Credits', 'glob prok Gold is 57800 Credits', 'pish pish Iron is 3910 Credits', 'how much is pish hnga glob glob ?', 'how many Credits is glob prok Silver ?','how many Credits is glob prok Gold ?','how many Credits is glob prok Iron ?', 'how many Credits is glob prok Wood ?'])
        
        

      

    


