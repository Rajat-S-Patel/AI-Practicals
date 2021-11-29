medicalTree = ['Do you have fever?',
               ['Do you have cough?',
                ['Do you have headache?',
                 ['Do you have body ache?',
                  ['Flu'],
                  ['Do you have rash?',
                   ['Do you have chills?',
                    ['Common Cold'],
                    ['German Measles']
                    ],
                   ['Chicken Pox']
                   ]
                  ], ['Measles']
                 ],
                ['Do you have swollen glands?',
                 ['Mumps'],
                 ['Common Cold']]
                ],
               ['Are you Sneezing?',
                ['Do you have headache?',
                 ['Flu'],
                 ['Allergies']
                 ],
                ['Healthy Body']
                ,
                
                ],
                
               ]


def expert(tree):
    currentNode = tree
    while len(currentNode) == 3:
        [question, yesNode, noNode] = currentNode  # name the parts of the list
        if agree(question):
            currentNode = yesNode
        else:
            currentNode = noNode
    # When the while loop is over, currentNode is a leaf with a single element.       
    [result] = currentNode
    print("You have {}".format(result))


def agree(question):
    answer = input(question + ' (y/n) ')
    return answer.startswith('y')


def prettyStr(tree, indent='', dif='  '):
    if len(tree) == 1:
        return indent + repr(tree)  # repr(string) -> quoted form used in programs
    
    else:
        [question, t1, t2] = tree
        t1Str = prettyStr(t1, indent + dif)
        t2Str = prettyStr(t2, indent + dif)
        return '''{indent}[{question!r},
    {t1Str},
    {t2Str}
    {indent}]'''.format(**locals())


if __name__ == '__main__':
    tree = medicalTree
    print("\nUsing this expert system tree:\n")
    print(prettyStr(tree))
    expert(tree)
        