import json
import random

def read_rules():
    rules = []
    with open('rules_text.json') as rules_json:
        rules = eval(json.dumps(json.load(rules_json)))
    return rules

def perform_replacement(string_built, rules, a_val, b_val):
    new_str = ""
    #print('starting_string:', string_built)
    changes_made = False
    for char in string_built:
        # print(char)
        if char in rules.keys():
            rule_for_char = rules[char]
            if rule_for_char[1] > 0:
                rule_for_char[1] -= 1
                replacement = random.choice(rules[char][0])
                #print(replacement)
                if replacement == 'a':
                    replacement = str(a_val)
                elif replacement == 'b':
                    replacement = str(b_val)
                new_str += replacement
                changes_made = True
                #print('max_gen val: ', rules[char][1])
            else:
                new_str += rule_for_char[0][0]
                changes_made = True
        else:
            new_str += char
    return new_str, changes_made


def generate_rule_set(rule_dict):
    #print('rule_dict', rule_dict)
    rule_reformat = {}
    for header in rule_dict:
        all_rules = rule_dict[header]
        #print('all_rules', all_rules)
        for rule in all_rules:
            #print('rule', rule)
            rule_reformat[rule['statement']] = [rule['replacements'], rule['max_gen']]
    #print('rule_reformat', rule_reformat)
    return rule_reformat



def main():
    set_of_rules = generate_rule_set(read_rules())
    orig_base_str = 's'
    max_iterations = 3
    cur_iterations = 0
    max_pushups = 30
    a_val = input('enter a:')
    b_val = input('enter b:')
    #print(a_val, b_val)
    maxVal = 0
    max_base = ""
    max_abs = ""
    while(cur_iterations < max_iterations):
        base_str = orig_base_str
        set_of_rules = generate_rule_set(read_rules())
        change = True
        while(change):
            change = False
            updated, change = perform_replacement(base_str, set_of_rules, a_val, b_val)
            # print('updated', updated)
            base_str = updated
        cur_iterations+=1

        #print(base_str)
        # print(eval(base_str))
        abs_wrapped = 'abs(' + base_str + ')'
        max_base_str = str(max_pushups) + ' if (' + str(eval(abs_wrapped)) + ') > ' + str(max_pushups) + ' else ' + str(eval(abs_wrapped))
        #print(max_base_str)
        value = eval(max_base_str)
        if value > maxVal:
            maxVal = value
            max_abs = max_base_str
            max_base = base_str
        # ret_str = "print('pushups: '," + max_base_str +')'
        # baby_str = "print('pushups: '," + base_str +')'
        #print(ret_str)
        # print('absolute and max value')
        # exec(ret_str)
        # print('regular')
        # exec(baby_str)
    
    print(max_base)
    print(max_abs)
    print('pushups: ', maxVal)
    
    

if __name__ == "__main__":
    main()


