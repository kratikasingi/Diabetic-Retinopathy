10 pass step
20 pass step
30 pass step
---------------------------------------------------------------------------
NotADirectoryError                        Traceback (most recent call last)
<ipython-input-20-e2926a7b7054> in <module>
     15     # getting ids of file images
     16     for dir in os.listdir(test_dir):
---> 17         for file in os.listdir(os.path.join(test_dir, dir)):
     18             img_id = os.path.splitext(file)[0]
     19             img_ids.append(img_id)

NotADirectoryError: [Errno 20] Not a directory: '../input/aptos2019-blindness-detection/test_images/42bef0737ac1.png'
Output exceeds the size limit. Open the full output data in a text editor
[tensor([2, 2, 2, 2, 2, 2, 2, 1, 3, 0, 4, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2,
         2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0, 3, 2, 2, 2, 2, 1, 2, 2, 3,
         2, 2, 3, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 3, 2], device='cuda:0'),
 tensor([2, 3, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 3, 0, 0, 0, 2, 2, 1, 2, 2, 2, 2,
         2, 1, 2, 2, 2, 2, 2, 2, 1, 0, 2, 2, 1, 0, 0, 2, 2, 2, 3, 2, 2, 0, 2, 3,
         2, 1, 2, 2, 4, 0, 2, 2, 0, 0, 3, 2, 3, 2, 2, 2], device='cuda:0'),
 tensor([0, 1, 0, 2, 2, 1, 2, 2, 2, 2, 0, 2, 4, 1, 2, 4, 2, 2, 0, 1, 0, 2, 1, 2,
         2, 0, 1, 1, 2, 2, 2, 0, 2, 2, 2, 2, 2, 4, 0, 4, 3, 0, 0, 2, 4, 2, 2, 2,
         2, 3, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 2, 2], device='cuda:0'),
 tensor([0, 2, 2, 2, 4, 1, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 2, 0, 2, 2, 2, 0, 2,
         2, 2, 2, 2, 2, 0, 0, 2, 4, 2, 2, 2, 0, 2, 2, 2, 1, 1, 3, 2, 2, 2, 2, 0,
         0, 2, 2, 0, 0, 2, 2, 4, 0, 0, 0, 1, 0, 2, 2, 0], device='cuda:0'),
 tensor([0, 1, 2, 3, 2, 2, 0, 0, 2, 2, 3, 0, 3, 2, 0, 0, 1, 0, 2, 2, 2, 4, 3, 2,
         2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 2, 2, 1, 2, 0, 1, 2, 2, 2, 0, 2, 2, 2,
         2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 2, 1, 2, 2, 2], device='cuda:0'),
 tensor([0, 0, 1, 0, 2, 4, 2, 1, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 2,
         2, 1, 0, 2, 0, 2, 2, 2, 0, 2, 2, 1, 3, 2, 0, 1, 2, 2, 2, 2, 2, 0, 1, 2,
         2, 2, 2, 2, 0, 2, 2, 0, 4, 3, 2, 2, 2, 2, 1, 2], device='cuda:0'),
 tensor([2, 2, 1, 2, 0, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2,
         2, 0, 0, 1, 1, 3, 2, 1, 0, 1, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2,
         2, 1, 2, 2, 4, 2, 0, 0, 2, 1, 0, 2, 2, 2, 0, 2], device='cuda:0'),
 tensor([3, 0, 1, 2, 2, 2, 0, 2, 2, 2, 2, 4, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 1, 0,
         2, 0, 0, 3, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 2, 0, 2, 3, 1, 2,
         3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4, 2, 0], device='cuda:0'),
 tensor([2, 2, 0, 2, 2, 2, 1, 2, 2, 0, 2, 1, 0, 2, 2, 1, 2, 2, 2, 2, 0, 3, 2, 1,
...
         2, 1, 2, 2, 0, 1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2], device='cuda:0'),
 tensor([0, 1, 0, 2, 0, 2, 2, 3, 1, 2, 3, 2, 1, 2, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2,
         4, 0, 2, 2, 4, 2, 1, 2, 0, 0, 0, 2, 2, 2, 4, 2, 2, 2, 0, 0, 0, 2, 2, 2,
         1, 2, 4, 0, 2, 2, 0, 3, 2, 2, 2, 2, 2, 1, 2, 2], device='cuda:0'),
 tensor([2, 2, 2, 0, 2, 2, 3, 0], device='cuda:0')]
<bound method NDFrame.head of            id_code  diagnosis
0     0005cfc8afb6          2
1     003f0afdcd15          2
2     006efc72b638          2
3     00836aaacf06          2
4     009245722fa4          2
...            ...        ...
1923  ff2fd94448de          0
1924  ff4c945d9b17          2
1925  ff64897ac0d8          2
1926  ffa73465b705          3
1927  ffdc2152d455          0

[1928 rows x 2 columns]>
conv1is frozen
bn1is frozen
reluis frozen
maxpoolis frozen
layer1is frozen
layer2is unfrozen
layer3is unfrozen
layer4is unfrozen
avgpoolis frozen
fcis unfrozen
