from rouge import Rouge
rouge = Rouge()

hyp_path = './model_outputs/SAMSum_generation_OCC_Planning.txt'  # generated summary
ref_path = './model_outputs/test.target'
src_path = './text_test.source'

hypothesis = []
with open(hyp_path, 'r') as f:
    lines = f.readlines()
    for l in lines:
        hypothesis.append(l[:-1])

reference = []
with open(ref_path, 'r') as f:
    lines = f.readlines()
    for l in lines:
        reference.append(l[:-1])

rouge = Rouge()
print("Val", rouge.get_scores(hypothesis, reference, avg = True))

src = []
above_2: int= 0
with open(src_path, 'r') as f:
    lines = f.readlines()
    for l in lines:
        utters = l.split('#')
        occur_planning = [_i.strip() for _i in utters[0].strip()[1:-1].split('|') ]
        if len(occur_planning) > 2:
            above_2 += 1
        src.append(l[:-1])
print("There are {} sentences with more than 2 people".format(above_2))