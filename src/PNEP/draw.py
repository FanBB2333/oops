import matplotlib.pyplot as plt
import numpy as np

PNEP_txt = './selected/SAMSum_generation_OCC_Planning_selected.txt'  # generated summary
SBART_txt = './selected/test_generations_selected.txt'  # generated summary

target_txt = './selected/test_selected.target'

src_txt = './selected/text_test_selected.source'

abs_deg_PNEP = []  # abstraction degree
abs_deg_SBART = []  # abstraction degree

original_lens = []  # original length
original_times = []  # 人物出现次数
occur_plannings = []  # occur planning



with open(src_txt, 'r') as f:
    lines = f.readlines()
    for idx, l in enumerate(lines):
        utters = l.split('#')
        original_len = [len(p.split()) for p in utters[1:]]
        original_lens.append(np.sum(original_len))
        occur_planning = [_i.strip() for _i in utters[0].strip()[1:-1].split('|') ]
        occur_plannings.append(occur_planning)
        times = [l.count(n)-1 for n in occur_planning]
        original_times.append(np.sum(times))


summarized_lens = []  # length
summarized_times = []  # 人物出现次数

with open(PNEP_txt, 'r') as f:
    lines = f.readlines()
    for idx, l in enumerate(lines):

        summarized_lens.append(len(l.split()))
        occur_planning = occur_plannings[idx]
        times = [l.count(n) for n in occur_planning]
        summarized_times.append(np.sum(times))

summarized_lens2 = []  # length
summarized_times2 = []  # 人物出现次数

with open(SBART_txt, 'r') as f:
    lines = f.readlines()
    for idx, l in enumerate(lines):
        summarized_lens2.append(len(l.split()))
        occur_planning = occur_plannings[idx]
        times = [l.count(n) for n in occur_planning]
        summarized_times2.append(np.sum(times))


summarized_SAMSum_lens = []  # length
summarized_SAMSum_times = []  # 人物出现次数

with open(target_txt, 'r') as f:
    lines = f.readlines()
    for idx, l in enumerate(lines):
        summarized_SAMSum_lens.append(len(l.split()))
        occur_planning = occur_plannings[idx]
        times = [l.count(n) for n in occur_planning]
        summarized_SAMSum_times.append(np.sum(times))

if __name__ == '__main__':
    # using length
    abs_deg_PNEP = np.array(summarized_lens) / np.array(original_lens)
    abs_deg_SBART = np.array(summarized_lens2) / np.array(original_lens)
    plt.subplot(3, 2, 1)
    plt.title('PNEP')
    plt.ylabel('times~length ratio')
    plt.hist(abs_deg_PNEP, bins=20, label='PNEP', density=True)
    plt.subplot(3, 2, 2)
    plt.title('SBART')
    plt.hist(abs_deg_SBART, bins=20, label='SBART', density=True)

    # using times
    abs_deg_PNEP = np.array(summarized_times) / np.array(original_times)
    abs_deg_SBART = np.array(summarized_times2) / np.array(original_times)
    plt.subplot(3, 2, 3)
    plt.ylabel('times~names freq ratio')
    plt.hist(abs_deg_PNEP, bins=20, label='PNEP', density=True)
    plt.subplot(3, 2, 4)

    plt.hist(abs_deg_SBART, bins=20, label='SBART', density=True)
    # plt.savefig('fig.png')

    # fg = plt.figure()
    plt.subplot(3, 2, 5)
    plt.xlabel('length')

    plt.hist(np.array(summarized_SAMSum_lens) / np.array(original_lens), bins=20, label='SAMSum', density=True)

    plt.subplot(3, 2, 6)
    plt.xlabel('names freq')
    plt.hist(np.array(summarized_SAMSum_times) / np.array(original_times), bins=20, label='SAMSum', density=True)
    plt.savefig('fig.png')
    plt.show()
