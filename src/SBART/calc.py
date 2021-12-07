from rouge import Rouge, FilesRouge


hyp_path = './composit/test_generations.txt'
selected_gene_path = './selected/test_generations_selected.txt'  # generated summary

ref_path = './data/test.target'
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
    for i, idx in enumerate(selected_idx):
        f.write(str(rouge_scores[idx]) + '\n')
        f.write(str(i+1) + ': ' + hypothesis[idx] + '\n')