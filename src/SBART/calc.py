from rouge import Rouge, FilesRouge


hyp_path = './composit/test_generations.txt'
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
print("Val", rouge.get_scores(hypothesis, reference, avg = True))