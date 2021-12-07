from rouge import Rouge
rouge = Rouge()

hyp_path = './model_outputs/SAMSum_generation_OCC_Planning.txt'  # generated summary
selected_gene_path = './selected/SAMSum_generation_OCC_Planning_selected.txt'  # generated summary

ref_path = './model_outputs/test.target'
selected_ref_path = './selected/test_selected.target'

src_path = './text_test.source'
selected_src_path = './selected/text_test_selected.source'

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
rouge_scores = rouge.get_scores(hypothesis, reference)
print(type(rouge_scores))
print("Val", rouge.get_scores(hypothesis, reference, avg = True))

src = []
selected_idx = []
cnt_gt2: int= 0
with open(src_path, 'r') as f:
    lines = f.readlines()
    for idx, l in enumerate(lines):
        utters = l.split('#')
        occur_planning = [_i.strip() for _i in utters[0].strip()[1:-1].split('|') ]
        if len(occur_planning) > 3:
            cnt_gt2 += 1
            selected_idx.append(idx)
        src.append(l[:-1])

with open(selected_gene_path, 'w') as f:
    for i, idx in enumerate(selected_idx):
        f.write(str(rouge_scores[idx]) + '\n')
        f.write(str(i+1) + ': ' + hypothesis[idx] + '\n')

with open(selected_ref_path, 'w') as f:
    for i, idx in enumerate(selected_idx):
        f.write(str(i+1) + ': ' + reference[idx] + '\n')

with open(selected_src_path, 'w') as f:
    for i, idx in enumerate(selected_idx):
        f.write(str(i+1) + ': ' + src[idx] + '\n')

s_bart = './selected/test_generations_selected.txt'  # generated summary
hypothesis = []
with open('../SBART/composit/test_generations.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        hypothesis.append(l[:-1])
rouge = Rouge()
rouge_scores = rouge.get_scores(hypothesis, reference)
with open(s_bart, 'w') as f:
    for i, idx in enumerate(selected_idx):
        f.write(str(rouge_scores[idx]) + '\n')
        f.write(str(i+1) + ': ' + hypothesis[idx] + '\n')

print("{} cases with more than 2 people in SAMSum-test.".format(cnt_gt2))