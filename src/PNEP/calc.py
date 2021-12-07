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
print("Val", rouge.get_scores(hypothesis, reference, avg = True))

src = []
selected_idx = []
cnt_gt2: int= 0
with open(src_path, 'r') as f:
    lines = f.readlines()
    for idx, l in enumerate(lines):
        utters = l.split('#')
        occur_planning = [_i.strip() for _i in utters[0].strip()[1:-1].split('|') ]
        if len(occur_planning) > 2:
            cnt_gt2 += 1
            selected_idx.append(idx)
        src.append(l[:-1])

with open(selected_gene_path, 'w') as f:
    for idx in selected_idx:
        f.write(hypothesis[idx])
        f.write('\n')

with open(selected_ref_path, 'w') as f:
    for idx in selected_idx:
        f.write(reference[idx])
        f.write('\n')

with open(selected_src_path, 'w') as f:
    for idx in selected_idx:
        f.write(src[idx])
        f.write('\n')

print("{} cases with more than 2 people in SAMSum-test.".format(cnt_gt2))